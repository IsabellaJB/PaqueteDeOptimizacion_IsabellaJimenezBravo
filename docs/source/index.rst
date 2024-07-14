.. Paquete de Optimizacion documentation master file, created by
   sphinx-quickstart on Sat Jul 13 14:05:46 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenidos a mi Paquete de Optimizacion - Isabella Jimenez Bravo!
===================================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   pages/modules
   pages/paqueteoptimizacion_isabella.FuncionesMultivariables
   pages/paqueteoptimizacion_isabella.FuncionesPrueba
   pages/paqueteoptimizacion_isabella.FuncionesUnaVariable

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Introducción
=======================================================================

Bienvenidos a la documentación oficial del paquete **paqueteoptimizacion_isabella**. Este paquete ha sido desarrollado para proporcionar una colección de funciones de optimización tanto para problemas de una variable como de múltiples variables.



Estructura del Paquete
=======================================================================

Este paquete está organizado en tres módulos principales:

1. **FuncionesMultivariables**: Contiene métodos de optimización para problemas de múltiples variables.
   
   - **Directos**: Métodos que no requieren derivadas.
   - **Gradiente**: Métodos que utilizan gradientes para encontrar óptimos.

2. **FuncionesUnaVariable**: Contiene métodos de optimización para problemas de una sola variable.

   - **Basados en la Derivada**: Métodos que utilizan derivadas de la función objetivo.
   - **Eliminación de Regiones**: Métodos que reducen el espacio de búsqueda iterativamente.

3. **FuncionesPrueba**: Contiene funciones para probarlas con los metodos anteriores.


Instalación
=======================================================================
Para instalar el paquete, puedes usar el siguiente comando:

``pip install paqueteoptimizacion-isabella==0.0.1``

Link de donde obtener más información del paquete: 
https://pypi.org/project/paqueteoptimizacion-isabella/0.0.1/



Ejemplo de uso
=======================================================================

.. code-block:: python

   import numpy as np
   from paqueteoptimizacion_isabella.FuncionesMultivariables.Gradiente.Newton import newton
   from paqueteoptimizacion_isabella.FuncionesUnaVariable.EliminacionDeRegiones.GoldenSectionSearch import busqueda_dorada
   from paqueteoptimizacion_isabella.FuncionesUnaVariable.EliminacionDeRegiones.FibonacciSearch import fibonacci_search
   from paqueteoptimizacion_isabella.FuncionesUnaVariable.EliminacionDeRegiones.IntervalHalving import interval_method
   from paqueteoptimizacion_isabella.FuncionesPrueba.Multivariables.multi import himmelblaus

   x0 = np.array([2, 1])

   solucion_1 = newton(himmelblaus,x0,busqueda_dorada)
   print(f"Resultado G: {solucion_1}")

   solucion_2 = newton(himmelblaus,x0,fibonacci_search)
   print(f"Resultado F: {solucion_2}")

   solucion_3 = newton(himmelblaus,x0,interval_method)
   print(f"Resultado I: {solucion_3}")
