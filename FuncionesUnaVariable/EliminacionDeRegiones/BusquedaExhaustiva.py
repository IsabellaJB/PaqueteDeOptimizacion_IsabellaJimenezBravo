import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def metodo_fase(punto_inicial, delta, funcion):
    # punto_inicial = 0.6
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
        if delta < 0:
            delta = delta
        else:
            delta = -1 * delta
    bandera = 0

    while (bandera != 1):
        x_anterior = x2
        f_anterior = funcion(x_anterior)
        x_nueva = x_anterior + ((2**k) * delta)
        f_nueva = funcion(x_nueva)
        k += 1
        if (f_nueva < f_anterior):
            x2 = x_nueva
        else:
            bandera = 1
    return x_anterior, x_nueva


