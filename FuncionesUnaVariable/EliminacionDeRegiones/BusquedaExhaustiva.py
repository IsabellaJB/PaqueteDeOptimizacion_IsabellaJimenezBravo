import numpy as np


def metodo_fase(punto_inicial, delta, funcion):
    """
    Implementación del método de la fase para minimización de funciones.

    Parameters:
    punto_inicial (float): Punto inicial para iniciar la búsqueda.
    delta (float): Tamaño del paso inicial para la búsqueda.
    funcion (callable): Función objetivo que se desea minimizar.

    Returns:
    float: Punto donde se estima que se encuentra el mínimo de la función.
    """
    k = 0

    x1 = punto_inicial - abs(delta)
    x2 = punto_inicial
    x3 = punto_inicial + abs(delta)

    fx1 = funcion(x1)
    fx2 = funcion(x2)
    fx3 = funcion(x3)


    if fx1 > fx2 > fx3:
        delta = abs(delta)
    else:
        delta = -abs(delta)

    while True:
        x_anterior = x2
        f_anterior = funcion(x_anterior)
        x_nueva = x_anterior + (2**k) * delta
        f_nueva = funcion(x_nueva)
        k += 1
        if f_nueva >= f_anterior:
            break
        x2 = x_nueva

    if funcion(x_anterior) < funcion(x_nueva):
        return x_anterior
    else: 
        return x_nueva



