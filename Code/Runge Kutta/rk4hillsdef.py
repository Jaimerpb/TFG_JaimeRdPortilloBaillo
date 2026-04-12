import numpy as np 
import matplotlib.pyplot as plt

#Condiciones inicales 
x0 = 1 # pos inicial
dxds = 0 # ángulo/vel inicial 
y0 = np.array([x0,dxds]) # estado inicial del sistema 

ds = 1 # milímetros 
s_end = 1000 # milímetrss 
s_vector = np.linspace(0,s_end, 1001)

# Para distintas func k(s=) creamos los vectores evaluados en s (?s_Vector')
kvector1 = s_vector # Es el caso k(s) = s
kvector2 = np.cos(s_vector) # Es j(S)= cos(s)
kvector3 = np.sqrt(3)* np.cos(np.sqrt(2)* s_vector) #k(s)= r(3)*cos(r(2)*s)

# Resolviendo hills con rk4

def solvehills(y0, k_vector, ds,s_end):

    return y 
