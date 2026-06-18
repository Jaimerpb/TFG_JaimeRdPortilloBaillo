import numpy as np 
import matplotlib.pyplot as plt 

from RK import rk4
from plotting import save_figure


def numstability(modeloEDO, y0, s_end, ds, filename):
    
    """
    Evala la convergencia y estabilidad del método RK4 para un modelo dado de los definidos en el modulo 'hills'.
    
    Se va reduciendo el tamño del paso h y compara numéricamente la sol. actual con la de la iteración anteriorf (interpolando)
    Genera y guarda una gráfica logarítmica de la desviación relativa.
    """
    # Definimos los pasos a explorar basados en el paso nominal ds
    h_step_values = ds/np.array([0.01, 0.1, 0.5, 1 ,2, 4])
    desv_relativa = []

   
    hanterior = 2* ds

    s_vector_anterior = np.arange(0, s_end + hanterior, hanterior)

    y_anterior = rk4(modeloEDO, y0, s_vector_anterior, hanterior)
    x_iteracion_anterior = y_anterior[0, :]

    # Ccomparando respecto al paso anterior
    for h in h_step_values:
        print(f"Solving hills para h= {h}")
        s_vector_actual = np.arange(0, s_end+ h, h)

        y_actual= rk4(modeloEDO, y0, s_vector_actual, h)
        x_actual = y_actual[0, :]

        #Se interpolan las posiciones sol. de la anterior a las posiciones solución actual
        # esto es para comparar en los mismos puntos (np.interp)
        x_anterior_interp= np.interp(s_vector_actual , s_vector_anterior, x_iteracion_anterior)

        # Error absoluto y error relativo
        # Ahora sí, se están restando vectores de igual dimensión. 
        error_abs = np.linalg.norm(x_actual- x_anterior_interp)
        desv_rel = error_abs/ np.linalg.norm(x_anterior_interp)

        desv_relativa.append(desv_rel)

        # Ahora 'actualizamos' para la próxima iteración, Xanterior pasa a ser Xactual
        x_iteracion_anterior = x_actual
        s_vector_anterior = s_vector_actual

    print("Desviaciones relativas:", desv_relativa)

    #Figura
    plt.figure(figsize=(10, 6))
    plt.plot(h_step_values, desv_relativa, marker='o', color='purple',  
             linewidth=2.5, markersize=8, label='Desviación relativa')

    plt.gca().invert_xaxis() # invierte el eje x para que la gráfica avance a medida que h decrece
    plt.xscale('log', base= 10)    
    plt.yscale('log', base=10)  

    

    plt.title("Convergencia RK4: Estabilidad Numérica", fontsize=14, fontweight='bold')
    plt.xlabel("Tamaño del paso h (m)", fontsize=12)
    plt.ylabel("Desviación relativa", fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend(fontsize=11)
    
    
    save_figure(filename)
