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

#se llama a la función solvehills
y1 = solvehills(y0,kvector1,ds,s_end)
y2 = solvehills(y0,kvector2,ds,s_end)
y3 = solvehills(y0,kvector3/10,ds,s_end)
y4 = solvehills(y0, kvector3*0 + .1 ,ds,s_end)

plt.figure(figsize=(8, 4))
plt.plot(s_vector, y4[0, :], label='Posición (x)')
plt.plot(s_vector, y4[1, :], label='Velocidad (v)')
plt.title("Hills eq usando RK4")
plt.xlabel("Tiempo (t)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(6, 6))
plt.plot(y4[0,:], y4[1, :]) # representamos pos vs vel
plt.title("Diagrama de Fases de Hills")
plt.xlabel("Posición (x)")
plt.ylabel("Velocidad (v)")
plt.grid(True)
plt.show()

# Esstabilidad numérica RK
#Comparando respecto a iteración anterior(Desviación)
h_step_values = [0.5,0.25,0.125,0.0625]
desv = []

h_anterior = 1.0
s_vector_anterior = np.arange(0, s_end + h_anterior, h_anterior)
k_vector_anterior = np.sqrt(3) * np.cos(np.sqrt(2) * s_vector_anterior)
    

y_anterior = solvehills( y0, k_vector_anterior, h_anterior, s_end)

#nos quedamos con todas las columnas de la fila1(la de posiciones)
x_iteracion_anterior = y_anterior[0,:] 


for h in h_step_values:
    s_vector_actual = np.arange(0, s_end + h, h)
    k_vector_actual = np.sqrt(3) * np.cos(np.sqrt(2) * s_vector_actual)

    
    y_actual = solvehills( y0,k_vector_actual,h , s_end)
    x_actual = y_actual[0,:]
    
    #nos quedamos con los nodos pares para poder calcular luego las desviaciones
    # se resulve con esto la resta de vectores de distinto tamaño
    x_actualsamesize= x_actual[:: 2] # Otra opciión es np.,interp(svectoractual, svectoranterior, x_actual )
    


    #Desviación relativa(es la distancia euclidea normalziada)
    
    error_absoluto = np.linalg.norm(x_actualsamesize - x_iteracion_anterior)
    desv_rela= error_absoluto/ np.linalg.norm( x_iteracion_anterior )
    
    desv.append(desv_rela)

    x_iteracion_anterior = x_actual

# wE visualiza el error

plt.figure(figsize=(8,4))
plt.plot(h_step_values, desv, marker='o', color='purple',linewidth = 2)


plt.gca().invert_xaxis() #invierte el ejex para que la gráfica avanze a medida qye h decrec3

plt.xscale('log', base =2 )
plt.yscale('log', base=12 )

plt.title("Convergenicia rk4")
plt.xlabel("tamaño del paso $h$ (mm)")
plt.ylabel('desv relativa')
plt.grid(True, which = "both", ls= "--", alpha =0.5)
plt.show()
