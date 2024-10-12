from __future__ import annotations

import os
import sys

from DUMMY.version import __version__


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Dummy"
copyright = "2024, paaalm07"
author = "paaalm07"

version = release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = "index"
templates_path = ["_templates"]
exclude_patterns = ["_build"]

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
]

autodoc_default_options = {
    "members": True,
    "members-order": "bysource",
    "special-members": False,
    "private-members": False,
    "undoc-members": False,
    "inherited-members": False,  # members of base class
    "show-inheritance": True,
    "exclude-members": "__dict__, __weakref__",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
