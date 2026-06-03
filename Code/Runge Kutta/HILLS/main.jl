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
rho = 3.81       # Radio de curvatura de las partículas en la sección de los dipolos (m)
Lc2 = 5.8        # Longitud de la celda slide20 (m)

ds = 0.001  # milímetros

s_end1 = 1000*Lc  # milímetros
s_vector1 = collect(0:ds:s_end1)

s_end2 = 700* Lc2
s_vector2 = collect(0:ds:s_end2)
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
        return k_val
    elseif s > (lq1 / 2) && s < (Lc2/4 - ld/2)
        return 0
    elseif s >= (Lc2/4 - ld/2) && s <= (Lc2/4 + ld/2)
        return 1/rho^2
    elseif s > (Lc2/4 + ld/2) && s < (Lc2/2 - lq1 / 2)
        return 0
    elseif s >= (Lc2/2 - lq1 / 2) && s <= (Lc2/2 + lq1 / 2)
        return -k_val
    elseif s > (Lc2/2 + lq1 / 2) && s < (3*Lc2/4 - ld/2)
        return 0
    elseif s >= (3*Lc2/4 - ld/2) && s <= (3*Lc2/4 + ld/2)
        return 1/rho^2
    elseif s > (3*Lc2/4 + ld/2) && s < (Lc2 - lq1 / 2)
        return 0
    elseif s >= (Lc2 - lq1 / 2) && s <= Lc2
        return k_val
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
        return [k20p(si) for si in s]  # Esto es para luego poder graficarlo
    end
end


















# Se invocan los modelos de Hills.jl, uno a uno 
modelo1 = HillsLinealHom(k_func=kquad)
# modelo2 = HillsLinealHom(k_func = k20)
# soluciones rk de los modelos
y1 = rk4(modelo1, y0, s_vector1, ds)
# y2 = rk4(modelo2, y0, s_vector2, ds )




# Diagrama de fases
p1 = plot(y1[1, :], y1[2, :], xlabel="Posición (x)", ylabel="Ángulo (x')", 
          title="Diagrama de Fases de Hills, slide20", legend=false, size=(800, 600))
display(p1)

# Gráfica de posición y velocidad vs s
p2 = plot(s_vector, y1[1, :], label=" x ", xlabel=" s ", ylabel="Amplitud",
          title="Hills eq usando RK4, Accelerador slide20", size=(800, 400))
plot!(p2, s_vector, y1[2, :], label= " x' ")
display(p2)

k_values = kquad(s_vector)
println("Array k(s):")

println("Computed k(s) over ", length(s_vector), " points.")


k_plot_cells = 4
k_s_end = k_plot_cells * Lc
k_s_vector = collect(0:ds:k_s_end)
k_values = k20(k_s_vector)



# Gráfica de k(s)
p3 = plot(k_s_vector, k_values, xlabel="s", ylabel="k(s)", 
          title="Función k(s) - Regular FODO lattice", legend=false, 
          size=(1000, 400), linewidth=2, color=:blue)
display(p3)
