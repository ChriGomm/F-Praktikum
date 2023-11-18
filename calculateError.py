
import sympy as sy
import numpy as np

def square(x):
    return x**2


def error(func,values,errors,quantities,method):
    deriv = []
    if (method=='Gauss'):
        errorweight = square
    else:
        errorweight = np.abs
    error =0
    for quantIndex in range(len(quantities)):
        deriv.append(sy.diff(func,quantities[quantIndex]))
        for i in range(len(values)):
            deriv[quantIndex] = deriv[quantIndex].subs(quantities[i],values[i])
        error += errorweight(sy.N(deriv[quantIndex])*errors[quantIndex])
    return error
        
        
        
            
