
# расчет массы заготовки круга

import math


def massa_circle(diametr_zag, length_zag, parametr_material):
    massa_zag = math.pi*(diametr_zag/1000)**2*parametr_material[0]*length_zag/4
    return massa_zag
        
