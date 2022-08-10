# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys


project = 'DIS2RBED LUA Engine'
copyright = '2022, Project W1TCH'
author = 'K1tty'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "myst_parser",
    "sphinx_rtd_dark_mode",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx-rtd-dark-mode'

default_dark_mode = True

html_context = {
     #'source_url_prefix': "https://gitlab.com/ItsK1tty/w1tchdocs/edit/main/docs/source/",
     "display_github": True, # Add 'Edit on Github' link instead of 'View page source'
     "github_user": "ItsK1tty",
     "github_repo": "w1tchdocs",
     "github_version": "main",
     "conf_py_path": "/docs/source/things/", # needs leading and trailing slashes!
}


# -- Options for EPUB output
epub_show_urls = 'footnote'


# def insert_github_link(filename): #https://github.com/peterjc/thapbi-pict/commit/f14b1df17ed3faf382a63095aa6e22f519e71957
#     """Insert file specific :github_url: metadata for theme breadcrumbs."""
#     assert "/" not in filename and filename.endswith(".rst")
#     with open("things/" + filename) as handle:
#         text = handle.read()
#     if ":github_url:" in text:
#         return

#     python = filename[:-4].replace(".", "/") + "/__init__.py"
#     if not os.path.isfile(os.path.join("../", python)):
#         python = filename[:-4].replace(".", "/") + ".py"
#     if not os.path.isfile(os.path.join("../", python)):
#         sys.stderr.write(
#             "WARNING: Could not map %s to a Python file, e.g. %s\n" % (filename, python)
#         )
#         return

#     text = ":github_url: https://github.com/%s/%s/edit/%s\n\n%s" % (
#         html_context["github_user"],
#         html_context["github_repo"],
#         html_context["github_version"],
#         text,
#     )
#     with open("api/" + filename, "w") as handle:
#         handle.write(text)

# for f in os.listdir("things/"):
#     print("Inserting GitHub links for %s" % f)
#     if f.endswith(".rst"):
#         insert_github_link(f)