import math
import numpy as np


def lata(x):
    operacion = ((2 * np.pi) * (x**2) + 500/x)
    return operacion


def caja(x):
    return -1*(((20 - (2 * x)) * (10 - (2 * x))) * (x))


def funcion1(x):
    return (x**2) + (54/x)


def funcion2(x):
    return (x**3) + (2*x) - 3


def funcion3(x):
    return (x**4) + (x**2) - 33


def funcion4(x):
    return (3*(x**4)) - (8*(x**3)) - (6*(x**2)) + (12*x)

