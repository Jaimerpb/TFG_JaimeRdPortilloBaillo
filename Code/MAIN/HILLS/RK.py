import numpy as np 


def rk4(modeloEDO, y0, s_vector, ds):
    
    # igual q antes solo que ahora de forma compacta y evaluando con el modelo directamente
    N= len(s_vector)
    y = np.zeros((2 , N))

    y[:, 0 ] = y0 
    
    for i in range(N - 1):
        s_i = s_vector[i]
        estado_act = y[:, i]

        #estructura rk4, evaluando directamente con el modelo f(s,y) q le pasemos
        k1= modeloEDO (s_i, estado_act)
        k2 = modeloEDO(s_i + 0.5*ds , estado_act + 0.5*ds*k1)
        k3 = modeloEDO(s_i + 0.5*ds, estado_act + 0.5*ds*k2 )
        k4=  modeloEDO (s_i + ds, estado_act + ds*k3)

        # Estado siguiente
        y[:, i+1] = estado_act + (1/6*ds) *(k1 +2*k2 + 2*k3+ k4)

    return y
