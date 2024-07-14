
import os
import sys
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath("../../paqueteoptimizacion_isabella/"))



project = 'Paquete de Optimizacion'
copyright = '2024, Isabella Jimenez Bravo'
author = 'Isabella Jimenez Bravo'
release = '1.0.0'


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
]



source_suffix = ".rst"


master_doc = "index"


exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'


html_theme = 'sphinx_rtd_theme'

