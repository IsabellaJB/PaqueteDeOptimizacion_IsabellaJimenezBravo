import numpy as np

def primera_derivada(x, funcion):
    delta = 0.0001
    primera_parte = funcion(x + delta)
    segunda_parte = funcion(x - delta)
    parte_arriba = primera_parte - segunda_parte
    parte_abajo = 2 * delta
    parte_final = parte_arriba / parte_abajo
    return parte_final

def segunda_derivada(x, funcion):
    delta = 0.0001
    primera_parte = funcion(x + delta)
    segunda_parte = 2 * funcion(x)
    tercera_parte = funcion(x - delta)
    parte_arriba = primera_parte - segunda_parte + tercera_parte
    parte_abajo = delta**2
    parte_final = parte_arriba / parte_abajo
    return parte_final



def z(x1, x2, funcion):
    parte_arriba = primera_derivada(x2,funcion)

    primera_parte = (primera_derivada(x2,funcion)) - (primera_derivada(x1,funcion))
    segunda_parte = x2 - x1
    parte_abajo = primera_parte/segunda_parte
    
    parte_final = parte_arriba / parte_abajo
    resul = x2 - parte_final
    return resul






def metodo_secante(x_inicial, funcion, epsilon, iter_max=100):
    """
    Encuentra una raíz de una función no lineal usando el método de la secante.
    El método de la secante es un algoritmo numérico iterativo para encontrar 
    las raíces de una función no lineal. A diferencia del método de Newton-Raphson, 
    no requiere la evaluación de la derivada de la función en cada paso, haciendo 
    el cálculo de la derivada menos crítico. 

    Parameters:
    x_inicial (tuple): Tupla con los dos puntos iniciales para comenzar el método.
    funcion (callable): Función objetivo.
    epsilon (float): Tolerancia para la convergencia del método.
    iter_max (int, optional): Número máximo de iteraciones permitidas. Default es 100.

    Returns:
    float: Aproximación de la raíz encontrada.
    """

    x1 = x_inicial[0]
    x2 = x_inicial[1]
    
    iteracion = 0
    while abs(x1 - x2) > epsilon and iteracion < iter_max:
        x_nuevo = z(x1, x2, funcion)
        x1 = x2
        x2 = x_nuevo
        iteracion += 1
    
    if iteracion == iter_max:
        print("El método de la secante no convergió después de", iter_max, "iteraciones.")
    
    return x2

