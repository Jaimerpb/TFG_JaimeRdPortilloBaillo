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



def colormapApertura(modeloEDO, s_vector, ds, deltas,X0range, actualizardelta, apertura,filename='colormapapertura.png'):

       
    #se incializa la matriz para lso resultados
    Z = np.zeros((len(X0range), len(deltas)))

    for i,x0 in enumerate(X0range):
        for j,delta in enumerate (deltas):
            y0aux= np.array([x0,0])
            y = rk4(modeloEDO, y0aux,s_vector,ds)

            #se busca el desplazamiento max en la simulació
            max_amp = np.max(np.abs(y[0,:]))

            # si supera la apertura, se marca como Nan(partícula perdida)
            if max_amp> apertura:
                Z[i,j] = np.nan
            else:
                Z[i,j] = max_amp

    actualizardelta(0)

    plt.figure(figsize= (10,8))
    # config. del colormap. Los NaN se pintan en negro.
    cmap= plt.cm.viridis.copy()
    cmap.set_bad(color='black')

    #pcolormesh para el heatmap
    X, Y = np.meshgrid(deltas, X0range)
    mesh = plt.pcolormesh(X, Y, Z, cmap=cmap, shading='auto')

    # Bbarra de color con etiqueta
    cbar= plt.colorbar(mesh)
    cbar.set_label('Amplitud Máxima |x| [m]', fontsize=16)
    cbar.ax.tick_params(labelsize=14)

    plt.title("Apertura Física y Dinámica (Zonas Negras = Haz Perdido)", fontsize=18, pad=15)
    plt.xlabel("Error de Momento (δ)", fontsize=18)
    plt.ylabel("Posición Inicial $x_0$ [m]", fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    save_figure(filename)




    
