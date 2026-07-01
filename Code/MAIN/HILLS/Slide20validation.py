import numpy as np 
import matplotlib.pyplot as plt 
import os 
from plotting import save_figure


def plottrayectoriaTHEO(archivotxt, filename = 'RFTrack_TrayectoriaS20.png'):
    """
    Se leen los datos del txt (RFtRack) y se grafica la trayectoria (s vs x) 
    """
    
    data = np.loadtxt(archivotxt, skiprows= 1)

    s = data[:,0]
    x_mm= data[:, 1]

    plt.figure(figuresize = (14, 6))
    plt.title("Trayectoria Transversal (Solución Teórica RF-Track)", fontsize=18, pad=15)


    #Se grafic a la trayectoria
    plt.plot(s, x_mm, color='darkblue', linewidth=1.5, alpha=0.9, label='Órbita RF-Track')

    plt.xlabel("Disstancia $s$ [m]", fontsize=16)
    plt.ylabel("Posición $x$ [mm]", fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend(fontsize=14, loc='upper right')
    
    save_figure(filename)


def plotpoincare_Rftrack