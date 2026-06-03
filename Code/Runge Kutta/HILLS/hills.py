import numpy as np 


## 1) Hills lineal homogénea, de la forma 𝑥′′+𝑘(𝑠)𝑥=0, con 𝑘(𝑠) periódica. 
# ONLY QUADS : 𝑥′′+𝑘_𝑞𝑢𝑎𝑑(𝑠)𝑥=0 


class hills_lineal_hom:
    def __init__(self, k_func):
        self.k_func = k_func
    
    def __call__(self,s, y):
        x, v = y

        vprima = -self.k_func(s)*x 

        return np.array([v, vprima])





# 2) Hills Lineal No homogénea,
#QUADS + BGNDING MAGNETs: 𝑥′′+ [1/(𝜌(𝑠)^2 ) + 𝑘_𝑞𝑢𝑎𝑑(𝑠)]𝑥 = 𝛿/(𝜌(𝑠))

class hills_lineal_nonhom:
    def __init__(self,k_func,inhomfunc):
        self.k_func = k_func
        self.inhomfunc = inhomfunc 
    
    # Esto es la f(s,y)
    def __call__(self, s, y):
        x, v = y
        # La x''
        Vprima = -self.k_func(s)*x + self.inhomfunc(s)
        return np.array([v, Vprima])

        

 





        





