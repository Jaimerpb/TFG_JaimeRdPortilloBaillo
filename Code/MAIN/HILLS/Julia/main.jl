
using LinearAlgebra
using Plots

# Importamos el módulo de Hills
include("hills.jl")

# Definimos el RK4 que resuelve el tipo de EDO que le pasemos
function rk4(modeloEDO, y0, s_vector, ds)
    # igual que antes solo que ahora de forma compacta y evaluando con el modelo directamente
    N = length(s_vector)
    y = zeros(2, N)
    
    y[:, 1] = y0
    
    for i in 1:(N - 1)
        s_i = s_vector[i]
        estado_act = y[:, i]
        
        # estructura rk4, evaluando directamente con el modelo f(s,y) que le pasemos
        k1 = modeloEDO(s_i, estado_act)
        k2 = modeloEDO(s_i + 0.5 * ds, estado_act + 0.5 * ds * k1)
        k3 = modeloEDO(s_i + 0.5 * ds, estado_act + 0.5 * ds * k2)
        k4 = modeloEDO(s_i + ds, estado_act + ds * k3)
        
        # Estado siguiente
        y[:, i + 1] = estado_act + (1/6 * ds) * (k1 + 2 * k2 + 2 * k3 + k4)
    end
    
    return y
end

# Parámetros

# Cond. iniciales
x0 = 1e-3  # pos inicial X0
dxds_0 = 0  # ángulo inicial X'0
y0 = [x0, dxds_0]  # Estado inicial del sistema, con pos y ángulo iniciales





function periodic_s(li, lf, f, s)
    if s >= li && s <= lf
        return f(s)
    elseif s > lf
        s_new = s - (lf - li)
        return periodic_s(li, lf, f, s_new)
    elseif s < li
        s_new = s + (lf - li)
        return periodic_s(li, lf, f, s_new)
    end
end

# Slide 19

k_val = 0.519     # Fuerza del gradiente magnético (1/m2)
lq1 = 0.4         # Longitud del cuadrupolo (m)
l_i = 0          # Pos. entrada (m)
Lc = 1           # Longitud/periodo de la celda (m)

# Slide 20

ld = 0.015       # Longitud del dipolo (m)
ρ = 3.81       # Radio de curvatura de las partículas en la sección de los dipolos (m)
Lc2 = 5.8        # Longitud de la celda slide20 (m)

ds = 0.001  # milímetros

s_end1 = 1000*Lc  # milímetros
s_vector1 = collect(0:ds:s_end1)

s_end2 = 100* Lc2
s_vector2 = collect(0:ds:s_end2)

δ = 0.01


function kquadb(s)
    if s >= l_i && s <= (lq1 / 2)
        return k_val
    elseif s > (lq1 / 2) && s < (Lc / 2 - lq1 / 2)
        return 0
    elseif s >= (Lc / 2 - lq1 / 2) && s <= (Lc / 2 + lq1 / 2)
        return -k_val
    elseif s > (Lc / 2 + lq1 /2) && s < (Lc - lq1 / 2)
        return 0
    elseif s >= (Lc - lq1 / 2) && s <= Lc
        return k_val
    end
end

function kquadp(s)
    return periodic_s(l_i, Lc, kquadb, s)
end

function kquad(s)
    # En lugar de recorrer todo s_vector en cada iteración del RK4, 
    # evalúa solo el s que toque, y devuelve k evaluada en ese punto.
    if isa(s, Number)
        return kquadp(s)
    else
        return [kquadp(si) for si in s]  # Esto es para luego poder graficarlo
    end
end



function k20b(s)
    if s >= l_i && s <= (lq1 / 2)
        return k_val*(1-δ)
    elseif s > (lq1 / 2) && s < (Lc2/4 - ld/2)
        return 0
    elseif s >= (Lc2/4 - ld/2) && s <= (Lc2/4 + ld/2)
        return 1/ρ^2
    elseif s > (Lc2/4 + ld/2) && s < (Lc2/2 - lq1 / 2)
        return 0
    elseif s >= (Lc2/2 - lq1 / 2) && s <= (Lc2/2 + lq1 / 2)
        return -k_val*(1-δ)
    elseif s > (Lc2/2 + lq1 / 2) && s < (3*Lc2/4 - ld/2)
        return 0
    elseif s >= (3*Lc2/4 - ld/2) && s <= (3*Lc2/4 + ld/2)
        return 1/ρ^2
    elseif s > (3*Lc2/4 + ld/2) && s < (Lc2 - lq1 / 2)
        return 0
    elseif s >= (Lc2 - lq1 / 2) && s <= Lc2
        return k_val*(1-δ)
    end
end

function k20p(s)
    return periodic_s(l_i, Lc2, k20b, s)
end

function k20(s)
    # En lugar de recorrer todo s_vector en cada iteración del RK4, 
    # evalúa solo el s que toque, y devuelve k evaluada en ese punto.
    if isa(s, Number)
        return k20p(s)
    else
        return [k20p(si) for si in s]  # Esto es para luego poder graficar
    end
end 




function inhomb(s)
    if s >= l_i && s < (Lc2/4 -  ld/2)
        return 0
    elseif s>= (Lc2/4 - ld/2) && s<= (Lc2/4 + ld/2)
        return δ/ρ
    elseif s> (Lc2/4 + ld/2) && s< (3Lc2/4 - ld/2)
        return 0 
    elseif s >=(3Lc2/4 - ld/2) && s<=(3Lc2/4 + ld/2)
        return δ/ρ
    else 
        return 0
    end
