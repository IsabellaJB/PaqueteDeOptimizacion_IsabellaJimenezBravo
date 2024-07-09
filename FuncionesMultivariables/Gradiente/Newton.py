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

# ---------------------------------- HESSIANA ---------------------------------- 
def hessiana(funcion, x, delta=0.001):
    n = len(x)
    matriz = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                copia1 = x.copy()
                copia1[i] += delta
                f1 = funcion(copia1)
                
                copia2 = x.copy()
                copia2[i] -= delta
                f2 = funcion(copia2)
                
                matriz[i, i] = (f1 - 2 * funcion(x) + f2) / (delta**2)
            elif i < j:
                copia3 = x.copy()
                copia3[i] += delta
                copia3[j] += delta
                f3 = funcion(copia3)
                
                copia4 = x.copy()
                copia4[i] += delta
                copia4[j] -= delta
                f4 = funcion(copia4)
                
                copia5 = x.copy()
                copia5[i] -= delta
                copia5[j] += delta
                f5 = funcion(copia5)
                
                copia6 = x.copy()
                copia6[i] -= delta
                copia6[j] -= delta
                f6 = funcion(copia6)
                
                matriz[i, j] = (f3 - f4 - f5 + f6) / (4 * delta * delta)
                matriz[j, i] = matriz[i, j]
    return matriz


# ---------------------------------- DISTANCIA ORIGEN ---------------------------------- 
def distancia_origen(vector):
    return np.linalg.norm(vector)

# ---------------------------------- MÉTODO DE NEWTON MODIFICADO ---------------------------------- 
def newton(funcion_objetivo, x0, metodo_busqueda, epsilon1=1e-6, epsilon2=1e-6, max_iterations=100):
    """
    Implementa el método de Newton modificado para la optimización de funciones.
    El Método de Newton es un algoritmo de optimización que busca encontrar 
    raíces de funciones o mínimos de funciones derivadas.

    Parameters:
    funcion_objetivo (callable): Función objetivo a minimizar.
    x0 (list): Punto inicial de búsqueda.
    metodo_busqueda (callable): Método de búsqueda para calcular el paso alpha.
    epsilon1 (float): Tolerancia para la norma del gradiente. Default es 1e-6.
    epsilon2 (float): Tolerancia para la diferencia relativa entre iteraciones sucesivas. Default es 1e-6.
    max_iterations (int): Número máximo de iteraciones permitidas. Default es 100.

    Returns:
    ndarray: Punto óptimo encontrado.
    """

    terminar = False
    xk = np.array(x0, dtype=float)
    k = 0
    while not terminar:
        # GRADIENTE
        gradienteX = gradiente(funcion_objetivo, xk)
        
        if np.linalg.norm(gradienteX) < epsilon1 or k >= max_iterations:
            terminar = True
        else:
            # HESSIANA
            hessian = hessiana(funcion_objetivo, xk)
            try:
                inversa = np.linalg.inv(hessian)
            except np.linalg.LinAlgError:
                print("La matriz Hessiana no es invertible.")
                return None
            
            # PRODUCTO PUNTO
            punto = np.dot(inversa, gradienteX)
            

            def alpha_calcular(alpha):
                return funcion_objetivo(xk - alpha * punto)
            
            alpha = metodo_busqueda(alpha_calcular, epsilon2, 0.0, 1.0)
            
            x_k1 = xk - alpha * punto

            if (distancia_origen(x_k1 - xk) / (distancia_origen(xk) + 0.00001)) <= epsilon2:
                terminar = True
            else:
                k += 1
                xk = x_k1
        
        # print(f"Iteración {k+1}: x = {xk}, f(x) = {funcion_objetivo(xk)}")

    if k < max_iterations:
        # print('\n')
        print(f"Convergencia alcanzada en {k+1} iteraciones")
    else:
        print("El método no convergió")
    
    return xk





