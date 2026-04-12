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

def solvehills(y0,k_vector,ds,s_end):
    N = len(k_vector)
    y = np.zeros((2,N))

    y[:,0] = y0 #Metemos las c.i (estado ini, pos y vel/ang iniciales) en la primera columna de la matriz de estados[la primerra columna de la matriz de estados corresponde al estado inicial (y(s=0))]
    for i in range(N-1):
        #Extraemos el es tado act. 'i',columna i de la matriz de stados
        xi = y[0,i]
        vi = y[1,i]

        k_i = k_vector[i]
        k_im1 = k_vector[i+1]

        #cÁLCULO DEL PTO MEDIO (INTERPOLANDO)
        k_medio = (k_i + k_im1) / 2

        #PENDIENTES
        #K1
        k1_x = vi
        k1_v = -k_i* xi

        #K2
        #H acemos una primera estimaci´pn del pto medio
        x_mid1 = xi + 0.5*ds*k1_x
        v_mid1 = vi + 0.5*ds*k1_v
        # se calcula k2
        k2_x = v_mid1
        k2_v  = -k_medio*x_mid1

        #k3 
        # estimamos pto emdio, esta vez con K2
        x_mid2 = xi + 0.5*ds*k2_x
        v_mid2 = vi + 0.5*ds* k2_v
        k3_x = v_mid2
        k3_v= -k_medio* x_mid2

        # K4 
        x_end = xi + ds*k3_x
        v_end = vi + ds*k3_v
        k4_x = v_end
        k4_v = -k_im1 *x_end
        
        #Avance del estado con cuadratura RK4
        y[0,i+1] = xi + (ds/6)* (k1_x+ 2*k2_x + 2*k3_x + k4_x)
        y[1,i+1] = vi + (ds/6)* (k1_v +2*k2_v +2*k3_v + k4_v)
    
    return y