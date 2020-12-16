# -*- coding: utf-8 -*-

"""
Module et_micc.project
======================

An OO interface to *micc* projects.

"""
import os
import shutil
import json
from pathlib import Path
import subprocess
from operator import xor
from types import SimpleNamespace
import json

import click
import semantic_version
from sphinx.cmd.build import main as sphinx_build

from et_micc.tomlfile import TomlFile
import et_micc.utils
import et_micc.expand
import et_micc.logger
from et_micc import __version__
# from et_micc.db import Database

CURRENT_ET_MICC_BUILD_VERSION = __version__


def micc_version():
    return __version__


class Project:
    """
    An OO interface to *micc* projects.

    :param types.SimpleNameSpace options: all options from the ``micc`` CLI.
    """

    def __init__(self, options):
        self.exit_code = 0
        self.logger = None
        self.options = options
        project_path = options.project_path

        if hasattr(options, 'template_parameters'):
            # only needed for expanding templates.
            # Pick up the default parameters
            default_parameters = {}
            template_parameters_json = project_path / 'micc.json'
            if template_parameters_json.exists():
                default_parameters.update(
                    et_micc.expand.get_template_parameters(template_parameters_json)
                )
            else:
                default_parameters.update(
                    et_micc.expand.get_template_parameters(
                        et_micc.expand.get_preferences(Path('.'))
                    )
                )
            # Add options.template_parameters to the default parameters
            # (options.template_parameters takes precedence, so they must be added last)
            default_parameters.update(options.template_parameters)
            # Store all the parameters in options.template_parameters.
            options.template_parameters = default_parameters

        if et_micc.utils.is_project_directory(project_path, self):
            # existing project
            self.get_logger()
            self.version = self.pyproject_toml['tool']['poetry']['version']

            with et_micc.utils.in_directory(self.project_path):
                with open('db.json', 'r') as f:
                    self.db = json.load(f)

        else:
            # not a project directory or not a directory at all
            if getattr(options, 'create', False):
                if project_path.exists() and os.listdir(str(project_path)):
                    self.error(f"Cannot create project in ({project_path}):\n"
                               f"  Directory must be empty."
                               )
                else:
                    self.create()
            else:
                # all other micc commands require a project directory.
                self.error(f"Not a project directory ({project_path}).")

    @property
    def project_path(self):
        return self.options.project_path

    def error(self, msg):
        """Print an error message :py:obj:`msg` and set the project's :py:obj:`exit_code`."""
        click.secho("[ERROR]\n" + msg, fg='bright_red')
        self.exit_code = 1

    def warning(self, msg):
        """Print an warning message :py:obj:`msg` and set the project's :py:obj:`exit_code`."""
        click.secho("[WARNING]\n" + msg, fg='green')

    def create(self):
        """Create a new project skeleton."""

        self.project_path.mkdir(parents=True, exist_ok=True)

        if not self.options.allow_nesting:
            # Prevent the creation of a project inside another project
            p = self.project_path.parent.resolve()
            while not p.samefile('/'):
                if et_micc.utils.is_project_directory(p):
                    self.error(f"Cannot create project in ({self.project_path}):\n"
                               f"  Specify '--allow-nesting' to create a et_micc project inside another et_micc project ({p})."
                               )
                    return
                p = p.parent

        project_name = self.project_path.name
        if not et_micc.utils.verify_project_name(project_name):
            self.error(f"Invalid project name ({project_name}):\n"
                       f"  project name must start with char, and contain only chars, digits, hyphens and underscores."
                       )
            return
        self.project_name = project_name
        self.package_name = et_micc.utils.pep8_module_name(project_name)
        try:
            relative_project_path = self.project_path.relative_to(Path.cwd())
        except ValueError:
            # project_path was specified relative to cwd using ../
            # use full path instead of relative path
            relative_project_path = self.project_path

        if self.options.publish:
            is_publishable = et_micc.utils.is_publishable(self.package_name,verbose=self.options.verbosity>1)
            if is_publishable is None:
                self.error(f"    Could not verify availability of name '{self.package_name}' on PyPI.\n"
                           f"    Are you online?\n"
                           f"    The project is not created."
                )
                return
            elif not is_publishable:
                self.error(
                    f"    The name '{self.package_name}' is already in use on PyPI.\n"
                    f"    The project is not created. You must choose another name if you want to publish."
                )
                return

        if self.options.structure == 'module':
            structure = f"({relative_project_path}{os.sep}{self.package_name}.py)"
        elif self.options.structure == 'package':
            structure = f"({relative_project_path}{os.sep}{self.package_name}{os.sep}__init__.py)"
        else:
            structure = ''

        self.options.verbosity = max(1, self.options.verbosity)
        self.get_logger()
        with et_micc.logger.logtime(self):
            with et_micc.logger.log(self.logger.info
                    , f"Creating project ({self.project_name}):"
                                    ):
                self.logger.info(f"Python {self.options.structure} ({self.package_name}): structure = {structure}")
                template_parameters = {'project_name': self.project_name
                    , 'package_name': self.package_name
                                       }
                template_parameters.update(self.options.template_parameters)
                self.options.template_parameters = template_parameters
                self.options.overwrite = False

                self.exit_code = et_micc.expand.expand_templates(self.options)
                if self.exit_code:
                    self.logger.critical(f"Exiting ({self.exit_code}) ...")
                    return

                my_micc_file = self.project_path / 'micc.json'
                with my_micc_file.open('w') as f:
                    json.dump(template_parameters, f)
                    self.logger.debug(f" . Wrote project template parameters to {my_micc_file}.")

                with et_micc.logger.log(self.logger.info, "Creating git repository"):
                    with et_micc.utils.in_directory(self.project_path):
                        cmds = [['git', 'init']
                            , ['git', 'add', '*']
                            , ['git', 'add', '.gitignore']
                            , ['git', 'commit', '-m', '"first commit"']
                        ]
                        if template_parameters['github_username']:
                            cmds.extend(
                                [ ['git', 'remote', 'add', 'origin',
                                  f"https://github.com/{template_parameters['github_username']}/{self.project_name}"]
                                , ['git', 'push', '-u', 'origin', 'master']
                                ]
                            )
                        et_micc.utils.execute(cmds, self.logger.debug, stop_on_error=False)

                self.logger.warning(
                    "Run 'poetry install' in the project directory to create a virtual "
                    "environment and install its dependencies."
                )
        if self.options.publish:
            self.logger.info(f"The name '{self.package_name}' is still available on PyPI.")
            self.logger.warning("To claim the name, it is best to publish your project now\n"
                                "by running 'poetry publish'."
            )

        self.db = {}
        with et_micc.utils.in_directory(self.project_path):
            with open('db.json','w') as f:
                json.dump (self.db, f)


    def module_to_package_cmd(self):
        """Convert a module project (:file:`module.py`) to a package project (:file:`package/__init__.py`)."""
        if self.package:
            self.warning(f"Project ({self.project_name}) is already a package ({self.package}).")
            return

        self.logger.info(
            f"Converting Python module project {self.project_name} to Python package project."
        )

        # add documentation files for general Python project
        self.options.templates = "package-general-docs"
        self.options.template_parameters.update(
            {'project_short_description': self.pyproject_toml['tool']['poetry']['description']}
        )
        self.exit_code = et_micc.expand.expand_templates(self.options)
        if self.exit_code:
            self.logger.critical(
                f"Expand failed during Project.module_to_package_cmd for project ({self.project_name})."
            )
            return

        # move <package_name>.py to <package_name>/__init__.py
        package_path = self.project_path / self.package_name
        package_path.mkdir(exist_ok=True)
        src = self.project_path / (self.package_name + '.py')
        dst = self.project_path / self.package_name / '__init__.py'
        shutil.move(src, dst)


    def info_cmd(self):
        """Output info on the project."""
        if self.options.verbosity >= 0:
            self.options.verbosity = 10

        if self.options.verbosity >= 1:
            click.echo("Project " + click.style(str(self.project_name), fg='green')
                       + " located at "
                       + click.style(str(self.project_path), fg='green')
                       + "\n  package: " + click.style(str(self.package_name), fg='green')
                       + "\n  version: " + click.style(self.version, fg='green')
                       )

        if self.options.verbosity >= 2:
            if self.module:
                kind = " (Python module)"
                source = str(self.module)
            else:
                kind = " (Python package)"
                source = str(self.package)
            click.echo("  structure: " + click.style(source, fg='green') + kind)

        if self.options.verbosity >= 3 and self.package:
            package_path = self.project_path / self.package_name
            files = []
            files.extend(package_path.glob('**/*.py'))
            files.extend(package_path.glob('**/cpp_*/'))
            files.extend(package_path.glob('**/f90_*'))
            if len(files) > 1:  # __init__.py is always there.
                click.echo("  contents:")
                for f in files:
                    # filters
                    if '{' in str(f):
                        continue
                    if 'package-' in str(f):  # very ad hoc solution, only relevant to the et_micc project itself
                        continue
                    if f.name == "__init__.py" and f.parent.samefile(package_path):  # ignore the top-level __init__.py
                        continue
                    if 'build_' in str(f):
                        continue

                    fg = 'green'
                    extra = ''
                    if f.name.startswith('cli'):
                        kind = "application "
                        fg = 'blue'
                    elif f.name.startswith('cpp_'):
                        kind = "C++ module  "
                        extra = f"{os.sep}{f.name.split('_', 1)[1]}.cpp"
                    elif f.name.startswith('f90_'):
                        kind = "f90 module "
                        extra = f"{os.sep}{f.name.split('_', 1)[1]}.f90"
                    elif f.name == '__init__.py':
                        kind = "package     "
                    else:
                        kind = "module      "
                    click.echo("    " + kind + click.style(str(f.relative_to(package_path)) + extra, fg=fg))


    def version_cmd(self):
        """Bump the version according to :py:obj:`self.options.rule` or show the
        current version if no rule is specified.

        The version is stored in pyproject.toml in the project directory, and in
        :py:obj:`__version__` variable of the top-level package, which is either
        in :file:`<package_name>.py`, :file:`<package_name>/__init__.py`, or in
        :file:`<package_name>/__version__.py`.
        """
        self.options.verbosity = max(1, self.options.verbosity)

        if not self.options.rule:
            if self.options.short:
                print(self.version)
            else:
                click.echo("Project " + click.style(f"({self.project_name}) ", fg='cyan')
                           + "version " + click.style(f"({self.version}) ", fg='cyan')
                           )
        else:
            r = f"--{self.options.rule}"
            current_semver = semantic_version.Version(self.version)
            if self.options.rule == 'patch':
                new_semver = current_semver.next_patch()
            elif self.options.rule == 'minor':
                new_semver = current_semver.next_minor()
            elif self.options.rule == 'major':
                new_semver = current_semver.next_major()
            else:
                r = f"--rule {self.options.rule}"
                new_semver = semantic_version.Version(self.options.rule)

            # update pyproject.toml
            if not self.options.dry_run:
                self.pyproject_toml['tool']['poetry']['version'] = str(new_semver)
                self.pyproject_toml.save()
                # update __version__
                look_for = f'__version__ = "{current_semver}"'
                replace_with = f'__version__ = "{new_semver}"'
                if self.module:
                    # update in <package_name>.py
                    et_micc.utils.replace_in_file(self.project_path / self.module, look_for, replace_with)
                else:
                    # update in <package_name>/__init__.py
                    p = self.project_path / self.package_name / "__version__.py"
                    if p.exists():
                        et_micc.utils.replace_in_file(p, look_for, replace_with)
                    else:
                        p = self.project_path / self.package
                        et_micc.utils.replace_in_file(p, look_for, replace_with)

                self.logger.info(f"({self.project_name})> micc version ({current_semver}) -> ({new_semver})")
            else:
                click.echo(f"({self.project_name})> micc version {r} --dry-run : "
                           + click.style(f"({current_semver} ", fg='cyan') + "-> "
                           + click.style(f"({new_semver})", fg='cyan')
                           )
            self.version = str(new_semver)  # even if dry run!

    def tag_cmd(self):
        """Create and push a version tag ``v<Major>.<minor>.<patch>`` for the current version."""
        tag = f"v{self.version}"

        with et_micc.utils.in_directory(self.project_path):
            self.logger.info(f"Creating git tag {tag} for project {self.project_name}")
            cmd = ['git', 'tag', '-a', tag, '-m', f'"tag version {self.version}"']
            self.logger.debug(f"Running '{' '.join(cmd)}'")
            completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            self.logger.debug(completed_process.stdout.decode('utf-8'))
            if completed_process.stderr:
                self.logger.critical(completed_process.stderr.decode('utf-8'))

            self.logger.debug(f"Pushing tag {tag} for project {self.project_name}")
            cmd = ['git', 'push', 'origin', tag]
            self.logger.debug(f"Running '{' '.join(cmd)}'")
            completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if completed_process.returncode == 0:
                if completed_process.stdout:
                    self.logger.debug(completed_process.stdout.decode('utf-8'))
            else:
                if completed_process.stdout:
                    self.logger.warning(completed_process.stdout.decode('utf-8'))
                if completed_process.stderr:
                    self.logger.warning(completed_process.stderr.decode('utf-8'))
                self.logger.warning(f"Failed '{' '.join(cmd)}'\nRerun the command later (you must be online).")

        self.logger.info('Done.')


    def add_cmd(self):
        """Add some source file to the project.

        This method dispatches to

        * :py:meth:`add_app`,
        * :py:meth:`add_python_module`,
        * :py:meth:`add_f90_module`,
        * :py:meth:`add_cpp_module`
        """
        if self.module:
            self.error(f"Cannot add to a module project ({self.module}).\n"
                       f"  Use `micc convert-to-package' on this project to convert it to a package project."
                       )
            return

        # set implied flags:
        if self.options.group:
            app_implied = f" [implied by --group   ({int(self.options.group)})]"
            self.options.app = True
        else:
            app_implied = ""

        if self.options.package:
            py_implied = f" [implied by --package ({int(self.options.package)})]"
            self.options.py = True
        else:
            py_implied = ""

        # Verify that one and only one of app/py/f90/cpp flags has been selected:
        if (not (self.options.app or self.options.py or self.options.f90 or self.options.cpp)
                or not xor(xor(self.options.app, self.options.py), xor(self.options.f90, self.options.cpp))):
            # Do not log, as the state of the project is not changed.
            self.error(f"Specify one and only one of \n"
                       f"  --app ({int(self.options.app)}){app_implied}\n"
                       f"  --py  ({int(self.options.py )}){py_implied}\n"
                       f"  --f90 ({int(self.options.f90)})\n"
                       f"  --cpp ({int(self.options.cpp)})\n", fg='bright_red'
                       )
            return

        db_entry = {'options': self.options.__dict__}

        if self.options.app:
            # Prepare for adding an app
            app_name = self.options.add_name
            if self.app_exists(app_name):
                self.error(f"Project {self.project_name} has already an app named {app_name}.")
                return

            if not et_micc.utils.verify_project_name(app_name):
                self.error(
                    f"Not a valid app name ({app_name}_. Valid names:\n"
                    f"  * start with a letter [a-zA-Z]\n"
                    f"  * contain only [a-zA-Z], digits, hyphens, and underscores\n"
                )
                return

            if self.options.group:
                if not self.options.templates:
                    self.options.templates = 'app-sub-commands'
            else:
                if not self.options.templates:
                    self.options.templates = 'app-simple'

            self.add_app(db_entry)

        else:
            # Prepare for adding a sub-module
            module_name = self.options.add_name

            # Verify that the name is not already used:
            if self.module_exists(module_name):
                self.error(f"Project {self.project_name} has already a module named {module_name}.")
                return

            # Verify that the name is valid:
            if (not et_micc.utils.verify_project_name(module_name)
                    or module_name != et_micc.utils.pep8_module_name(module_name)):
                self.error(
                    f"Not a valid module name ({module_name}). Valid names:\n"
                    f"  * start with a letter [a-zA-Z]\n"
                    f"  * contain only [a-zA-Z], digits, and underscores\n"
                )
                return

            if self.options.py:
                # prepare for adding a Python sub-module:
                # self.options.structure = 'package' if self.options.package else 'module'
                if not self.options.templates:
                    self.options.templates = 'module-py'
                self.add_python_module(db_entry)

            elif self.options.f90:
                # prepare for adding a Fortran sub-module:
                if not self.options.templates:
                    self.options.templates = 'module-f90'
                self.add_f90_module(db_entry)

            elif self.options.cpp:
                # prepare for adding a C++ sub-module:
                if not self.options.templates:
                    self.options.templates = 'module-cpp'
                self.add_cpp_module(db_entry)

        self.db[self.options.add_name] = db_entry

        with open('db.json','w') as f:
            json.dump (self.db, f)

    def add_app(self, db_entry):
        """Add a console script (app, aka CLI) to the package."""
        project_path = self.project_path
        app_name = self.options.add_name
        cli_app_name = 'cli_' + et_micc.utils.pep8_module_name(app_name)
        w = 'with' if self.options.group else 'without'

        with et_micc.logger.log(self.logger.info,
                                f"Adding CLI {app_name} {w} sub-commands to project {project_path.name}."):
            self.options.template_parameters.update(
                {'app_name': app_name, 'cli_app_name': cli_app_name}
            )

            self.exit_code = et_micc.expand.expand_templates(self.options)
            if self.exit_code:
                self.logger.critical(
                    f"Expand failed during Project.add_app for project ({self.project_name})."
                )
                return

            package_name = self.options.template_parameters['package_name']
            src_file = os.path.join(project_path.name, package_name, f"cli_{app_name}.py")
            tst_file = os.path.join(project_path.name, 'tests', f"test_cli_{app_name}.py")
            self.logger.info(f"- Python source file {src_file}.")
            self.logger.info(f"- Python test code   {tst_file}.")

            with et_micc.utils.in_directory(project_path):
                # docs
                with open('docs/index.rst', "r") as f:
                    lines = f.readlines()
                has_already_apps = False

                api_line = -1
                for l, line in enumerate(lines):
                    has_already_apps = has_already_apps or line.startswith("   apps")
                    if line.startswith('   api'):
                        api_line = l
                if not has_already_apps:
                    lines.insert(api_line, '   apps\n')
                    with open('docs/index.rst', "w") as f:
                        for line in lines:
                            f.write(line)
                txt = ''
                if not Path('APPS.rst').exists():
                    title = "Command Line Interfaces (apps)"
                    line = len(title) * '*' + '\n'
                    txt += (line
                            + title + '\n'
                            + line
                            + '\n'
                            )
                else:
                    txt += (f".. click:: {package_name}.{cli_app_name}:main\n"
                            f"   :prog: {app_name}\n"
                            f"   :show-nested:\n\n"
                            )
                with open("APPS.rst", "a") as f:
                    f.write(txt)

                # pyproject.toml
                self.add_dependencies({'click': '^7.0.0'})
                self.pyproject_toml['tool']['poetry']['scripts'][app_name] = f"{package_name}:{cli_app_name}.main"
                self.pyproject_toml.save()

                # add 'import <package_name>.cli_<app_name> to __init__.py
                line = f"import {package_name}.cli_{app_name}\n"
                file = project_path / self.package
                et_micc.utils.insert_in_file(file, [line], before=True, startswith="__version__")

    def add_python_module(self, db_entry):
        """Add a python sub-module or sub-package to this project."""
        project_path = self.project_path
        module_name = self.options.add_name

        if not module_name == et_micc.utils.pep8_module_name(module_name):
            self.error(f"Not a valid module_name: {module_name}")
            return

        source_file = f"{module_name}{os.sep}__init__.py" if self.options.package else f"{module_name}.py"
        with et_micc.logger.log(self.logger.info,
                                f"Adding python module {source_file} to project {project_path.name}."
                                ):
            self.options.template_parameters.update({'module_name': module_name})

            # Create the needed folders and files by expanding the templates:
            self.exit_code = et_micc.expand.expand_templates(self.options)
            if self.exit_code:
                self.logger.critical(
                    f"Expand failed during Project.add_python_module for project ({self.project_name})."
                )
                return

            package_name = self.options.template_parameters['package_name']
            if self.options.package:
                self.module_to_package(project_path / package_name / (module_name + '.py'))

            src_file = os.path.join(project_path.name, package_name, source_file)
            tst_file = os.path.join(project_path.name, 'tests', 'test_' + module_name + '.py')

            self.logger.info(f"- python source in    {src_file}.")
            self.logger.info(f"- Python test code in {tst_file}.")

            with et_micc.utils.in_directory(project_path):
                # docs
                filename = "API.rst"
                text = f"\n.. automodule:: {package_name}.{module_name}" \
                        "\n   :members:\n\n"
                with open(filename, "a") as f:
                    f.write(text)
                db_entry[filename] = text

    def add_f90_module(self, db_entry):
        """Add a f90 module to this project."""
        project_path = self.project_path
        module_name = self.options.add_name

        with et_micc.logger.log(self.logger.info,
                                f"Adding f90 module {module_name} to project {project_path.name}."
                                ):
            self.options.template_parameters.update({'module_name': module_name})

            self.exit_code = et_micc.expand.expand_templates(self.options)
            if self.exit_code:
                self.logger.critical(
                    f"Expand failed during Project.add_f90_module for project ({self.project_name})."
                )

            package_name = self.options.template_parameters['package_name']
            src_file = os.path.join(project_path.name
                                    , package_name
                                    , 'f90_' + module_name
                                    , module_name + '.f90'
                                    )
            tst_file = os.path.join(project_path.name
                                    , 'tests'
                                    , 'test_f90_' + module_name + '.py'
                                    )

            rst_file = os.path.join(project_path.name
                                    , package_name
                                    , 'f90_' + module_name
                                    , module_name + '.rst'
                                    )
            self.logger.info(f"- Fortran source in       {src_file}.")
            self.logger.info(f"- Python test code in     {tst_file}.")
            self.logger.info(f"- module documentation in {rst_file} (restructuredText format).")

            with et_micc.utils.in_directory(project_path):
                self.add_dependencies({'et-micc-build': f"^{CURRENT_ET_MICC_BUILD_VERSION}"})
                # docs
                with open("API.rst", "a") as f:
                    f.write(f"\n.. include:: ../{package_name}/f90_{module_name}/{module_name}.rst\n")

        self.add_auto_build_code()

    def add_auto_build_code(self):
        """Add auto build code for binary extension modules in :file:`__init__.py` of the package."""
        module_name = self.options.add_name
        text_to_insert = [
            "",
            "try:",
            f"    import {self.package_name}.{module_name}",
            "except ModuleNotFoundError as e:",
            "    # Try to build this binary extension:",
            "    from pathlib import Path",
            "    import click",
            "    from et_micc_build.cli_micc_build import auto_build_binary_extension",
            f"    msg = auto_build_binary_extension(Path(__file__).parent, '{module_name}')",
            "    if not msg:",
            f"        import {self.package_name}.{module_name}",
            "    else:",
            f"        click.secho(msg, fg='bright_red')",
        ]
        et_micc.utils.insert_in_file(
            self.project_path / self.package_name / "__init__.py",
            text_to_insert,
            startswith="__version__ = ",
        )

    def add_cpp_module(self, db_entry):
        """Add a cpp module to this project."""
        project_path = self.project_path
        module_name = self.options.add_name

        with et_micc.logger.log(self.logger.info,
                                f"Adding cpp module cpp_{module_name} to project {project_path.name}."
                                ):
            self.options.template_parameters.update({'module_name': module_name})

            self.exit_code = et_micc.expand.expand_templates(self.options)
            if self.exit_code:
                self.logger.critical(
                    f"Expand failed during Project.add_cpp_module for project ({self.project_name})."
                )
                return

            package_name = self.options.template_parameters['package_name']
            src_file = os.path.join(project_path.name
                                    , package_name
                                    , 'cpp_' + module_name
                                    , module_name + '.cpp'
                                    )
            tst_file = os.path.join(project_path.name
                                    , 'tests'
                                    , 'test_cpp_' + module_name + '.py'
                                    )

            rst_file = os.path.join(project_path.name
                                    , package_name
                                    , 'cpp_' + module_name
                                    , module_name + '.rst'
                                    )
            self.logger.info(f"- C++ source in           {src_file}.")
            self.logger.info(f"- Python test code in     {tst_file}.")
            self.logger.info(f"- module documentation in {rst_file} (restructuredText format).")

            with et_micc.utils.in_directory(project_path):
                self.add_dependencies({'et-micc-build': f"^{CURRENT_ET_MICC_BUILD_VERSION}"})
                # docs
                with open("API.rst", "a") as f:
                    f.write(f"\n.. include:: ../{package_name}/cpp_{module_name}/{module_name}.rst\n")

        self.add_auto_build_code()

    def app_exists(self, app_name):
        """Test if there is already an app with name ``app_name`` in this project.

        * :file:`<package_name>/cli_<app_name>.py`

        :param str app_name: app name
        :returns: bool
        """
        return (self.project_path / self.package_name / f"cli_{app_name}.py").is_file()

    def module_exists(self, module_name):
        """Test if there is already a module with name py:obj:`module_name` in this project.

        This can be either a Python module, package, or a binary extension module.

        :param str module_name: module name
        :returns: bool
        """
        return (self.py_module_exists(module_name)
                or self.py_package_exists(module_name)
                or self.cpp_module_exists(module_name)
                or self.f90_module_exists(module_name)
                )

    def py_module_exists(self, module_name):
        """Test if there is already a python module with name :py:obj:`module_name`
        in the project at :file:`project_path`.

        :param str module_name: module name
        :returns: bool
        """
        file = self.project_path / self.package_name / f'{module_name}.py'
        return file.is_file()

    def py_package_exists(self, module_name):
        """Test if there is already a python package with name :py:obj:`module_name`
        in the project at :file:`project_path`.

        :param str module_name: module name
        :returns: bool
        """
        return (self.project_path / self.package_name / module_name / '__init__.py').is_file()

    def f90_module_exists(self, module_name):
        """Test if there is already a f90 module with name py:obj:`module_name` in this project.

        :param str module_name: module name
        :returns: bool
        """
        return (self.project_path / self.package_name / ('f90_' + module_name) / f"{module_name}.f90").is_file()

    def cpp_module_exists(self, module_name):
        """Test if there is already a cpp module with name py:obj:`module_name` in this project.

        :param str module_name: module name
        :returns: bool
        """
        return (self.project_path / self.package_name / ('cpp_' + module_name) / f"{module_name}.cpp").is_file()

    def add_dependencies(self, deps):
        """Add dependencies to the :file:`pyproject.toml` file.

        :param dict deps: (package,version_constraint) pairs.
        """
        tool_poetry_dependencies = self.pyproject_toml['tool']['poetry']['dependencies']
        modified = False
        for pkg, version_constraint in deps.items():
            if pkg in tool_poetry_dependencies:
                # project was already depending on this package
                range1 = et_micc.utils.version_range(version_constraint)
                range2 = et_micc.utils.version_range(tool_poetry_dependencies[pkg])
                if range1 == range2:
                    # nothing to do: new and old version specifcation are the same
                    continue
                intersection = et_micc.utils.intersect(range1, range2)
                if et_micc.utils.validate_intersection(intersection):
                    range = intersection
                else:
                    range = et_micc.utils.most_recent(version_constraint, tool_poetry_dependencies[pkg])
                tool_poetry_dependencies[pkg] = et_micc.utils.version_constraint(range)
                modified = True
            else:
                # an entirely new dependency
                tool_poetry_dependencies[pkg] = version_constraint
                modified = True
        if modified:
            self.pyproject_toml.save()
            self.logger.warning("Dependencies added. Run `poetry update` to update the project's virtual environment.")

    def module_to_package(self, module_py):
        """Move file :file:`module.py` to :file:`module/__init__.py`.

        :param str|Path module_py: path to module.py
        """
        module_py = Path(module_py).resolve()

        if not module_py.is_file():
            raise FileNotFoundError(module_py)
        src = str(module_py)

        package_name = str(module_py.name).replace('.py', '')
        package = module_py.parent / package_name
        package.mkdir()
        dst = str(package / '__init__.py')
        shutil.move(src, dst)

        et_micc.logger.log(self.logger.debug,
                           f" . Module {module_py} converted to package {package_name}{os.sep}__init__.py."
                           )

    # removed in favor of docs/Makefile
    # see https://github.com/etijskens/et-micc/issues/24
    # def docs_cmd(self):
    #     """Build documentation."""
    #     docs = self.project_path / 'docs'
    #     open_cmds = []
    #
    #     for format_ in self.options.documentation_formats:
    #         args = ['-M', format_, str(docs), str(docs / '_build')]
    #         self.exit_code = sphinx_build(args)
    #         if self.options.open:
    #             if format_ == 'html':
    #                 open_cmds.append(['open', str(docs / '_build' / 'html' / 'index.html')])
    #             elif format_ == 'latexpdf':
    #                 open_cmds.append(['open', str(docs / '_build' / 'latex' / (self.project_name + ".pdf"))])
    #
    #     if open_cmds:
    #         my_env = os.environ.copy()
    #         et_micc.utils.execute(open_cmds, logfun=print, cwd=str(docs), env=my_env)

    def get_logger(self, log_file_path=None):
        """"""
        if self.logger:
            return

        if log_file_path:
            log_file_name = log_file_path.name
            log_file_dir = log_file_path.parent
        else:
            log_file_name = f"{self.options.project_path.name}.micc.log"
            log_file_dir = self.options.project_path
            log_file_path = log_file_dir / log_file_name
        self.log_file = log_file_path

        if getattr(self.options, 'clear_log', False):
            if log_file_path.exists():
                log_file_path.unlink()

        # create a new logger object that will write to the log file and to the console
        self.logger = et_micc.logger.create_logger(log_file_path)

        # set the log level from the verbosity
        self.logger.console_handler.setLevel(et_micc.logger.verbosity_to_loglevel(self.options.verbosity))

        if self.options.verbosity > 2:
            print(f"Current logfile = {log_file_path}")

        if getattr(self.options, 'clear_log', False):
            self.logger.info(f"The log file was cleared: {log_file_path}")
            self.options.clear_log = False

        self.options.logger = self.logger
# eof
