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
