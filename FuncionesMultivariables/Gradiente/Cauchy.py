import numpy as np
import math



# ---------------------------------- GRADIENTE ---------------------------------- 
def gradiente(funcion, x, delta=0.001):
    derivadas = []
    for i in range(len(x)):
        copia = x.copy()
        copia[i] = x[i] + delta
        valor1 = funcion(copia)
        copia[i] = x[i] - delta
        valor2 = funcion(copia)
        derivada = (valor1 - valor2) / (2 * delta)
        derivadas.append(derivada)
    return np.array(derivadas)

# ----------------------------------- DISTANCIA ORIGEN ----------------------------------
def distancia_origen(vector):
    return np.linalg.norm(vector)


# --------------------------------------- CAUCHY -------------------------------------
def cauchy(funcion_objetivo, x, metodo_busqueda, epsilon1=1e-6, epsilon2=1e-6, max_iterations=100):
    """
    Implementa el método de Cauchy para la optimización de funciones con restricciones.
    El Método de Cauchy, también conocido como el método del gradiente descendente, 
    es una técnica de optimización iterativa utilizada para encontrar el mínimo de una función.

    Parameters:
    funcion_objetivo (callable): La función objetivo a minimizar.
    x (ndarray): Punto inicial de búsqueda.
    metodo_busqueda (callable): Método de búsqueda para calcular el paso alpha.
    epsilon1 (float): Tolerancia para la condición de convergencia basada en la distancia del gradiente al origen. Default es 1e-6.
    epsilon2 (float): Tolerancia para la condición de convergencia basada en la diferencia relativa entre iteraciones. Default es 1e-6.
    max_iterations (int): Número máximo de iteraciones permitidas. Default es 100.

    Returns:
    ndarray: Punto óptimo encontrado.
    """

    terminar = False
    xk = x
    k = 0
    while not terminar:
        gradienteX = np.array(gradiente(funcion_objetivo,xk))
        distancia = distancia_origen(gradienteX)
        if distancia <= epsilon1:
            terminar = True
        elif (k >= max_iterations):
            terminar = True
        else:
            def alpha_calcular(alpha):
                return funcion_objetivo(xk - alpha*gradienteX)
            alpha = metodo_busqueda(alpha_calcular,epsilon2, 0.0,1.0)
            x_k1 = xk - alpha * gradienteX
            if (distancia_origen(x_k1-xk)/distancia_origen(xk)+0.00001) <= epsilon2:
                terminar = True
            else:
                k = k + 1
                xk = x_k1
    return xk




