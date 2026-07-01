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
        
    plt.figure(figsize=(10, 8))
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


if __name__ == "__main__":
    
    # archivos de entrada de Javier, obtenidos con RF-Track
    archtrayectoria= "transport_table.txt"
    archpoincare = "poincare_map.txt"
    
    plottrayectoriaTHEO(archtrayectoria)
    plot_poincareTHEO(archpoincare)
    