end 

function inhomp(s)
    return periodic_s(l_i, Lc2, inhomb, s)
end

function inhom(s)
    if isa(s, Number)
        return inhomp(s)
    else
        return [inhomp(si) for si in s]
    end
end
    





# Se invocan los modelos de Hills.jl, uno a uno 
# modelo1 = HillsLinealHom(k_func = kquad)
modelo2 = HillsLinealNonHom(k_func = k20, inhom_func = inhom)
# soluciones rk de los modelos
# y1 = rk4(modelo2, y0, s_vector2, ds)
y2 = rk4(modelo2, y0, s_vector2, ds )


# # # Diagrama de fases: posición vs velocidad
# # fig = plot(
# #     y2[1, :], y2[2, :],
# #     size=(1000, 600),
# #     title="Diagrama de Fases de Hills",
# #     xlabel="Posición (x)",
# #     ylabel="Velocidad (v)",
# #     grid=true,
# #     legend=false
# # )
# # display(fig)


# # # Posición y velocidad en función del tiempo
# # fig2 = plot(
# #     s_vector2, y2[1, :],
# #     size=(1000, 400),
# #     label="Posición (x)",
# #     title="Hills eq usando RK4",
# #     xlabel="Tiempo (t)",
# #     ylabel="Amplitud",
# #     grid=true
# # )
# # plot!(fig2, s_vector2, y2[2, :], label="Velocidad (v)")
# # display(fig2)












# Gráfica de posición y velocidad vs s
# p2 = plot(s_vector2, y1[1, :], label=" x ", xlabel=" s ", ylabel="",
#           title="Hills eq usando RK4, Accelerador slide20", size=(800, 400))
# plot!(p2, s_vector2, y1[2, :], label= " x' ")
# display(p2)

# ------------------ Mapa de Poincare (elemental y formativo) ------------------
# Estado: X = [x, x'].
# Ecuacion: dX/ds = f(X,s), con f periodica en s de periodo T.
# Mapa de Poincare: X_n = X(nT), es decir, muestreo estroboscopico cada periodo.
# Fisicamente: cada punto representa el estado de la particula al final de celda.

# T = Lc2
# period_steps = max(1, Int(round(T / ds)))
# sample_idxs = 1:period_steps:length(s_vector2)

# # Varias particulas = varias condiciones iniciales (x0, x0').
# # Mismo campo de fuerzas, distinto punto inicial en espacio de fases.
# x0_values = range(-5e-3, 5e-3, length=5)
# xp0_values = range(-2e-3, 2e-3, length=3)
# inits = [[x0i, xp0i] for x0i in x0_values for xp0i in xp0_values]

# # Mostramos los ultimos puntos para reducir el transitorio inicial.
# nplot = min(200, length(sample_idxs))
# fig_poincare = plot(xlabel="x", ylabel="x'", title="Mapa de Poincare (varias condiciones iniciales)", legend=false)

# for x0i in inits
#     y_i = rk4(modelo2, x0i, s_vector2, ds)
#     pts = y_i[:, sample_idxs]
#     start = max(1, size(pts, 2) - nplot + 1)
#     scatter!(fig_poincare, pts[1, start:end], pts[2, start:end], markersize=2, alpha=0.8)
# end

# display(fig_poincare)



# k_values = k20(s_vector2)
# println("Array k(s):")

# println("Computed k(s) over ", length(s_vector2), " points.")



# # Grafincando k(s), FODO with BEND
# k_plot_cells = 4
# k_s_end = k_plot_cells * Lc2
# k_s_vector = collect(0:ds:k_s_end)
# k_values = k20(k_s_vector)


# p3 = plot(k_s_vector, k_values, xlabel="s", ylabel="k(s)", 
#           title="Función k(s) - Regular FODO lattice", legend=false, 
#           size=(1000, 400), linewidth=2, color=:blue)
# display(p3)

ds_fino = 0.00025 
s_vector2_fino = collect(0:ds_fino:s_end2)

# Colores para que el degradado de deltas sea visualmente intuitivo
valores_delta = [-0.02, -0.01, 0.0, 0.01, 0.02]
colores = [:red, :orange, :green, :blue, :purple]

plt_poincare = plot(
    title="Espacio de Fases: Efecto de la Dispersión", 
    xlabel="Posición x [m]", 
    ylabel="Divergencia x' [rad]",
    framestyle=:box,
    grid=true,
    gridalpha=0.3,
    legend=:outertopright,
    aspect_ratio=:none # Dejamos que Julia escale los ejes para ver bien las elipses
)

# Calculamos los nuevos índices con el ds ajustado
pasos_por_periodo = round(Int, Lc2 / ds_fino)
indices_poincare = 1:pasos_por_periodo:length(s_vector2_fino)

for (i, val_delta) in enumerate(valores_delta)
    global δ = val_delta 
    
    # Integramos con la nueva malla fina
    y_temp = rk4(modelo2, y0, s_vector2_fino, ds_fino)
    
    x_p = @view y_temp[1, indices_poincare]
    xp_p = @view y_temp[2, indices_poincare]
    
    # Plot más limpio: puntos más pequeños, sin bordes y conectados ligeramente si quieres
    scatter!(plt_poincare, x_p, xp_p, 
        label="δ = $val_delta", 
        color=colores[i],
        markersize=1.2,           
        markerstrokewidth=0,      
        seriesalpha=0.9           
    )
end

global δ = 0.01 # Restaurar valor

display(plt_poincare)