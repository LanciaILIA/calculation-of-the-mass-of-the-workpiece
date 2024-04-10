
# расчет массы заготовки трубы

import math

def guantity_detal(length_pipe, length_zag):
    guantity_detal = math.trunc(length_pipe/length_zag)
    return guantity_detal
    
def massa_pipe(diametr_pipe, wall_thickness, length_zag, length_pipe, parametr_material, result_g_d):
    massa_zag = ((math.pi * (diametr_pipe / 1000)**2 / 4) - \
                           (math.pi * ((diametr_pipe - wall_thickness * 2) / 1000)**2 / 4)) * \
                           parametr_material[0] * length_pipe / result_g_d
    return massa_zag

def remains(length_pipe, length_zag):
    remains = length_pipe % length_zag
    return remains 
   
    
