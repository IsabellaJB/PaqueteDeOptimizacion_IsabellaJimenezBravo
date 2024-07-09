import random
import numpy as np


def caminata_aleatoria(func, x0, paso, iteraciones=1000):
    """
    Realiza una búsqueda de optimización usando el método de Caminata Aleatoria.
    La caminata aleatoria es un proceso donde el punto se mueve paso a paso en direcciones 
    aleatorias dentro de un espacio, un plano o un espacio de mayor dimensión. Cada paso en 
    este proceso es independiente de los anteriores.
    
    Parameters:
    func (callable): La función objetivo a minimizar.
    x0 (ndarray): El punto inicial de la búsqueda.
    iteraciones (int): El número de iteraciones de la búsqueda. Default es 1000.
    paso (float): El tamaño del paso en cada iteración. Recomendacion de 0.1.
    
    Returns:
    ndarray: El punto óptimo encontrado.
    """
    x = x0
    for i in range(iteraciones):
        x_nuevo = x + np.random.uniform(-paso, paso, size=x.shape)
        if func(x_nuevo) < func(x):
            x = x_nuevo
    return x


# def generar_vecino(x):
#     return [xi + random.uniform(-1, 1) for xi in x]

# def random_walk(funcion_objetivo, x0, max_iter=1000):
#     x_best = x0
#     f_best = funcion_objetivo(x_best)
    
#     for _ in range(max_iter):
#         x_k_plus_1 = generar_vecino(x_best)
#         f_k_plus_1 = funcion_objetivo(x_k_plus_1)
        
#         if f_k_plus_1 < f_best:
#             x_best = x_k_plus_1
#             f_best = f_k_plus_1
    
#     return x_best



