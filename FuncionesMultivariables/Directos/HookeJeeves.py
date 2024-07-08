import numpy as np

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
        x_new[i] -= 2 * deltas[i]
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

    while np.linalg.norm(deltas) > epsilon:
        xk_new = exploratory_move(xk, deltas, objective_function)
        
        if xk_new != xk:
            xk_1 = xk[:]
            xk = xk_new[:]
            xk_p = pattern_move(xk, xk_1)
            xk_new = exploratory_move(xk_p, deltas, objective_function)
            
            if objective_function(xk_new) < objective_function(xk):
                xk = xk_new[:]
        else:
            if max(deltas) < epsilon:
                break
            deltas = [delta / alpha for delta in deltas]
    
    return xk

