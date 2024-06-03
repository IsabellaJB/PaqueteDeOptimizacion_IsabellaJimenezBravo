import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def deltas(a,b,n):
    return ((b - a) / n)


def busqueda_exhaustiva(x, funcion, precision):
    a = x[0]
    b = x[-1]
    n = int((2 * (b - a)) / precision)
    delta = ((b - a) / n)
    x1 = a
    x2 = x1 + delta
    x3 = x2 + delta
    fx1 = funcion(x1)
    fx2 = funcion(x2)
    fx3 = funcion(x3)
    while (b>=x3):
        if fx1 >= fx2 and fx2 <= fx3:
            return x1, x3
        else:
            x1 = x2
            x2 = x3
            x3 = x3 + delta
            fx1 = funcion(x1)
            fx2 = funcion(x2)
            fx3 = funcion(x3)
    return x1, x3






