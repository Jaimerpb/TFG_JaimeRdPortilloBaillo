import numpy as np 
import matplotlib.pyplot as plt 
from RK import rk4 


class HarmonicOscillator:
    """
    Modelo del Oscilador aarmónico simple para pasarselo al rk4 e integrar.
    Ecuación de movto.: 𝑥′′+𝑘𝑥=0, con 𝑘=cte.
    
    """

    def __init__(self, k):
        self.k = k

    def __call__(self, y):
        x ,v = y
        Vprima = -self.k *x

        return np.array({v, Vprima})
    

#Para´metros del sistema
kcte = 1        
ds = 0.001
s_end = 20
s_vector = np.arange(0, s_end +ds, ds)

# Se fijan las siguientes condiciones inciales
x0 = 1
v0= 0
y0 = np.array([x0,v0])





modeloOA = HarmonicOscillator(k= kcte)

