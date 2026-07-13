# coding: utf-8
def integral(f, a, b):
    import numpy as np
    
    n = 100000
    x = np.linspace(a, b, n)
    y = f(x)
    result = np.trapz(y, x)
    
    return result
