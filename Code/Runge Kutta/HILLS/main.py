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

        # estructura rk4, evaluando directamente con el modelo f(s,y) q le pasemos
        k1 = modeloEDO (s_i, estado_act)
        k2 = modeloEDO(s_i + 0.5*ds , estado_act + 0.5*ds*k1)
        k3= modeloEDO(s_i + 0.5*ds, estado_act + 0.5*ds*k2 )
        k4 = modeloEDO (s_i + ds, estado_act + ds*k3)

        # Estado siguiente
        y[:, i+1] = estado_act + (1/6*ds) *(k1 +2*k2 + 2*k3+ k4)

    return y 


# Parámetros

#Cond. iniciales
x0 = 1 # pos incial Xo
dxds_0 = 0 #aangulo inicial X'o
y0 = np.array([x0,dxds_0]) #estado inicial del sist

ds= .1 #milímetros
s_end= 100 #milímetros
s_vector = np.arange(0,s_end+ds, ds)

k_val = 0.541









# Definimos las funciones periódica kquad, ksext (no se puede entender como funciones continuas, han de entenderse cómo lo que son, una función definida a trozos y periódica)
# Creamos una función que devuelva cualquier función 'k' definida en el rango [li,lf]








def kquad(s_vector):
    return np.sqrt(3)* np.cos(np.sqrt(2)/100* s_vector)/100




# def ksext():

#     return

# def rho():

#     return

# 𝛿 = 0.1

# Se invocan los 'modelos'
modelo1 = onlyquads(kquad_func = kquad)
# modelo2 = quads_bending(kquad_func= kquad, rho_func = rho)
# modelo3 = hills_off(kquad_func=kquad, rho_func= rho, delta = 𝛿)
# modelo4 = sext_off(kquad_func = kquad, rho_func = rho,delta = 𝛿, ksext_func = ksext )
# modelo5 = Nonhomsext_off ( kquad_func = kquad, rho_func = rho, delta = 𝛿, ksext_func = ksext)

    
# solucions rk de los modelos
y1 = rk4(modelo1, y0, s_vector, ds)
# y2 = rk4(modelo2, y0, s_vector, ds)
# y3 = rk4(modelo3, y0,s_vector, ds)
# y4 = rk4(modelo4, y0, s_vector, ds)
# y5 = rk4(modelo5, y0, s_vector, ds)

# Diagrama de fases
plt.figure(figsize=(6, 6))
plt.plot(y1[0,:], y1[1, :]) # representamos pos vs vel
plt.title("Diagrama de Fases de Hills")
plt.xlabel("Posición (x)")
plt.ylabel("Velocidad (v)")
plt.grid(True)
plt.show()    

plt.figure(figsize=(8, 4))
plt.plot(s_vector, y1[0, :], label='Posición (x)')
plt.plot(s_vector, y1[1, :], label='Velocidad (v)')
plt.title("Hills eq usando RK4")
plt.xlabel("Tiempo (t)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()

