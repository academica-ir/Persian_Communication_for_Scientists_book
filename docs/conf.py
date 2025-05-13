import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'ارتباط علمی برای پژوهشگران'
author = 'ترجمه و گردآوری'
release = '1.0'

extensions = ['myst_parser']
templates_path = ['_templates']
exclude_patterns = []

language = 'fa'
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    "navigation_with_keys": True,
    "show_nav_level": 2,
}

html_css_files = [
    'rtl.css',
]
