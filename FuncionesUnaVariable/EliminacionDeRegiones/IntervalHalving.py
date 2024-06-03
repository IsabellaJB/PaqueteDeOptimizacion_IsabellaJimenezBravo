import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def intervalMethod(x,error,funcion):
    a = x[0]
    b = x[-1]
    Xm = (a+b) / 2
    L = b - a
    bandera = 0
    while (bandera != 1):
        x1 = a + (L/4)
        x2 = b - (L/4)
        funcionX1 = funcion(x1)
        funcionX2 = funcion(x2)
        funcionXm = funcion(Xm)
        if funcionX1 < funcionXm:
            b = Xm
            Xm = x1
        else:
            if funcionX2 < funcionXm:
                a = Xm
                Xm = x2
            else:
                a = x1
                b = x2 
        L = b - a
        if abs(L) < error:
            # print(Xm)
            bandera = 1
        # else:
        #     print(x1)
        #     print(x2)
        #     print("\n"*3)
    return x1,x2


