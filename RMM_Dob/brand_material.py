
# выбор марки материала

steel = [7.85, 1.25, 2.5]
aluminium = [2.7, 1.2, 3.0]
brass = [8.5, 0.6, 1.5]
copper = [8.94, 0.6, 1.5]

def menu_material():
    display_material()
    material_param = []
    while True:
        choice = int(input('Выбрать вариант: '))
        if choice == 1:
            material_param = [] + steel
            break
        elif choice == 2:
            material_param = [] + aluminium
            break
        elif choice == 3:
            material_param = [] + brass
            break
        elif choice == 4:
            material_param = [] + copper
            break
        print('Недопустимый выбор!')   
    return material_param
    
def display_material():
    print('1. Сталь углеродистая')
    print('2. Алюминий')
    print('3. Латунь, бронза')
    print('4. Медь')
 

