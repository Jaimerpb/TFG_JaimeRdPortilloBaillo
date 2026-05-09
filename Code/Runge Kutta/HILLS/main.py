import numpy as np 
import matplotlib.pyplot as plt 

# Del módulo hills importamso las EDOS

from hills import hills_lineal_hom



#Definimos el RK4 q resuleva con la tipo d eEDO q le pasemos

def rk4 (modeloEDO, y0, s_vector, ds):
    # igual q antes solo que ahora de fomra compacta y evaluando con el modelo directmente
    N= len(s_vector)
    y = np.zeros((2 , N))

    y[:, 0 ] = y0 
    
    for i in range(N - 1):
        s_i = s_vector[i]
        estado_act = y[:, i]

        # estructura rk4, evaluando directamente con el modelo f(s,y) q le pasemos
        k1 = modeloEDO (s_i, estado_act)
        k2 = modeloEDO(s_i + 0.5*ds , estado_act + 0.5*ds*k1)
        k3 = modeloEDO(s_i + 0.5*ds, estado_act + 0.5*ds*k2 )
        k4 = modeloEDO (s_i + ds, estado_act + ds*k3)

        # Estado siguiente
        y[:, i+1] = estado_act + (1/6*ds) *(k1 +2*k2 + 2*k3+ k4)

    return y 


# Parámetros

#Cond. iniciales
x0 = 1e-3 # pos incial Xo
dxds_0 = 0 #aangulo inicial X'o
y0 = np.array([x0,dxds_0]) # Estado inicial del sistema, con pos y ángulo iniciales





def periodic_s(li, lf , f, s):
    if s >= li and s <= lf:
        return f(s)

    elif s > lf:
        s_new = s - (lf - li)
        return periodic_s(li, lf, f, s_new)
    elif s < li:
        s_new = s + (lf-li)
        return periodic_s(li, lf, f, s_new)


 



#Slide 19

k_val = 0.05     # Fuerza del gradiente magnético (1/m2)

lq1 = 0.2  # Longitud del cuadrupolo (m) 
l_i = 0  # Pos. entrada (m)
Lc =  1 # Longitud/periodo de la celda (m) 

# Slide 20
 
ld = 1.5 # Longitud del dipolo (m)
rho = 3.81 # Radio de curvatura de las partículas en la sección de los dipolos (m)
Lc2 = 5.8 # Longitud de la celda slide20 (m)

ds = 1e-3 # metros
s_end= 100*Lc2 # metros
s_vector = np.arange(0,s_end+ds, ds)



def kquadb(s):
    if s >= l_i and s <= (lq1/2):
        return k_val
    elif s > (lq1/ 2) and s < (Lc/2 - lq1/2):
        return 0 
    elif s >= (Lc/2 - lq1/2) and s <= (Lc/2 + lq1/2):
        return -k_val
    elif s > (Lc/2 + lq1/2) and s < (Lc - lq1/2):
        return 0 
    elif s >= (Lc - lq1/2) and s <= (Lc):
        return  k_val
    
def kquadp(s):
    return periodic_s(l_i, Lc, kquadb, s)

def kquad(s):
    #eN lugar de recorrer todo s_vector en cada iteración del RK4, evalúa solo el s que toque, y devuelve k evaluada en ese punto. 
        if np.isscalar(s): 
            return kquadp(s)
        return np.array([kquadp(si) for si in s]) #Esto es para luego poder gráficarlo






# Se invocan los 'modelos'
modelo1 = hills_lineal_hom(k_func = kquad)


    
# solucions rk de los modelos
y1 = rk4(modelo1, y0, s_vector, ds)


#Grafica de k(S)
k_values = kquad(s_vector)
print(k_values)
plt.figure(figsize=(10, 3))
plt.step(s_vector, k_values, where='post')
plt.title("k(s) (step)")
plt.xlabel("s")
plt.ylabel("k")
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.tight_layout()
plt.show()




# # Diagrama de fases
# plt.figure(figsize=(10, 6))
# plt.plot(y1[0,:], y1[1, :]) # representamos pos vs vel
# plt.title("Diagrama de Fases de Hills")
# plt.xlabel("Posición (x)")
# plt.ylabel("Velocidad (v)")
# plt.grid(True)
# plt.show()    


# plt.figure(figsize=(10, 4))
# plt.plot(s_vector, y1[0, :], label='Posición (x)')
# plt.plot(s_vector, y1[1, :], label='Velocidad (v)')
# plt.title("Hills eq usando RK4")
# plt.xlabel("Tiempo (t)")
# plt.ylabel("Amplitud")
# plt.legend()
# plt.grid(True)
# plt.show()

