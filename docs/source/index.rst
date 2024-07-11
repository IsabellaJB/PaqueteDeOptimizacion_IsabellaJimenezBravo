.. PaqueteDeOptimizacion_IsabellaJimenezBravo documentation master file, created by
   sphinx-quickstart on Mon Jul  8 19:40:36 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. PaqueteDeOptimizacion_IsabellaJimenezBravo documentation master file, created by
   sphinx-quickstart on Mon Jul  8 19:40:36 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenidos a la documentación del paquete: PaqueteDeOptimizacion_IsabellaJimenezBravo
======================================================================================


..    :maxdepth: 2
..    :caption: Contenido:

..    FuncionesMultivariables
..    FuncionesUnaVariable
..    module1
..    module2
..    Funciones


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   FuncionesMultivariables
   FuncionesUnaVariable
   FuncionesPrueba
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Introducción
-------

Bienvenidos a la documentación oficial del paquete **PaqueteDeOptimizacion_IsabellaJimenezBravo**. Este paquete ha sido desarrollado para proporcionar una colección de funciones de optimización tanto para problemas de una variable como de múltiples variables.

Estructura del Paquete
-------

Este paquete está organizado en dos módulos principales:

1. **FuncionesMultivariables**: Contiene métodos de optimización para problemas de múltiples variables.
   
   - **Directos**: Métodos que no requieren derivadas.
   - **Gradiente**: Métodos que utilizan gradientes para encontrar óptimos.

2. **FuncionesUnaVariable**: Contiene métodos de optimización para problemas de una sola variable.

   - **Basados en la Derivada**: Métodos que utilizan derivadas de la función objetivo.
   - **Eliminación de Regiones**: Métodos que reducen el espacio de búsqueda iterativamente.


Uso del Paquete
-------

Aquí se presenta un ejemplo básico de cómo utilizar el paquete para resolver un problema de optimización:

```python
from PaqueteDeOptimizacion_IsabellaJimenezBravo.FuncionesUnaVariable.Directos import metodo_directo

resultado = metodo_directo(funcion, intervalo)
print(resultado)




Instalación
-------

Para instalar el paquete, puedes usar el siguiente comando:

``pip install paqueteoptimizacion-isabellajb==0.0.1``

Link de donde obtener más información del paquete: 
https://pypi.org/project/paqueteoptimizacion-isabellajb/0.0.1/


