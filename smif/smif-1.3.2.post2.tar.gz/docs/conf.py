# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its containing dir.

# To run the docs build directly, generate module index:
#   rm -r docs/api ; sphinx-apidoc -f -M -o docs/api smif
# Then build docs:
#   rm -r docs/_build ; sphinx-build -b html docs docs/_build/html

# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# -- Hack for ReadTheDocs and apidoc options -----------------------------------
# This hack is necessary since RTD does not issue `sphinx-apidoc` before running
# If extensions (or modules to document with autodoc) are in another directory,
# DON'T FORGET: Check the box "Install your project inside a virtualenv using
# setup.py install" in the RTD Advanced Settings.
# `sphinx-build -b html . _build/html`. See Issue:
# https://github.com/rtfd/readthedocs.org/issues/1139

# It also appears necessary in order to pass options to sphinx-apidoc which obr
# or setuptools don't currently allow. See issue:
# https://github.com/sphinx-doc/sphinx/issues/1861

import inspect
import os
import sys
from unittest.mock import MagicMock

import better_apidoc

# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.join(__location__, '../src'))


class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


# mock modules which we can avoid installing for docs-building
mock_modules = [
    'dateutil',
    'dateutil.parser',
    'fiona',
    'flask',
    'flask.views',
    'isodate',
    'minio',
    'minio.error',
    'networkx',
    'numpy',
    'pint',
    'pyarrow',
    'rtree',
    'ruamel.yaml',
    'shapely',
    'shapely.geometry',
    'shapely.validation',
    'pandas',
    'pandas.core',
    'pandas.core.internals',
    'xarray'
]
sys.modules.update((mod_name, Mock()) for mod_name in mock_modules)

output_dir = os.path.join(__location__, "api")
module_dir = os.path.join(__location__, "../src/smif")
templates_dir = os.path.join(__location__, "_templates")

better_apidoc.main([
    'better-apidoc',
    '-t',
    templates_dir,
    '--force',
    '--separate',
    '-o',
    output_dir,
    module_dir
])

# -- General configuration -----------------------------------------------------


# Extra styles, found in _static
def setup(app):
    app.add_stylesheet('theme_tweaks.css')


# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon',
              'sphinx.ext.inheritance_diagram', 'sphinx.ext.autosummary',
              'sphinx.ext.imgmath', 'sphinx.ext.intersphinx', 'sphinx.ext.todo',
              'sphinx.ext.autosummary', 'sphinx.ext.viewcode',
              'sphinx.ext.coverage', 'sphinx.ext.doctest',
              'sphinx.ext.ifconfig', 'sphinx.ext.graphviz', 'sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'smif'
copyright = u'2017, Will Usher, Tom Russell'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''  # Is set by calling `setup.py docs`
# The full version, including alpha/beta/rc tags.
release = ''  # Is set by calling `setup.py docs`

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '../tests/**']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'paraiso-dark'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['smif.']

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
try:
    from smif import __version__
    version = __version__
except ImportError:
    pass
else:
    release = version

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = ""

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'smif-doc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'user_guide.tex', u'smif Documentation',
     u'Will Usher & Tom Russell', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = ""

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

# -- External mapping ------------------------------------------------------------
python_version = '.'.join(map(str, sys.version_info[0:2]))
intersphinx_mapping = {
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'python': ('https://docs.python.org/' + python_version, None),
    'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
    'xarray': ('http://xarray.pydata.org/en/stable/', None),
}
