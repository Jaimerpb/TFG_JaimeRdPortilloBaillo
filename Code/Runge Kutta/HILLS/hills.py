import numpy as np 

# 1) ONLY QUADS X''+KsX = 0

class onlyquads:
    def __init__(self,kquad_func):
        self.kquad_func = kquad_func
    
    # esto es la f(s,y) que pasamos al Rk para el ca'lculo de las pendientes
    def __call__(self, s, y):
        x, v = y
        
        #la x''
        Vprima = -self.kquad_func(s) * x
        return np.array([v, Vprima])
    

        
    

# # 2) QUADS + BGNDING MAGNET: X''+ (1/ps^2 + Ks)x= 0

# class quads_bending:
    
#     def __init__(self, kquad_func,rho_func):
#         self.kquad_func = kquad_func
#         self.rho_func = rho_func
    

#     def __call__(self, s, y):
#         x,v = y

#         kdip = 1 / (self.rho_func(s) **2)
#         Vprima = -(rhoinv + self.kquad_func) *x
        
#         return np.array([v, Vprima]) 

# 3) QUADS + BENDING MAGNET + OFF MOMETNUM (no homogneo)
class hills_off():
    def __init__(self,kquad_func , rho_func, delta):
        
        self.k_func = kquad_func 
        self.rho_func = rho_func
        
        self.delta= delta 
    
    def __call__(self, s, y):
        x,v = y 

        kdip = 1 / (self.rho_func(s) **2)
        inhomterm = self.delta / self.rho_func(s)

        Vprima= -(k_dip + self.kquad_func) *x + inhomterm
        return np.array( [v, Vprima])

## EXTENSIONES NO LINEALES 
#4 ) QUADS + OFF MOMENTUM + SEXTUPOLES (Hogeneous)

class sext_off():
    def __init__(self, kquad_func, rho_func, delta, ksext_func):
        self.kquad_func = kquad_func 
        self.rho_func = rho_func 
        self.delta = delta 
        self.ksext_func = ksext_func 

    def __call__(self, s, y):
      x,v =  y 
    


      Vprima = -(kquad_func * (1-delta))* x - 1/2*(ksext_func * (1 - delta))*x**2

      return np.array([v, Vprima])
    
# 5) QUADS + BEND + OFF MOMMENTUM + SEXTUPOLES 

class




        





