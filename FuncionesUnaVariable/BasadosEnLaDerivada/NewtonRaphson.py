import numpy as np

def primera_derivada(x, funcion):
    delta = 0.0001
    primera_parte = funcion(x + delta)
    segunda_parte = funcion(x - delta)
    parte_arriba = primera_parte - segunda_parte
    parte_abajo = 2 * delta
    parte_final = parte_arriba / parte_abajo
    return parte_final

def segunda_derivada(x, funcion):
    delta = 0.0001
    primera_parte = funcion(x + delta)
    segunda_parte = 2 * funcion(x)
    tercera_parte = funcion(x - delta)
    parte_arriba = primera_parte - segunda_parte + tercera_parte
    parte_abajo = delta**2
    parte_final = parte_arriba / parte_abajo
    return parte_final

def newton_raphson(x, funcion, epsilon):
    """
    Implementa el método de Newton-Raphson para encontrar una raíz de la función dada.
    El método de Newton-Raphson es un algoritmo iterativo utilizado para encontrar 
    numéricamente las raíces de una función mediante la aproximación sucesiva de 
    un punto inicial hacia la raíz, basándose en la derivada de la función. 

    Parameters:
    x (float): Punto inicial de búsqueda.
    funcion (callable): Función objetivo para la cual se busca la raíz.
    epsilon (float): Tolerancia de convergencia del método.

    Returns:
    float: Valor aproximado de la raíz de la función.
    """

    k = 0
    x_actual = x[k]
    x_derivada1 = primera_derivada(x_actual, funcion)
    x_derivada2 = segunda_derivada(x_actual, funcion)
    x_siguiente = x_actual - (x_derivada1 / x_derivada2)
    while abs(x_siguiente - x_actual) > epsilon:
        k += 1
        if k >= len(x):
            return x_siguiente
        x_actual = x[k]
        x_derivada1 = primera_derivada(x_actual, funcion)
        x_derivada2 = segunda_derivada(x_actual, funcion)
        x_siguiente = x_actual - (x_derivada1 / x_derivada2)
    return x_siguiente
