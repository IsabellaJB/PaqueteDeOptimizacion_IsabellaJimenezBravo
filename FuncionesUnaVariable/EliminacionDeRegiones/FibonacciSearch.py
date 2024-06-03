import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def minimo(a, b):
    if a < b:
        return a
    else:
        return b



def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b



def fibonacciSearch(x, funcion):
    a = x[0]
    b = x[-1]

    L = b - a

    n = 7
    k = 2

    bandera = 0

    # paso 2
    while (bandera != 1):
        i = n - k + 2
        Fi = fibonacci(i)
        j = n + 2
        Fj = fibonacci(j)
        L_K = (Fi/Fj) * L
        x1 = a + L_K
        x2 = b - L_K
        funcionX1 = funcion(x1)
        funcionX2 = funcion(x2)
        if funcionX1 > funcionX2:
            a = x1
        elif funcionX1 < funcionX2:
            b = x2
        elif funcionX1 == funcionX2:
            a = x1
            b = x2
        if k == n:
            bandera = 1
        else:
            k += 1

    return a,b

