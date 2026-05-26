import numpy as np 
import matplotlib.pyplot as plt 
from pathlib import Path
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

k_val = 0.519     # Fuerza del gradiente magnético (1/m2)

lq1 = 0.4  # Longitud del cuadrupolo (m) 
l_i = 0  # Pos. entrada (m)
Lc =  1 # Longitud/periodo de la celda (m) 

# Slide 20
 
ld = .015 # Longitud del dipolo (m)
rho = 3.81 # Radio de curvatura de las partículas en la sección de los dipolos (m)
Lc2 = 5.8 # Longitud de la celda slide20 (m)

ds = 1e-3 # metros
s_end= 100*Lc # metros
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
print(y1)

#Estabilidad Numérica

# h_step_values = ds/np.array([0.01, 0.1, 0.5, 1 ,2, 4])
# desv_relativa = []

# h_anterior = 2* ds
# s_vector_anterior = np.arange(0, s_end+ h_anterior, h_anterior)

# y_anterior = rk4(modelo1,y0,s_vector_anterior,h_anterior)

# #De la matriz de estados cojo la fila de posiciones
# x_iteracion_anterior = y_anterior[0,:]



# # Comparando respecto al paso anterior

# for h in h_step_values:
#     print(f"Solving hills for h = {h} mm")
#     s_vector_actual = np.arange(0, s_end+ h, h)

#     y_actual = rk4(modelo1, y0, s_vector_actual, h)

#     x_actual = y_actual[0,:]

#     #Se interpolan las posiciones sol. de la anterior a las posiciones solición actual
#     # esto es para comparar en los mismos puntos (np,interp)
#     x_anterior_interp = np.interp(s_vector_actual,s_vector_anterior,x_iteracion_anterior)


#     #Error absoluto yerro relativo
#     #Ahora sí, se están restando vectores de igual dimensión. 
#     error_abs = np.linalg.norm(x_actual - x_anterior_interp)
#     desv_rel = error_abs/ np.linalg.norm(x_anterior_interp)


#     desv_relativa.append(desv_rel)

#     # Ahora 'actualizamos' para la próxima iteración, Xanterior pasa a ser Xactual
#     x_iteracion_anterior = x_actual

#     s_vector_anterior = s_vector_actual

# print(desv_relativa)

# plt.figure(figsize=(10, 6))
# plt.plot(h_step_values, desv_relativa, marker='o', color='purple',  
# linewidth=2.5, markersize=8, label='Desviación relativa')

# plt.gca().invert_xaxis() #invierte el ejex para que la gráfica avanze a medida qye h decrec3


# plt.yscale('log', base= 10)

# plt.title("Convergencia RK4: Estabilidad Numérica", fontsize=14, fontweight='bold')
# plt.xlabel("Tamaño del paso h (mm)", fontsize=12)
# plt.ylabel("Desviación relativa", fontsize=12)
# plt.grid(True, which="both", ls="--", alpha=0.5)
# plt.legend(fontsize=11)
# plt.tight_layout()
# plt.show()




#Grafica de k(S), pero limitada a 4 celdsa para mayor legibilidad
s_plot_end = 4 * Lc
s_plot = np.arange(0, s_plot_end + ds, ds)
k_values_4cells = kquad(s_plot)
plt.figure(figsize=(10, 3))
plt.step(s_plot, k_values_4cells, where='post')
plt.title("k(s) — 4 celdas")
plt.xlabel("s")
plt.ylabel("k")
plt.ylim(min(-1.5, np.min(k_values_4cells) - 0.1), max(1.5, np.max(k_values_4cells) + 0.1))
plt.grid(True)
plt.tight_layout()
plt.show()




# Diagrama de fases
# plt.figure(figsize=(10, 6))
# plt.plot(y1[0,:], y1[1, :]) # representamos pos vs vel
# plt.title("Diagrama de Fases de Hills")
# plt.xlabel("Posición (x)")
# plt.ylabel("Velocidad (v)")
# plt.grid(True)
# plt.show()    


