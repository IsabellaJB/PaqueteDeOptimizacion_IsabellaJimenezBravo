<!-- # Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content. -->

# Paquete de Optimización

Bienvenido a la documentación del paquete de optimización `paqueteoptimizacion_isabella`! Este paquete proporciona una colección de funciones de optimización para resolver problemas tanto de una variable como de múltiples variables.

## Contenidos

- [Introducción](#introducción)
- [Estructura del Paquete](#estructura-del-paquete)
- [Instalación](#instalación)
- [Ejemplo de Uso](#ejemplo-de-uso)

## Introducción

Este paquete ha sido desarrollado para ofrecer métodos de optimización efectivos y eficientes para una amplia gama de problemas. Incluye algoritmos que no requieren derivadas, así como métodos que utilizan gradientes y derivadas para encontrar óptimos en funciones tanto univariables como multivariables.

## Estructura del Paquete

El paquete está organizado en dos módulos principales:

1. **FuncionesMultivariables**: Contiene métodos de optimización para problemas de múltiples variables.
   - **Directos**: Métodos que no requieren derivadas.
   - **Gradiente**: Métodos que utilizan gradientes para encontrar óptimos.

2. **FuncionesUnaVariable**: Contiene métodos de optimización para problemas de una sola variable.
   - **Basados en la Derivada**: Métodos que utilizan derivadas de la función objetivo.
   - **Eliminación de Regiones**: Métodos que reducen el espacio de búsqueda iterativamente.

## Instalación

Puedes instalar el paquete utilizando pip:

```pip install paqueteoptimizacion-isabella==0.0.1```


Para más detalles, visita el [paqueteoptimizacion-isabella en PyPI](https://pypi.org/project/paqueteoptimizacion-isabella/0.0.1/).

## Ejemplo de Uso

Aquí tienes un ejemplo básico de cómo usar el paquete:

```python
import numpy as np
from paqueteoptimizacion_isabella.FuncionesMultivariables.Gradiente.Newton import newton
from paqueteoptimizacion_isabella.FuncionesUnaVariable.EliminacionDeRegiones.GoldenSectionSearch import busqueda_dorada
from paqueteoptimizacion_isabella.FuncionesPrueba.Multivariables.multi import himmelblaus

x0 = np.array([2, 1])
solucion_golden = newton(himmelblaus, x0, busqueda_dorada)
print(f"Resultado Golden: {solucion_golden}")
