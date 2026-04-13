import numpy as np 
import matplotlib.pyplot as plt 

# Del módulo hills importamso las EDOS

from hills import onlyquads



#Definimos el RK4 q resuleva con la tipo d eEDO q le pasemos

def rk4 (modeloEDO, y0, s_vector, ds):
    # igual q antes solo que ahora de fomra compacta y evaluando con el modelo directmente
    N= len(s_vector)
    y = np.zeros((2 , N))

    y[:, 0 ] = y0 
    
    for i in range(N - 1):
        s_i = s_vector[i]
        estado_act = y[:, i]

        # estructura rk4, evaluando directamente con el modelo q le pasemos
        k1 = modeloEDO (s_i, estado_act)
        k2 = modeloEDO(s_i + 0.5*ds , estado_act + 0.5*ds*k1)
        k3= modeloEDO(s_i + 0.5*ds, estado_act + 0.5*ds*k2 )
        k4 = modeloEDO (s_i + ds, estado_act + ds*k3)

        # Estado siguiente
        y[:, i+1] = estado_act + (1/6*ds) *(k1 +2*k2 + 2*k3+ k4)

    return y 


# Parámetros y funciones

#Cond. iniciales
x0 = 1 # pos incial Xo
dxds_0 = 0 #aangulo inicial X'o
y0 = np.array([x0,dxds_0]) #estado inicial del sist

ds= 1 #milímetros
s_end= 1000 #milímetros
s_vector = np.linspace(0,s_end,1001)

#definimos la función k(s)
def k(s):
    return np.cos(s)

# def rho(s):
#     return ??

# se invocan los 'modelos'
modelo1 = onlyquads(k_func = k)
modelo2 = 
# sols rk de los modelos
y1 = rk4(modelo1, y0, s_vector, ds)


# Diagrama de fFASES

plt.figure(figsize=(6, 6))
plt.plot(y1[0,:], y1[1, :]) # representamos pos vs vel
plt.title("Diagrama de Fases de Hills")
plt.xlabel("Posición (x)")
plt.ylabel("Velocidad (v)")
plt.grid(True)
plt.show()