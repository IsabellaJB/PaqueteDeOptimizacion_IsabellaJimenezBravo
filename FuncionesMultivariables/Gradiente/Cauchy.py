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




