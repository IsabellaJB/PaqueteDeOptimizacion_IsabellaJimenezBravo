import numpy as np

def booth_function(arreglo):
    x = arreglo[0] 
    y = arreglo[1]
    return ((x + 2*y - 7)**2) + ((2*x + y - 5)**2)



def prueba(x):
    return np.sum(np.square(x))

def Himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def Rastrigin(x):
    n = len(x)
    return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))  

def Rosenbrock(x):
    return sum(100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x) - 1))
