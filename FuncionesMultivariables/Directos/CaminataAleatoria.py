import random
import numpy as np



def generar_vecino(x):
    return [xi + random.uniform(-1, 1) for xi in x]

def random_walk(funcion_objetivo, x0, max_iter=1000):
    x_best = x0
    f_best = funcion_objetivo(x_best)
    
    for _ in range(max_iter):
        x_k_plus_1 = generar_vecino(x_best)
        f_k_plus_1 = funcion_objetivo(x_k_plus_1)
        
        if f_k_plus_1 < f_best:
            x_best = x_k_plus_1
            f_best = f_k_plus_1
    
    return x_best