plt.figure(figsize=(10, 4))
plt.plot(s_vector, y1[0, :], label='Posición (x)')
plt.plot(s_vector, y1[1, :], label='Velocidad (v)')
plt.title("Hills eq usando RK4")
plt.xlabel("Tiempo (t)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()


#Mapa de Poincaré (Simulando FODO onlyquads, slide 19, con varios Xo)


def INDpoincare(s_vector, period):
    # tomando la sección fija s = n*Lc, Lc es el perido.
    #Elegimos el pto de la malla discreta(de s_vector) más cercano a cada múltiplo entero del periodod.
    s_targets = np.arange(s_vector[0], s_vector[-1]+ 0.5*period, period) #estos son los 'ptos teóricos',se generan los pts s= n*Lx
    
    #searchsorted para buscar eos ptos en la malla
    indx = np.searchsorted(s_vector, s_targets) 
    # indx = np.clip(indx, 1,len(s_vector)- 1)
    
    #s e comparan el nodo izq y el der para elegi rel más cercano
    ileft = indx-1 
    iright = indx # ileft y right son dos nodos contiguos alrededor del talget

    # para ver si el nodod derecho está más cerca que le izq
    cond = np.abs(s_vector[iright]-s_targets)< np.abs(s_targets - s_vector[ileft])
    #np.where(condition, [x, y, ] /) returns elements chosen from x or y depending on a condition
    closest = np.where(cond, iright,ileft ) #son los indices en la malla que aprox cada starget

    return np.unique(closest) #devuelve índice únicos, evita repetdos por redondeo


# Ahora, función que guarda una sol. en un .txt

def savesolution_block(file_handle, x0_val, dxds_0_value, s_values, y_values):
        # columnas: 's x dxds'.
        # data = np.column_stack() construye una matriz N x 3 con las
        #     columnas (s,x(s),v(s)). Esa es la órbita 'continua' muestreada.
        # np.savetxt escribe la matriz en formato numérico legible.
        header = f"x0={x0_val:.12e}, dxds_0={dxds_0_value:.12e}"
        file_handle.write(f"# {header}\n")
        file_handle.write("# columns: s x dxds\n")
        data = np.column_stack((s_values, y_values[0, :], y_values[1, :]))
        np.savetxt(file_handle, data, fmt="%.12e")
        file_handle.write("\n")



def storemuchosX0(modeloEDO, x0_vals, dxds_0_value, s_values, ds_value, output_path):

    #guardan los ptso disc. que van a formar el mapa (x, v) y su etiqeta
    poincarex= []
    poincarev = []
    poincare_labels = []

    #abrimso el fichero,en modod escritura, y guardamos cada óribita compeplta(llamando a la función savesolution_block o)
    with open(output_path, "w", encoding="utf-8") as file_handle:
                for x0_val in x0_vals:
                        
                        y0_value = np.array([x0_val, dxds_0_value], dtype=float) # cocndiciones inic.
                        y_values = rk4(modeloEDO, y0_value, s_values, ds_value) #resuelve 
                        savesolution_block(file_handle, x0_val, dxds_0_value, s_values, y_values) #guarda la órbita completa en el txt

                        idx = INDpoincare(s_values, Lc)# devuelve los indices de la malla que aproximan s=n*L
                        
                        poincarex.append(y_values[0, idx]) #estoe es x(s_n)
                        poincarev.append(y_values[1, idx])  # y v(s_n)
                        #esto guardad la etiqueta (Xo) para el diag.
                        poincare_labels.append(np.full(idx.shape, x0_val))
     # concatenamos los res. para graficaar 
    return np.concatenate(poincarex),np.concatenate(poincarev) , np.concatenate(poincare_labels)


x0_values = np.linspace(0.25e-3,2.0e-3 , 3)
dxds_0= 0

output_path = Path(__file__).with_name("poincare_solutions.txt")
poincare_x, poincare_v, poincare_labels = storemuchosX0(
    modelo1,
    x0_values,
    dxds_0,
    s_vector,
    ds,
    output_path,
)


# diagram mapa poincaré 
plt.figure(figsize=(8, 6))
scatter = plt.scatter(poincare_x, poincare_v, c=poincare_labels, cmap="viridis", s=3, alpha=0.85)
plt.colorbar(scatter, label="x0 inicial")
plt.title("Mapa de Poincaré")
plt.xlabel("x")
plt.ylabel("dx/ds")
plt.grid(True, alpha=0.35)
plt.tight_layout()
plt.show()