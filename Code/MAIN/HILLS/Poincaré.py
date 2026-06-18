import numpy as np 
import matplotlib.pyplot as plt
from RK import rk4
from plotting import save_figure
# Asegúrate de tener importada tu función rk4 y save_figure donde definas esto

def plot_poincare1(modeloEDO, x0_valores, s_vector, ds, periodo, filename, titulo="Mapa de Poincaré"):
    
    """
    Crea y guarda un mapa de Poincaré para múltiples condiciones iniciales
    
    Args:
     modeloEDO:  a clase o función del modelo a integrar
     x0_valores :pos. iniciales
     s_vector: discretización de s 
     ds: paso 
     periodo:longitud de la celda para el muestreo
    """
    plt.figure(figsize=(9, 6))
    plt.title(titulo)
    plt.xlabel("x [m]")
    plt.ylabel("x' [rad]")

    # Se calculan los índices de Poincaré, son los índices en el svector correspondientes a s= n*L, o múltiplos enteros de L (L, el periodo y longitud de la celda)
    pasosXperiodo = int(round(periodo/ ds))
    indices_poincare = range(0, len(s_vector), pasosXperiodo)

    
    for x0 in x0_valores:
        y0_act = np.array([x0, 0])

        y= rk4(modeloEDO, y0_act, s_vector, ds) #u sando el modelo que le pasemos

       
        x_p = y[0, indices_poincare]
        xp_p = y[1,indices_poincare]
        
        plt.scatter(x_p, xp_p, s=1.5, alpha =0.7, label=f"x_0 = {x0*1000} mm")


    plt.gca().set_aspect('auto') 
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(loc='upper right', fontsize=10)
    
   
    save_figure(filename) # se guarda la figura con la función 'save_figure' del módulo plotting.py 


def plot_poincareδ(modeloEDO, y0,s_vector, ds, periodo, valsdelta, actualizardelta, filename = "Poincare Dispersion.png") :
    """
    Crea y guarda un mapa de Poincaré para distintos valroes de delta.


    Args.:
    modeloEDO : Modelo a integrar
    y0 : Condiciones inciales, fijas.
    s_vector: discretización del dominio sz
    periodo: longitud de la celda 
    valsdelta : lista con distintos deltas
    actualizardleta: callback para actualizar el valor de delta en el script principal

    """

    plt.figure(figsize=(14, 7)) 
    plt.title("Mapa de Poincaré: Efecto de la Dispersión (δ)")
    plt.xlabel("x [m]")
    plt.ylabel("x' [rad]")

    pasos_por_periodo = int(round(periodo / ds))
    indices_poincare = range(0, len(s_vector), pasos_por_periodo)

    for valdelta in valsdelta:
        actualizardelta(valdelta) #actualiza el delta en el main
        
        y= rk4(modeloEDO, y0, s_vector, ds) # se integra el modelo, igual que antes.
        
        # Y como antes, se extraen los ptos. correspondientes a los ínidces de Poincaré
        x_p = y[0,indices_poincare]
        xp_p = y[1, indices_poincare]
        
        # 4. Añadimos la elipse al gráfico
        plt.scatter(x_p, xp_p, s=3, alpha=0.8, label=f"δ = {valdelta}")

    # se reestaura el valor de δ por seguridad a un valor neutro
    actualizardelta(0)

    plt.gca().set_aspect('auto')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(loc= 'upper right')
    
    save_figure(filename)