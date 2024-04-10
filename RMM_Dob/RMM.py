
# расчет массы заготовки листа, трубы и круга


import circle
import brand_material
import sheet
import pipe
import assortment
import assortment_parametr


MASSA_LIST = 1
MASSA_CIRCLE = 2
MASSA_PIPE = 3
MASSA_ASSORTMENT = 4
OUTPUT = 5


def main():
    choice = 0
    while choice != OUTPUT:
        display_menu()
        choice = int(input('Выбрать вариант: '))
        
        if choice == MASSA_LIST:    # расчет массы листовой заготовки
            keep_going = 'д'
            while keep_going.lower() == 'д':
                sheet_thickness = float(input('Введите толщину листа, мм: ').replace(',','.'))
                length_zag = int(input('Введите длину заготовки, мм: '))
                width_zag = int(input('Введите ширину заготовки, мм: '))
                parametr_material = brand_material.menu_material()
                if parametr_material[1] * 1000 - length_zag < 0 and parametr_material[1] * 1000 - width_zag < 0:
                    print('Размер заготовки больше размера листа ')
                    return main()
                else:
                    result = sheet.massa_sheet(sheet_thickness, length_zag, width_zag, parametr_material)
                    print('Масса заготовки: ', format(result, '.2f'), 'кг')
                keep_going = input('продолжить?' + '(введите д, если да): ')
                            
        elif choice == MASSA_CIRCLE:    # расчет массы заготовки из прутка
            keep_going = 'д'
            while keep_going.lower() == 'д':
                diametr_zag = int(input('Введите диаметр заготовки, мм: '))
                length_zag = int(input('Введите длину заготовки, мм: '))
                parametr_material = brand_material.menu_material()
                result = circle.massa_circle(diametr_zag, length_zag, parametr_material)
                print('Масса заготовки: ', format(result, '.2f'), 'кг')
                keep_going = input('продолжить?' + '(введите д, если да): ')
            
           
        elif choice == MASSA_PIPE:  # расчет массы заготовки из трубы
            keep_going = 'д'
            while keep_going.lower() == 'д':
                diametr_pipe = float(input('Введите диаметр трубы, мм: ').replace(',','.'))
                wall_thickness = float(input('Введите толщину стенки, мм: ').replace(',','.'))
                length_zag = int(input('Введите длину заготовки, мм: '))
                length_pipe = int(input('Введите длину трубы, мм '))
                parametr_material = brand_material.menu_material()
                if length_pipe - length_zag < 0:
                    print('Длина заготовки больше длины трубы ')
                    return main()
                else:
                    result_g_d = pipe.guantity_detal(length_pipe, length_zag)
                    print('Количество заготовок из трубы, ', result_g_d, 'шт')
                    result = pipe.massa_pipe(diametr_pipe, wall_thickness, length_zag, length_pipe, parametr_material, result_g_d)
                    print('Масса заготовки: ', format(result, '.2f'), 'кг')
                    result_remains = pipe.remains(length_pipe, length_zag)
                    print('Длина остатка от трубы, ', result_remains, 'мм ')
                keep_going = input('продолжить?' + '(введите д, если да): ')
                             
        elif choice == MASSA_ASSORTMENT:   # расчет массы заготовки из сортамента
            keep_going = 'д'
            while keep_going.lower() == 'д':
                length_zag = int(input('Введите длину заготовки, мм: '))
                massa_metr = assortment_parametr.menu_typ() 
                result = assortment.massa_assortment(length_zag, massa_metr)
                print('Масса заготовки: ', format(result, '.2f'), 'кг')
                keep_going = input('продолжить?' + '(введите д, если да): ')
                
        elif choice == OUTPUT:
            print('Выход из программы.')
        else:
            print('Ошибка! Недопустимый выбор. ')
            keep_going = input('продолжить?' + '(введите д, если да): ')

          

def display_menu():
    print('1. Расчет массы листовой заготовки')
    print('2. Расчет массы заготовки из прутка')
    print('3. Расчет массы заготовки из трубы')
    print('4. Расчет массы заготовок сортамента')
    print('5. Выход')


main()
