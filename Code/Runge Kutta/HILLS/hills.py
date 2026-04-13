import numpy as np 

# 1) ONLY QUADS X''+KsX = 0

class onlyquads:
    def __init__(self,k_func):
        self.k_func = k_func
    
    # esto es la f(s,y)
    def __call__(self, s, y):
        x, v = y
        #la x''
        Vprima = -self.k_func(s) * x
        return np.array([v, Vprima])
    

        
    

# 2) QUADS + BGNDING MAGNET: X''+ (1/ps^2 + Ks)x= 0 
