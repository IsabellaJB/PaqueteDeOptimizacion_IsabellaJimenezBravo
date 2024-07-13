import os
import sys

# Añade el directorio del paquete al path
sys.path.insert(0, os.path.abspath('../../'))
sys.path.append(os.path.abspath('../../paqueteoptimizacion_isabella'))

# -- Project information -----------------------------------------------------
project = 'Proyecto de optimización'
copyright = '2024, Isabella Jimenez Bravo'
author = 'Isabella Jimenez Bravo'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'es'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Configuración para Read the Docs
if os.environ.get('READTHEDOCS'):
    html_output_path = os.path.join(os.environ['READTHEDOCS_OUTPUT'], 'html')
else:
    html_output_path = os.path.abspath('_build/html')

html_output_path = os.path.join(os.environ.get('READTHEDOCS_OUTPUT', ''), 'html')

