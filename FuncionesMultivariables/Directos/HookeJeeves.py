import numpy as np

def booth_function(arreglo):
    x = arreglo[0] 
    y = arreglo[1]
    return ((x + 2*y - 7)**2) + ((2*x + y - 5)**2)

def exploratory_move(arreglo_variables, delta):
    copia = arreglo_variables.copy()
    if len(arreglo_variables) == len(delta):
        nuevo_punto = []
        for i in range(0, len(arreglo_variables)):
            normal = arreglo_variables[i]
            suma = arreglo_variables[i] + delta[i]
            resta = arreglo_variables[i] - delta[i]
            copia[i] = normal
            evalua_normal = booth_function(copia)
            copia[i] = suma
            evalua_suma = booth_function(copia)
            copia[i] = resta
            evalua_resta = booth_function(copia)
            minimo = min(evalua_normal, evalua_suma, evalua_resta)
            if minimo == evalua_normal:
                nuevo_punto.append(normal)
            elif minimo == evalua_suma:
                nuevo_punto.append(suma)
            else:
                nuevo_punto.append(resta)
        return nuevo_punto
    else:
        print("No son de la misma dimension")

def pattern_move(k, k_minus_1):
    resul = []
    x = k[0] + (k[0] - k_minus_1[0])
    y = k[1] + (k[1] - k_minus_1[1])
    resul.append(x)
    resul.append(y)
    return resul

def actualizar_delta(delta,alpha):
    lista_deltas = []
    for i in delta:
        nueva_delta = i / 2
        lista_deltas.append(nueva_delta)
    return lista_deltas

def distancia_origen(vector):
    return np.linalg.norm(vector)

def verificar_distancia(vector, e):
    distancia = distancia_origen(vector)
    return distancia < e








def exploratory_move(x, deltas, objective_function):
    n = len(x)
    best_x = x[:]
    best_value = objective_function(x)
    for i in range(n):
        x_new = x[:]
        x_new[i] += deltas[i]
        new_value = objective_function(x_new)
        if new_value < best_value:
            best_x = x_new[:]
            best_value = new_value
        x_new = x[:]
        x_new[i] -= deltas[i]
        new_value = objective_function(x_new)
        if new_value < best_value:
            best_x = x_new[:]
            best_value = new_value
    return best_x

def pattern_move(xk, xk_1):
    return [xk[i] + (xk[i] - xk_1[i]) for i in range(len(xk))]

def hooke_jeeves(x0, deltas, alpha, epsilon, objective_function):
    xk = x0[:]
    xk_1 = x0[:]
    k = 0

    distancia = distancia_origen(deltas)
    
    while (distancia > 0):
        # Paso 2: Movimiento exploratorio
        xk_new = exploratory_move(xk, deltas, objective_function)
        
        if xk_new != xk:
            xk = xk_new[:]
            xk_1 = xk[:]
            k += 1
            
            # Paso 4: Movimiento de patrón
            xk_p = pattern_move(xk, xk_1)
            
            # Paso 5: Otro movimiento exploratorio desde el nuevo punto patrón
            xk_new = exploratory_move(xk_p, deltas, objective_function)
            
            if objective_function(xk_new) < objective_function(xk):
                xk = xk_new[:]
            else:
                # Paso 3: Verificar si los incrementos son menores que epsilon
                if max(deltas) < epsilon:
                    break
                deltas = [delta / alpha for delta in deltas]
        else:
            # Paso 3: Verificar si los incrementos son menores que epsilon
            if max(deltas) < epsilon:
                break
            deltas = [delta / alpha for delta in deltas]
    
    return xk


def objective_function(x):
    # Funcion Sphere
    return np.sum(np.square(x))

    # Funcion Himmelblau
    # return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    # Función Rastrigin
    # n = len(x)
    # return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))  

    # Funcion Rosenbrock
    # return sum(100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x) - 1))




# Funcion Sphere
# x0 = np.array([-1.0, 1.5])

# Funcion Himmelblau
# x0 = np.array([3.0, 2.0])

# Función Rastrigin
# x0 = np.array([-2,-2,-2])

# Funcion Rosenbrock
# x0 = np.array([2,1.5,3,-1.5,-2])



x0 = [5, 5] 
deltas = [0.5,0.5]  
alpha = 2  
epsilon = 1e-6 

# x0 = [-5, -2.5] 
# deltas = [0.5,0.25]  
# alpha = 2  
# epsilon = 0.001

resultado = hooke_jeeves(x0, deltas, alpha, epsilon, booth_function)
print("Resultado final:", resultado)
print("Valor de la función objetivo en el resultado final:", booth_function(resultado))

# resultado = hooke_jeeves(x0, deltas, alpha, epsilon, objective_function)
# print("Resultado final:", resultado)
# print("Valor de la función objetivo en el resultado final:", objective_function(resultado))






