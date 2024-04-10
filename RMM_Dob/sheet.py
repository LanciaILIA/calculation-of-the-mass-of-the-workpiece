
# расчет массы заготовки листа

import math
    
def massa_sheet(sheet_thickness, length_zag, width_zag, parametr_material):
    
    guantity_detal_length = parametr_material[1] * 1000 // width_zag
    guantity_detal_width = parametr_material[2] * 1000 // length_zag

    guantity_detal_length_1 = parametr_material[1] * 1000 // length_zag
    guantity_detal_width_1 = parametr_material[2] * 1000 // width_zag

    guantity_detal_1 = guantity_detal_length * guantity_detal_width
    guantity_detal_2 = guantity_detal_length_1 * guantity_detal_width_1

    difference = guantity_detal_1 - guantity_detal_2

    if difference > 0:
        guantity_detal = guantity_detal_1
    else:
        guantity_detal = guantity_detal_2

    massa_sheet1 = parametr_material[0] * parametr_material[1] * parametr_material[2] * sheet_thickness
    massa_zag = massa_sheet1 / math.trunc(guantity_detal)
    return massa_zag




        

