import numpy as np 
import matplotlib.pyplot as plt 

from RK import rk4
from plotting import save_figure

def trayectoriasb(modeloEDO, s_vector,dxds_0 ,ds, valsXos, apertura, filename='Trayectorias.png'):
    plt.figure(figsize= (14,6))
    plt.xlabel("s [m]", fontsize= 15)
    plt.ylabel("x [m]", fontsize = 15)
    plt.xticks(fontsize= 12)
    plt.yticks(fontsize = 12)

    for Xo in valsXos:
        y0act= np.array([Xo, dxds_0 ])
        y= rk4(modeloEDO, y0act,s_vector,ds)
        plt.plot(s_vector, y[0,:],label=f"Xo= {Xo}", linewidth= 1.5, alpha= 0.8 )
    
    plt.axhline(y= apertura, color= 'red', linestyle = '--', linewidth= 2.5)
    plt.axhline(y= -apertura, color= 'red', linestyle= '--', linewidth = 2.5)

    plt.grid(True, alpha = 0.4, linestyle= '--')
    plt.legend(loc= 'upper right', fontsize = 14)
    save_figure(filename)



def trayectoriasδ(modeloEDO, y0, s_vector, ds, valsdelta, actualizardelta, apertura, filename='Trayectorias δ.png'):
    """
    Se grafica la evoluición de la trayectorias x(s) para distintos 
    valores de delta (para distintas dispersiones).

    """

    plt.figure(figsize= (14,6))
    plt.xlabel("s [m]", fontsize= 15)
    plt.ylabel("x [m]", fontsize = 15)
    plt.xticks(fontsize= 12)
    plt.yticks(fontsize = 12)


    for val_delta in valsdelta:
        
        actualizardelta (val_delta)
        y=rk4(modeloEDO, y0, s_vector, ds)
        # plt.plot(s_vector , y[0,:], label=f"δ= {val_delta}", linewidth= 1.5, alpha= 0.8)
        plt.plot(s_vector[::100], y[0, ::100], label=f"δ= {val_delta}", linewidth=1.5)
    actualizardelta(0) #se restaur el valor de delt a un valor neutro

    # se añaden al plot las líneas que marcan la apertura de la pipe 
    plt.axhline(y= apertura, color= 'red', linestyle = '--', linewidth= 2.5, label= 'Apertura')
    plt.axhline(y= -apertura, color= 'red', linestyle= '--', linewidth = 2.5)

    plt.grid(True, alpha = 0.4, linestyle= '--')
    plt.legend(loc= 'upper right', fontsize = 14)
    save_figure(filename)