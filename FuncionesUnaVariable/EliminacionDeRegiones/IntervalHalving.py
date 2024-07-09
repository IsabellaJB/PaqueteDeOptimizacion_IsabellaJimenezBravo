import numpy as np


def interval_method(x, error, function):
    a = x[0]
    b = x[-1]
    Xm = (a + b) / 2
    L = b - a
    converged = False
    
    while not converged:
        x1 = a + (L / 4)
        x2 = b - (L / 4)
        func_x1 = function(x1)
        func_x2 = function(x2)
        func_Xm = function(Xm)
        
        if func_x1 < func_Xm:
            b = Xm
            Xm = x1
        else:
            if func_x2 < func_Xm:
                a = Xm
                Xm = x2
            else:
                a = x1
                b = x2
                
        L = b - a
        if abs(L) < error:
            converged = True
    
    return Xm

