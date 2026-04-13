import numpy as np 

# 1) ONLY QUADS X''+KsX = 0

class onlyquads:
    def __init__(self,k_func):
        self.k_func = k_func
    
    # esto es la f(s,y) que pasamos al Rk para el ca'lculo de las pendientes
    def __call__(self, s, y):
        x, v = y
        
        #la x''
        Vprima = -self.k_func(s) * x
        return np.array([v, Vprima])
    

        
    

# # 2) QUADS + BGNDING MAGNET: X''+ (1/ps^2 + Ks)x= 0

# class quads_bending:
    
#     def __init__(self, k_func,rho_func):
#         self.k_func = k_func
#         self.rho_func = rho_func
    

#     def __call__(self, s, y):
#         x,v = y

#         rhoinv = 1 / (self.rho_func(s) **2)
#         Vprima = -(rhoinv + self.k_func) *x
        
#         return np.array([v, Vprima]) 

# 3) QUADS + BENDING MAGNET + OFF MOMETNUM (no homogneo)
class hills_off():
    def __init__(self,k_func , rho_func, delta):
        
        self.k_func = k_func 
        self.rho_func = rho_func
        
        self.delta= delta 
    
    def __call__(self, s, y):
        x,v = y 
        





