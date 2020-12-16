import functools

import click
from click_didyoumean import DYMMixin
from click_help_colors import HelpColorsCommand, HelpColorsGroup
from pydantic import UUID4

from tktl.core.loggers import LOG

OPTIONS_FILE_OPTION_NAME = "optionsFile"
OPTIONS_FILE_PARAMETER_NAME = "options_file"
OPTIONS_DUMP_FILE_OPTION_NAME = "createOptionsFile"


class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx) if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail("Too many matches: %s" % ", ".join(sorted(matches)))


class ClickGroup(DYMMixin, HelpColorsGroup, AliasedGroup):
    pass


class ClickCommand(DYMMixin, HelpColorsCommand):
    pass


def deprecated(msg):
    deprecated_invoke_notice = (
        msg
        + """\nFor more information, please see:

https://docs.taktile.com
If you depend on functionality not listed there, please file an issue."""
    )

    def new_invoke(self, ctx):
        click.echo(click.style(deprecated_invoke_notice, fg="red"), err=True)
        super(type(self), self).invoke(ctx)

    def decorator(f):
        f.invoke = functools.partial(new_invoke, f)

    return decorator


_shared_options = [
    click.option("-f", "--full", help="Full (verbose) output", is_flag=True),
    click.option(
        "-a", "--all", "all_resources", help="Return all resources", is_flag=True
    ),
    click.option(
        "-O",
        "--output",
        help="Output as json or yaml ot stdout",
        default="stdout",
        type=click.Choice(["stdout", "json", "yaml"]),
    ),
]


_filter_deploy_shared_options = [
    click.option("-c", "--commit", help="Commit hash"),
    click.option("-b", "--branch", help="Branch name"),
    click.option("-s", "--status", help="Status in which deployment is"),
]


_filter_repo_shared_options = [
    click.option("-r", "--repo", help="Repository name"),
    click.option("-o", "--owner", help="Owner of the repository"),
]


def shared_options_to_decorator(options, func):
    for option in reversed(options):
        func = option(func)
    return func


get_cmd_shared_options = functools.partial(shared_options_to_decorator, _shared_options)
filter_deploy_shared_options = functools.partial(
    shared_options_to_decorator, _filter_deploy_shared_options
)
filter_repo_shared_options = functools.partial(
    shared_options_to_decorator, _filter_repo_shared_options
)


def to_uuid(_, __, x):
    return UUID4(x) if x else None
