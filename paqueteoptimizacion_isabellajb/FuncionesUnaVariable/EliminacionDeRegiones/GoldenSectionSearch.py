import math

def regla_eliminacion(x1, x2, fx1, fx2, a, b):
    if fx1 > fx2:
        return x1, b
    if fx1 < fx2:
        return a, x2
    return x1, x2

def w_to_x(w, a, b):
    return w * (b - a) + a

def busqueda_dorada(funcion, epsilon, a, b):
    """
    Implementación del método de búsqueda por la razón áurea (Golden Section Search) para minimización de funciones.

    Parameters:
    funcion (callable): Función objetivo que se desea minimizar.
    epsilon (float): Precisión deseada para la aproximación del mínimo.
    a (float): Límite inferior del intervalo de búsqueda.
    b (float): Límite superior del intervalo de búsqueda.

    Returns:
    float: Punto donde se estima que se encuentra el mínimo de la función.
    """
    PHI = (1 + math.sqrt(5)) / 2 - 1
    aw, bw = 0, 1
    Lw = 1
    k = 1
    while Lw > epsilon:
        w2 = aw + PHI * Lw
        w1 = bw - PHI * Lw
        aw, bw = regla_eliminacion(w1, w2, funcion(w_to_x(w1, a, b)), funcion(w_to_x(w2, a, b)), aw, bw)
        k += 1
        Lw = bw - aw
    return (w_to_x(aw, a, b) + w_to_x(bw, a, b)) / 2
