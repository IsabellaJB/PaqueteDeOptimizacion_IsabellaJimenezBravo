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

def metodo_biseccion(x, funcion, epsilon):
    a_original = x[0]
    b_original = x[-1]

    puntos_prueba = np.arange(a_original, b_original, 0.1)
    
    a = next(p for p in puntos_prueba if primera_derivada(p, funcion) <= 0)
    b = next(p for p in puntos_prueba if segunda_derivada(p, funcion) >= 0)
    
    x1 = a
    x2 = b
    
    
    z = (x2 + x1) / 2
    while abs(x1 - x2) > epsilon:
        z = (x2 + x1) / 2
        if primera_derivada(z, funcion) < 0:
            x1 = z
        elif primera_derivada(z, funcion) > 0:
            x2 = z
    
    return z




