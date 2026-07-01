import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Intentamos importar tu función de guardado
try:
    from plotting import save_figure
except ImportError:
    def save_figure(filename):
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()
        plt.close()

# --- CLAVE PARA EVITAR EL FileNotFoundError ---
# Obtenemos la ruta exacta de la carpeta donde está guardado ESTE script
DIRECTORIO_ACTUAL = Path(__file__).parent

def plottrayectoriaTHEO(archivo_txt, filename="RFTrack_Trayectoria.png"):
    """
    Lee los datos de RF-Track y grafica la trayectoria (s vs x).
    """
    # Unimos la ruta de la carpeta con el nombre del archivo de forma segura
    ruta_completa = DIRECTORIO_ACTUAL / archivo_txt
    
    print(f"Leyendo datos de trayectoria desde: {ruta_completa} ...")
    
    if not ruta_completa.exists():
        print(f"ERROR: No se encuentra el archivo en la ruta:\n{ruta_completa}")
        return

    data = np.loadtxt(ruta_completa, skiprows=1)
    
    s = data[:, 0]
    x_mm = data[:, 1]
    
    plt.figure(figsize=(14, 6))
    plt.title("Trayectoria Transversal (Solución Teórica RF-Track)", fontsize=18, pad=15)
    
    plt.plot(s, x_mm, color='darkblue', linewidth=1.5, alpha=0.9, label='Órbita RF-Track')
    
    plt.xlabel(" $s$ [m]", fontsize=16)
    plt.ylabel(" $x$ [mm]", fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend(fontsize=14, loc='upper right')
    
    save_figure(filename)


def plot_poincareTHEO(archivo_txt, filename="RFTrack_Poincare.png"):
    """
    lEe los puntos de RF-Track y dibuja el mapa de Poincaré (xx').
    """
    ruta_completa = DIRECTORIO_ACTUAL/ archivo_txt
    


    data = np.loadtxt(ruta_completa, skiprows=1)
    
    x_mm = data[:, 0]
    xp_mrad = data[:, 1]
        
    plt.figure(figsize=(9, 6))
    plt.title("Mapa de Poincaré Slide 20 (Solución Teórica RF-Track)", fontsize=18, pad=15)
    
    plt.scatter(x_mm, xp_mrad, s=15, color='darkred', alpha=0.7, label='Puntos RF-Track')
    
    plt.xlabel(" $x$ [mm]", fontsize=16)
    plt.ylabel(" $x'$ [mrad]", fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    plt.gca().set_aspect('auto')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=14, loc='upper right')
    
    save_figure(filename)


def comparativa_trayectorias(archivo_txt, s_rk4, x_rk4, filename="Comparativa_RK4_vs_RFTrack.png"):
    """
    Superpone la trayectoria calculada con tu RK4 (en metros) 
    con la extraída de RF-Track (en milímetros).
    """
    ruta_completa = DIRECTORIO_ACTUAL / archivo_txt
    
    if not ruta_completa.exists():
        print(f"ERROR: No se encuentra el archivo para comparar:\n{ruta_completa}")
        return

    # se lelen los datos teóricos
    data = np.loadtxt(ruta_completa, skiprows=1)
    s_rf = data[:, 0]
    x_rf_mm = data[:, 1]
    
    plt.figure(figsize=(14, 6))
    plt.title("Validación: RK4 (Propio) vs RF-Track (Teórico)", fontsize=18, pad=15)
    
    # se dibuja el RK4 convirtiendo los metros a milímetros (* 1000)
    plt.plot(s_rk4, x_rk4 * 1000, color='lightgray', linewidth=4.0, label='Numérica (Tu RK4)')
    
    #Dibujamos el RF-Track encima (línea punteada roja para ver si coinciden)
    plt.plot(s_rf, x_rf_mm, color='red', linestyle='--', linewidth=2.0, label='Teórica (RF-Track)')
    
    plt.xlabel("Distancia $s$ [m]", fontsize=16)
    plt.ylabel("Posición $x$ [mm]", fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    # Acotamos el eje X al límite del archivo de RF-Track para comparar justamente ese tramo
    plt.xlim(0, max(s_rf))
    
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend(fontsize=14, loc='upper right')
    
    save_figure(filename)

if __name__ == "__main__":
    
    # archivos de entrada de Javier, obtenidos con RF-Track
    archtrayectoria= "transport_table.txt"
    archpoincare = "poincare_map.txt"
    
    plottrayectoriaTHEO(archtrayectoria)
    plot_poincareTHEO(archpoincare)
    


