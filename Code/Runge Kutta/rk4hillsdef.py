import numpy as np 
import matplotlib.pyplot as plt

#Condiciones inicales 
x0 = 1 # pos inicial
dxds = 0 # ángulo/vel inicial 
y0 = np.array([x0,dxds]) # estado inicial del sistema 

ds = 1 # milímetros 
s_end = 1000 # milímetrss 
s_vector = np.linspace(0,s_end, 1001)

#