# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# docs/source/conf.py

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# docs/source/conf.py

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output



import os
import sys

import os
import sys
sys.path.insert(0, os.path.abspath('../paqueteoptimizacion_isabellajb/FuncionesMultivariables'))
sys.path.insert(0, os.path.abspath('../paqueteoptimizacion_isabellajb/FuncionesUnaVariable'))

# sys.path.insert(0, os.path.abspath('../../'))
# sys.path.insert(0, os.path.abspath('../paqueteoptimizacion_isabellajb/FuncionesMultivariables'))
# # O:\SextoSemestre\PaqueteDeOptimizacion_IsabellaJimenezBravo\paqueteoptimizacion_isabellajb\FuncionesMultivariables
# sys.path.insert(0, os.path.abspath('../paqueteoptimizacion_isabellajb/FuncionesUnaVariable'))
# sys.path.insert(0, os.path.abspath('../../FuncionesMultivariables/Directos'))
# sys.path.insert(0, os.path.abspath('../../FuncionesMultivariables/Gradiente'))
# sys.path.insert(0, os.path.abspath('../../FuncionesUnaVariable/BasadosEnLaDerivada'))
# sys.path.insert(0, os.path.abspath('../../FuncionesUnaVariable/EliminacionDeRegiones'))



project = 'Paquete de Optimización Isabella Jiménez Bravo'
author = 'Isabella Jiménez Bravo'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

html_theme = 'nature'
html_static_path = ['_static']



# project = 'PaqueteDeOptimizacion_IsabellaJimenezBravo'
# copyright = '2024, Isabella Jimenez Bravo'
# author = 'Isabella Jimenez Bravo'
# release = '08/07/2024'

# extensions = [
#     'sphinx.ext.autodoc',
#     'sphinx.ext.napoleon',
#     'sphinx.ext.viewcode'
    
# ]

# templates_path = ['_templates']
# exclude_patterns = []

# language = 'es'

# html_theme = 'nature'
# html_static_path = ['_static']


