import numpy as np 

# def periodic_s(li, lf,f, s):
#     if s >= li and s <= lf:
#         return f(s)
    
#     elif s > lf:
#         s_new = s - (lf - li)
#         return periodic_s(li, lf, f, s_new)
    
#     elif s < li:
#         s_new = s + (lf-li)
#         return periodic_s(li, lf, f, s_new)



# #K(s), FODO without BEND (onlyquad s)
# def kquadb(s,p):
#     if s >= p.l_i and s <= (p.lq1/2):
#         return p.k_val
#     elif s > (p.lq1/ 2) and s < (p.Lc/2 - p.lq1/2):
#         return 0 
#     elif s >= (p.Lc/2 - p.lq1/2) and s <= (p.Lc/2 + p.lq1/2):
#         return -p.k_val
#     elif s > (p.Lc/2 + p.lq1/2) and s < (p.Lc - p.lq1/2):
#         return 0 
#     elif s >= (p.Lc - p.lq1/2) and s <= (p.Lc):
#         return  p.k_val
    

# def kquadp(s,p):
#     return periodic_s(p.l_i,p.Lc, lambda s_val: kquadb(s_val,p), s)


# def kquad(s,p):
#     #eN lugar de recorrer todo s_vector en cada iteración del RK4, evalúa solo el s que toque, y devuelve k evaluada en ese punto. 
#         if np.isscalar(s): 
#             return kquadp(s,p)
#         return np.array([kquadp(si,p) for si in s]) #Esto es para luego poder graficarlo






# #K(s) slide 20, FODO with bend
# def k20b(s,p):
#     if s >= p.l_i and s<= (p.l_i  + p.lq1/2):
#         return p.k_val*(1- p.delta)
#     elif s > (p.l_i+ p.lq1/ 2) and s < (p.Lc2/4 - p.ld/2):
#         return 0
#     elif s >= (p.Lc2/4 - p.ld/2) and s <= (p.Lc2/4 + p.ld/2):
#         return 1/p.rho**2
#     elif s > (p.Lc2/4 + p.ld/2) and s < (p.Lc2/2- p.lq1/2):
#         return 0
#     elif s >= (p.Lc2/2 - p.lq1/2) and s <= (p.Lc2/2 + p.lq1/2):
#         return -p.k_val* (1-p.delta)
#     elif s > (p.Lc2/2 + p.q1/2) and s < (3* p.Lc2/4 -p.ld/2):
#         return 0
#     elif s>= (3*p.Lc2/4 - p.ld/2) and s <= (3*p.Lc2/4 + p.ld/2):
#         return 1/p.rho**2
#     elif s > (3*p.Lc2/4 + p.ld/2) and s < (p.Lc2- p.lq1/2):
#         return 0
#     elif s >= (p.Lc2 - p.lq1/2) and s <= (p.Lc2):
#         return p.k_val *(1-p.delta)
    

# def k20p(s,p):
#     return periodic_s(p.l_i, p.Lc2, lambda s_val: k20b(s_val,p), s)

# def k20(s,p):
#         if np.isscalar(s) or np.ndim(s)==0: 
#             return k20p(s,p)
#         return np.array([k20p(si,p) for si in s]) #Esto es para luego poder graficarlo



# #Término inhomogeneo de la ec. de hll
# def inhomb(s, p):
#     if s >= p.l_i and s < (p.Lc2/4 - p.ld/2):
#         return 0
#     elif s >= (p.Lc2/4 - p.ld/2) and s <= (p.Lc2/4 + p.ld/2):
#         return p.delta/ p.rho
#     elif s > (p.Lc2/4 + p.ld/2) and s < (3*p.Lc2/4 - p.ld/2):
#         return 0
#     elif s >= (3*p.Lc2/4 - p.ld/2) and s <= (3*p.Lc2/4 + p.ld/2):
#         return p.delta / p.rho
#     elif s > (3*p.Lc2/4 + p.ld/2) and s <= p.Lc2:
#         return 0
#     return 0

# def inhomp(s,p):
#     return periodic_s(p.l_i, p.Lc2, lambda s_val: inhomb(s_val,p), s)


# def inhom(s,p):
#     if np.isscalar(s) or np.ndim(s)==0: 
#         return inhomp(s,p)
#     return np.array([inhomp(si,p) for si in s]) #mismo concepts


# #sextupolos
# def ksextb(s):
#     if s> (l_i + lq1/2) and s<=(l_i+ lq1/2+ lsext):
#         return k_sext*(1-𝛿)
#     elif s > (Lc2/2 + lq1/2) and s <= (Lc2/2 + lq1/2 + lsext):
#         return -k_sext*(1-𝛿)
#     else:
#         return 0
    

# def ksextp(s):
#     return periodic_s(l_i, Lc2, ksextb,s)

