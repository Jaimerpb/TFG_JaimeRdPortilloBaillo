
using LinearAlgebra

## 1) Hills lineal homogénea, de la forma x'' + k(s)x = 0, con k(s) periódica.
# ONLY QUADS : x'' + k_quad(s)x = 0 y QUADS + BENDING MAGNET: x'' + [1/(ρ(s)^2) + k_quad(s)]x = 0

struct HillsLinealHom
    k_func::Function
end

# Constructor con argumento nombrado
HillsLinealHom(; k_func::Function) = HillsLinealHom(k_func)

# Esto es la f(s,y) que pasamos al RK para el cálculo de las pendientes
function (hills::HillsLinealHom)(s, y)
    x, v = y
    
    # la x''
    v_prima = -hills.k_func(s) * x
    return [v, v_prima]
end



struct HillsLinealNonHom
    k_func::Function
    inhom_func::Function
end


HillsLinealNonHom(;k_func::Function, inhom_func::Function) = HillsLinealNonHom(k_func,inhom_func)

function (hills::HillsLinealNonHom)(s, y)
    x, v = y
    
    # la x''
    v_prima = -hills.k_func(s)*x + hills.inhom_func(s)
    return [v, v_prima]
end
