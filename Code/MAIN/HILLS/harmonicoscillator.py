import numpy as np 
import matplotlib.pyplot as plt 
from RK import rk4 
from plotting import save_figure

class HarmonicOscillator:
    """
    Modelo del Oscilador aarmónico simple para pasarselo al rk4 e integrar.
    Ecuación de movto.: 𝑥′′+𝑘𝑥=0, con 𝑘=cte.
    
    """

    def __init__(self, k):
        self.k = k

    def __call__(self, s, y):
        x, v = y
        v_prima = -self.k * x
        return np.array([v, v_prima])
    

#Para´metros del sistema
kcte = 1        
ds = 0.001 #step size 
s_end = 20 # Límite de integración 
s_vector = np.arange(0, s_end +ds, ds)

# Se fijan las siguientes condiciones inciales
x0 = 1  # pos inicial
v0= 0   # ángulo incial
y0 = np.array([x0,v0])





modeloOA = HarmonicOscillator(k= kcte)

y_sol= rk4(modeloOA, y0, s_vector, ds)



plt.figure(figsize=(10, 5))
plt.plot(s_vector, y_sol[0, :], label=' x ', color='blue', linewidth=2)
plt.plot(s_vector, y_sol[1, :], label=' x\' ', color='orange', linestyle='--', linewidth=2)

plt.title('Oscilador Armónico (x\'\' + kx = 0) resuelto con RK4')
plt.xlabel('s')
plt.ylabel('Amplitud')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.5, linestyle='--')
plt.tight_layout()
save_figure("Trayectorias.png")

# Diagrama de fases x'x
plt.figure(figsize=(6, 6))
plt.plot(y_sol[0, :], y_sol[1, :] , color='purple')
plt.title('Plano xx\'')
plt.xlabel(' x ')
plt.ylabel(' x\' ')
plt.grid(True, alpha=0.5, linestyle='--')
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()
save_figure("DiagramafasesOArk4.png")