# def ksext(s):
#     if np.isscalar(s) or np.ndim(s)==0:
#         return ksextb(s)
    
#     return np.array([ksextp(si) for si in s])



import numpy as np 

def periodic_s(li, lf , f, s):
    if s >= li and s <= lf:
        return f(s)
    elif s > lf:
        s_new = s - (lf - li)
        return periodic_s(li, lf, f, s_new)
    elif s < li:
        s_new = s + (lf-li)
        return periodic_s(li, lf, f, s_new)

# K(s), FODO without BEND (only quads)
def kquadb(s, p):
    if s >= p.l_i and s <= (p.lq1/2):
        return p.k_val
    elif s > (p.lq1/ 2) and s < (p.Lc/2 - p.lq1/2):
        return 0 
    elif s >= (p.Lc/2 - p.lq1/2) and s <= (p.Lc/2 + p.lq1/2):
        return -p.k_val
    elif s > (p.Lc/2 + p.lq1/2) and s < (p.Lc - p.lq1/2):
        return 0 
    elif s >= (p.Lc - p.lq1/2) and s <= p.Lc:
        return p.k_val
    return 0

def kquadp(s, p):
    # Usamos un lambda para inyectar 'p' en la función base
    return periodic_s(p.l_i, p.Lc, lambda s_val: kquadb(s_val, p), s)

def kquad(s, p):
    if np.isscalar(s): 
        return kquadp(s, p)
    return np.array([kquadp(si, p) for si in s])


# K(s) slide 20, FODO with bend
def k20b(s, p):
    if s >= p.l_i and s <= (p.l_i + p.lq1/2):
        return p.k_val * (1 - p.delta)
    elif s > (p.l_i + p.lq1/ 2) and s < (p.Lc2/4 - p.ld/2):
        return 0
    elif s >= (p.Lc2/4 - p.ld/2) and s <= (p.Lc2/4 + p.ld/2):
        return 1 / p.rho**2
    elif s > (p.Lc2/4 + p.ld/2) and s < (p.Lc2/2 - p.lq1/2):
        return 0
    elif s >= (p.Lc2/2 - p.lq1/2) and s <= (p.Lc2/2 + p.lq1/2):
        return -p.k_val * (1 - p.delta)
    elif s > (p.Lc2/2 + p.lq1/2) and s < (3*p.Lc2/4 - p.ld/2):
        return 0
    elif s >= (3*p.Lc2/4 - p.ld/2) and s <= (3*p.Lc2/4 + p.ld/2):
        return 1 / p.rho**2
    elif s > (3*p.Lc2/4 + p.ld/2) and s < (p.Lc2 - p.lq1/2):
        return 0
    elif s >= (p.Lc2 - p.lq1/2) and s <= p.Lc2:
        return p.k_val * (1 - p.delta)
    return 0

def k20p(s, p):
    return periodic_s(p.l_i, p.Lc2, lambda s_val: k20b(s_val, p), s)

def k20(s, p):
    if np.isscalar(s) or np.ndim(s)==0: 
        return k20p(s, p)
    return np.array([k20p(si, p) for si in s])


# Término inhomogeneo de la ec. de hill
def inhomb(s, p):
    if s >= p.l_i and s < (p.Lc2/4 - p.ld/2):
        return 0
    elif s >= (p.Lc2/4 - p.ld/2) and s <= (p.Lc2/4 + p.ld/2):
        return p.delta / p.rho
    elif s > (p.Lc2/4 + p.ld/2) and s < (3*p.Lc2/4 - p.ld/2):
        return 0
    elif s >= (3*p.Lc2/4 - p.ld/2) and s <= (3*p.Lc2/4 + p.ld/2):
        return p.delta / p.rho
    elif s > (3*p.Lc2/4 + p.ld/2) and s <= p.Lc2:
        return 0
    return 0

def inhomp(s, p):
    return periodic_s(p.l_i, p.Lc2, lambda s_val: inhomb(s_val, p), s)

def inhom(s, p):
    if np.isscalar(s) or np.ndim(s)==0: 
        return inhomp(s, p)
    return np.array([inhomp(si, p) for si in s])


# # Sextupolos
# def ksextb(s, p):
#     if s > (p.l_i + p.lq1/2) and s <= (p.l_i + p.lq1/2 + p.lsext):
#         return p.k_sext * (1 - p.delta)
#     elif s > (p.Lc2/2 + p.lq1/2) and s <= (p.Lc2/2 + p.lq1/2 + p.lsext):
#         return -p.k_sext * (1 - p.delta)
#     else:
#         return 0

# def ksextp(s, p):
#     return periodic_s(p.l_i, p.Lc2, lambda s_val: ksextb(s_val, p), s)

# def ksext(s, p):
#     if np.isscalar(s) or np.ndim(s)==0:
#         return ksextp(s, p)
#     return np.array([ksextp(si, p) for si in s])