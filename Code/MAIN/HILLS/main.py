import numpy as np 
import matplotlib.pyplot as plt 


from RK import rk4
from hills import hills_lineal_hom , hills_lineal_nonhom
from auxiliar import kquad , k20, inhom
from Poincaré import plot_poincare1,plot_poincareδ
from numericalstability import numstability
from plotting import save_figure
from offmomentum import trayectoriasb, trayectoriasδ


class Parametroslattice:
    def __init__(self):

        # Sslide 19
        self.k_val= 0.519 # Es la fuerza de los cuadrupolos(1/m2)
        self.lq1= 0.4   #Longitud del cuadrupolo (m)
        self.l_i = 0     # Pos. entrada (m)
        self.Lc= 1      #Longitud de la celda/periodo

        #Slide 20
        self.delta= 0 #Error de momento 𝛿
        self.ld = 0.015 #Longitud del dipolo (m)
        self.rho= 3.81  # Radio de curvatura (m)
        self.Lc2 = 5.8  # Longiutd de la celda(m)


p= Parametroslattice() #instanciamos los para´metros


# Dsicretización del dominio 's': 

ds= 0.00025 #Tamaño del paso (m) 
s_end1= 100* p.Lc
s_vector1 = np.arange(0,s_end1 + ds, ds)

s_end2 = 70*p.Lc2
s_vector2 = np.arange(0,s_end2+ ds, ds)



#Cond. iniciales
x0= 1e-3 # pos incial Xo
dxds_0= 0 # aangulo inicial X'o
y0= np.array([x0,dxds_0]) #Estado inicial del sistema, con pos y ángulo iniciales

# iInner diametre of beam pipe
radiopipe= 0.02765 # inner radio en m

# Se invocan los 'modelos'
modelo1 = hills_lineal_hom(k_func=lambda s: kquad(s, p))
modelo2 = hills_lineal_nonhom(k_func = lambda s: k20(s,p), inhomfunc = lambda s:inhom(s,p))
# modelo3 = hillssext_off(k_func = k20,inhomfunc = inhom,ksextfunc = ksext)
    


# Soluciones del Runge Kutta
# y1 = rk4(modelo1, y0, s_vector1, ds)
# print(y1)
# y2= rk4(modelo2,y0, s_vector2, ds)
# print(y2)
# y3 = rk4(modelo3, y0, s_vector2, ds)
# print(y3)





#Mapa de Poincaré para cada sistema
x0s= np.linspace(0,5e-3,3)

# plot_poincare1(modelo1, x0s, s_vector1,ds,p.Lc, "Poincaré Hills Lineal Homogeneo.png",titulo= "Mapa de Poinca´re: FODO only quads")
# plot_poincare1(modelo2,x0s, s_vector2, ds, p.Lc2, "Poincaré Hills Lineal No HOmogeneo.png", titulo= "Mapa de Poincaré: FODO quads + BEND + offmomentum " )
# plot_poincare1(modelo3, x0s,s_vector2, ds, Lc2,"Poincaré Hills No Lineal.png", titulo=  "Mapa de Poinaré: quads+BEND + off-momentum + sextupoles")


#Mapa de Poincaré para distintos valores de delta usando tu función del módulo
# def actδ(nuevo_delta):
    # p.delta= nuevo_delta # acttualiza el parámetro delta directamente en el objeto

# valoresδ= [-0.2, -0.1, 0, 0.1, 0.2]

# plot_poincareδ(modelo2, y0, s_vector2, ds, p.Lc2, valoresδ, actδ,radiopipe, filename= "Poincaré Dispersion.png")


#Trayectorias para las distintas dispersiones, fijando cond. inic y0
# shortsvector= np.arange(0, 40*p.Lc2 + ds, ds)

# trayectoriasδ(modelo2, y0, shortsvector,ds, valoresδ, actδ, apertura=radiopipe, filename="Trayectorias vs Apert.png")



# Estabilidad Numérica (para ccada uno de los modelo)

numstability(modelo1, y0, s_end1, ds, "Establidad numérica Hills Lineal Hom.")
numstability(modelo2, y0, s_end2, ds, "Estabilidad Numérica Hills Lineal No Hom.")
# numstability(modelo3, y0, s_end2, ds, "Estabilidadc nUmérica Hills No lineal")

















# #Grafica de k(S), pero limitada a 4 celdsa para mayor legibilidad
# s_plot_end = 4 * Lc2
# s_plot = np.arange(0, s_plot_end + ds, ds)
# k_values_4cells = k20(s_plot)

# fig = plt.figure(figsize=(10, 3))
# plt.step(s_plot, k_values_4cells, where='post')
# plt.title("k(s) — 4 celdas")
# plt.xlabel("s")
# plt.ylabel("k")
# plt.ylim(min(-1.5, np.min(k_values_4cells) - 0.1), max(1.5, np.max(k_values_4cells) + 0.1))
# plt.grid(True)
# plt.tight_layout()




# Espacio de fases
# fig = plt.figure(figsize=(10, 6))
# plt.plot(y2[0,:], y2[1, :]) # representamos pos vs vel
# plt.title("Diagrama de Fases de Hills")
# plt.xlabel("Posición (x)")
# plt.ylabel("Velocidad (v)")
# plt.grid(True)



# fig = plt.figure(figsize=(10, 4))
# plt.plot(s_vector2, y2[0, :], label='Posición (x)')
# plt.plot(s_vector2, y2[1, :], label='Velocidad (v)')
# plt.title("Hills eq usando RK4")
# plt.xlabel("Tiempo (t)")
# plt.ylabel("Amplitud")
# plt.legend()
# plt.grid(True)






# #COMPARANDO VS SOL ANALÍTICA, Acelerador de la slide 19 (Thin lens approx., ver 7.3)

# f = 1/ ( k_val*lq1) # dsitancia focal
# L= Lc /2 # longitud entre quads

# # Matriz de transferencia FODO cell
# M = np.array([
#     [1 - (L**2)/(2*f**2), 2*L*  (1+ L/(2*f))],
#     [-(L/(2*f**2)) * (1 - L/(2*f)),  1- (L**2)/(2*f**2)]
# ])

# # se iniciazlian los vectores para guardar los estados al final de cada celda
# s_discret = np.arange(0, s_end+ Lc, Lc)
# y_thin= np.zeros((2,len( s_discret)))
# y_thin[:, 0] = y0

# # se multiplica la matriz celda a celda 

# for i in range(1, len(s_discret)):
#      y_thin[:, i] = M @ y_thin[:, i-1 ]




# #PLOT PRAA COMPARAR
# plt.figure(figsize=(12,5))

# #esto es la numérica, la del rk4
# plt.plot(s_vector, y1[0, :], label='Numérica RK4 (Continua)', color='lightgray', linewidth=2)

# # Dibujamos los puntos 'discretos'(por tener un paso mucho más grueso) de la solución teórica
# plt.plot(s_discret, y_thin[0, :], 'ro', markersize=4, label='Teórica Thin-Lens')

# plt.title("Dinámica Transversal: RK4 vs Thin Lens Approxi")
# plt.xlabel("s(m)")
# plt.ylabel("x(s)")
# plt.xlim(0, s_end) 
# plt.legend()
# plt.grid(True)
