import numpy as np

def fibonacci_search(funcion, epsilon, a, b):
    """
    Implementación del método de búsqueda utilizando la secuencia de Fibonacci para minimización de funciones.

    Parameters:
    funcion (callable): Función objetivo que se desea minimizar.
    epsilon (float): Precisión deseada para la aproximación del mínimo.
    a (float): Límite inferior del intervalo de búsqueda.
    b (float): Límite superior del intervalo de búsqueda.

    Returns:
    float: Punto donde se estima que se encuentra el mínimo de la función.
    """
    
    fibs = [0, 1]
    while (b - a) / fibs[-1] > epsilon:
        fibs.append(fibs[-1] + fibs[-2])

    n = len(fibs) - 1
    k = n - 1

    x1 = a + fibs[k-1] / fibs[k] * (b - a)
    x2 = a + fibs[k] / fibs[k+1] * (b - a)
    f1 = funcion(x1)
    f2 = funcion(x2)
    
    while k > 1:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + fibs[k-1] / fibs[k] * (b - a)
            f2 = funcion(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + fibs[k-2] / fibs[k-1] * (b - a)
            f1 = funcion(x1)
        k -= 1

    if f1 < f2:
        return x1
    else:
        return x2
    


