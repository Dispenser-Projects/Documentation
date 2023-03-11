
project = 'Dispenser Projects'
copyright = '2023, Gunivers'
author = 'theogiraudet & theaustudio'

import os
import pydata_sphinx_theme

# Project information ---------------------------------------------------------

project = 'Bookshelf'
copyright = '2023, Gunivers'
author = 'Gunivers'
html_favicon = "_static/logo.png"

# -- General configuration ----------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_togglebutton',
    'sphinx_copybutton',
]
myst_heading_anchors = 6
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Options for HTML output -----------------------------------------------------

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "github_url": "https://github.com/Dispenser/",
    "announcement": "⚠️ You are reading a doc of an undergoing development version. Information can be out of date and/or change at any time. ⚠️",
    "logo": {
        "image_dark": "_static/logo.png",
        "text": "Dispenser",  # Uncomment to try text with logo
    },
    "icon_links": [
        {
            "name": "Gunivers",
            "url": "https://gunivers.net",
            "icon": "_static/logo-gunivers.png",
            "type": "local",
        },
        {
            "name": "Discord server",
            "url": "https://discord.gg/E8qq6tN",
            "icon": "_static/logo-discord.png",
            "type": "local",
        },
    ]
}

html_logo = "_static/logo.png"

html_static_path = ['_static']

html_css_files = [
    'css/stylesheet.css',
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    #"linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]