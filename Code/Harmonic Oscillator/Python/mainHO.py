
import numpy as np
import matplotlib.pyplot as plt


class OAsimple:
    def __init__(self, omega):
        self.omega = float(omega)

    def __call__(self, s, y):
        x, v = y
        return np.array([v, -(self.omega**2) * x])


def rk4(modelo_edo, y0, s_vector, ds):
    
    n_puntos = len(s_vector)
    y = np.zeros((2, n_puntos), dtype=float)
    y[:, 0] = y0

    for i in range(n_puntos - 1):
        s_i = s_vector[i]
        estado_act = y[:, i]

        k1= modelo_edo(s_i, estado_act)
        k2= modelo_edo(s_i + 1/2* ds, estado_act + 1/2 * ds *k1)
        k3 = modelo_edo(s_i + 1/2* ds, estado_act + 1/2* ds * k2)
        k4= modelo_edo(s_i + ds, estado_act + ds * k3)

        y[:, i + 1]= estado_act + (ds /6) * (k1 + 2 *k2 + 2 *k3 + k4)

    return y



#Defino la matriz solución como funciók de python
def matrizflujo(omega, s):
    #Sol teórica de la edc x''(s) + omega^2x(s)= 0
    return np.array(
        [[np.cos(omega * s), np.sin(omega* s)/ omega],
        [-omega* np.sin(omega* s), np.cos(omega* s)],
        ]
    )


#Se va aplicando la matriz de flujo para la obtención de soluciones
def solteorica(omega, y0, s_vector):
    y_teorica = np.zeros((2, len(s_vector)), dtype=float)
    for i, s in enumerate(s_vector):
        y_teorica[:, i] = matrizflujo(omega,s)@ y0
    return y_teorica


#Parácmetros
omega= 1
x0 =1
dxds_0= 0
y0 = np.array([x0, dxds_0], dtype=float)

ds = 1e-3
s_end = 20 * (2*np.pi / omega)
s_vector = np.arange(0.0, s_end + ds, ds)



# Modelo y solución
modelo = OAsimple(omega=omega)
y_rk4 = rk4(modelo, y0, s_vector, ds) #solución via RK4
y_teorica = solteorica(omega, y0, s_vector) #sol. teórica


error_max = np.max(np.abs(y_rk4- y_teorica))
print(f"Errorl abs. máximo RK4 vs solución teórica: {error_max:.6e}")


#Solución
plt.figure(figsize=(11, 4))
plt.plot(s_vector, y_rk4[0, :], label="RK4: x(s)", color="tab:blue")
plt.plot(s_vector, y_teorica[0, :], "--", label="Teórica: x(s)", color="tab:orange")
plt.title("Oscilador armónico simple: RK4 vs solucin teórica")
plt.xlabel("s")
plt.ylabel("x(s)")
plt.grid(True, alpha=0.35)
plt.legend()
plt.tight_layout()

#FASES
plt.figure(figsize=(6, 6))
plt.plot(y_rk4[0, :], y_rk4[1, :], label="RK4")
plt.plot(y_teorica[0, :], y_teorica[1, :], "--", label="Teórica")
plt.title("Diagrama de fases del oscilador armónico simple")
plt.xlabel("x")
plt.ylabel("dx/ds")
plt.grid(True, alpha=0.35)
plt.legend()
plt.tight_layout()
plt.show()