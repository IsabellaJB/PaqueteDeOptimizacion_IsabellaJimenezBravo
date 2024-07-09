import numpy as np
import math

# ---------------------------------- FUNCION OBJETIVO ---------------------------------- 
def funcion_objetivo(arreglo):
    x = arreglo[0]
    y = arreglo[1]
    operacion = ((x**2 + y - 11)**2) + ((x + y**2 - 7)**2)
    return operacion

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




# ------------------------------------ GRADIENTE CONJUGADO ------------------------------------ 
def gradiente_conjugado(f_o, x0, metodo_busqueda, e1=1e-6, e2=1e-6, e3=1e-6):
    """
    Implementa el método del Gradiente Conjugado para la optimización de funciones.
    El método del gradiente conjugado utiliza tanto la información del gradiente en 
    la iteración actual como la de iteraciones previas para calcular la dirección de 
    búsqueda siguiente.

    Parameters:
    f_o (callable): La función objetivo a minimizar.
    x0 (ndarray): Punto inicial de búsqueda.
    metodo_busqueda (callable): Método de búsqueda para calcular el paso alpha.
    e1 (float): Tolerancia para la búsqueda de línea. Default es 1e-6.
    e2 (float): Tolerancia para la condición de convergencia basada en la diferencia relativa. Default es 1e-6.
    e3 (float): Tolerancia para la condición de convergencia basada en la norma del gradiente. Default es 1e-6.

    Returns:
    ndarray: Punto óptimo encontrado.
    """

    x = x0
    grad = gradiente(f_o, x)
    s = -grad
    k = 0

    def line_search(f_o, x, s, e1):
        def alpha_funcion(alpha):
            return f_o(x + alpha * s)
        return metodo_busqueda(alpha_funcion, e1, 0.0, 1.0)

    while True:
        alpha = line_search(f_o, x, s, e1)
        x_next = x + alpha * s
        grad_next = gradiente(f_o, x_next)

        if np.linalg.norm(x_next - x) / (np.linalg.norm(x) + 1e-8) <= e2 or np.linalg.norm(grad_next) <= e3:
            break

        beta = np.dot(grad_next, grad_next) / np.dot(grad, grad)
        s = -grad_next + beta * s

        x = x_next
        grad = grad_next
        k += 1

    return x




