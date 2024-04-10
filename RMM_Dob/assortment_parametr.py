
    # Параметры сортового материала

def menu_typ():
    display_typ()
    while True:
        choice = int(input('Выбрать вариант: '))
        if choice == 1:
            found = False
            search = input('Введите параметры уголка: ')
            gost8509 = open('gost_8509.txt', 'r')
            parametr = gost8509.readline()
            while parametr != '':
                massa = float(gost8509.readline().replace(',','.'))
                parametr = parametr.rstrip('\n')
                if parametr == search:
                    return massa
                    found = True
                parametr = gost8509.readline()
            gost8509.close()
            if not found:
                print('Значение не найдено. ')
                print('Добавить в базу? ')
            another = 'д'
            gost8509 = open('gost_8509.txt', 'a')
            while another.lower() == 'д':
                print('Введите новые данные: ')
                parametr = input('Параметры уголка: ')
                massa = input('Масса погонного метра, кг: ')
                gost8509.write(parametr + '\n')
                gost8509.write(massa + '\n')
                print('Добавить еще одну запись?')
                another = input('д - да, остальное - нет: ')     
            gost8509.close()
            print('Данные добавлены.')

        elif choice == 2:
            found = False
            search = input('Введите параметры уголка: ')
            gost8510 = open('gost_8510.txt', 'r')
            parametr = gost8510.readline()
            while parametr != '':
                massa = float(gost8510.readline().replace(',','.'))
                parametr = parametr.rstrip('\n')
                if parametr == search:
                    return massa
                    found = True
                parametr = gost8510.readline()
            gost8510.close()
            if not found:
                print('Значение не найдено. ')
                print('Добавить в базу? ')
            another = 'д'
            gost8510 = open('gost_8510.txt', 'a')
            while another.lower() == 'д':
                print('Введите новые данные: ')
                parametr = input('Параметры уголка: ')
                massa = input('Масса погонного метра, кг: ')
                gost8510.write(parametr + '\n')
                gost8510.write(massa + '\n')
                print('Добавить еще одну запись?')
                another = input('д - да, остальное - нет: ')     
            gost8510.close()
            print('Данные добавлены.')
  
        elif choice == 3:
            found = False
            search = input('Введите параметры трубы: ')
            gost8639 = open('gost_8639.txt', 'r')
            parametr = gost8639.readline()
            while parametr != '':
                massa = float(gost8639.readline().replace(',','.'))
                parametr = parametr.rstrip('\n')
                if parametr == search:
                    return massa
                    found = True
                parametr = gost8639.readline()
            gost8639.close()
            if not found:
                print('Значение не найдено. ')
                print('Добавить в базу? ')
            another = 'д'
            gost8639 = open('gost_8639.txt', 'a')
            while another.lower() == 'д':
                print('Введите новые данные: ')
                parametr = input('Параметры трубы: ')
                massa = input('Масса погонного метра, кг: ')
                gost8639.write(parametr + '\n')
                gost8639.write(massa + '\n')
                print('Добавить еще одну запись?')
                another = input('д - да, остальное - нет: ')     
            gost8639.close()
            print('Данные добавлены.')
            
        elif choice == 4:
            found = False
            search = input('Введите параметры трубы: ')
            gost8645 = open('gost_8645.txt', 'r')
            parametr = gost8645.readline()
            while parametr != '':
                massa = float(gost8645.readline().replace(',','.'))
                parametr = parametr.rstrip('\n')
                if parametr == search:
                    return massa
                    found = True
                parametr = gost8645.readline()
            gost8645.close()
            if not found:
                print('Значение не найдено. ')
                print('Добавить в базу? ')
            another = 'д'
            gost8645 = open('gost_8645.txt', 'a')
            while another.lower() == 'д':
                print('Введите новые данные: ')
                parametr = input('Параметры трубы: ')
                massa = input('Масса погонного метра, кг: ')
                gost8645.write(parametr + '\n')
                gost8645.write(massa + '\n')
                print('Добавить еще одну запись?')
                another = input('д - да, остальное - нет: ')     
            gost8645.close()
            print('Данные добавлены.')
            
        elif choice == 5:
            found = False
            search = input('Введите параметры профиля: ')
            gost13737 = open('gost_13737.txt', 'r')
            parametr = gost13737.readline()
            while parametr != '':
                massa = float(gost13737.readline().replace(',','.'))
                parametr = parametr.rstrip('\n')
                if parametr == search:
                    return massa
                    found = True
                parametr = gost13737.readline()
            gost13737.close()
            if not found:
                print('Значение не найдено. ')
                print('Добавить в базу? ')
            another = 'д'
            gost13737 = open('gost_13737.txt', 'a')
            while another.lower() == 'д':
                print('Введите новые данные: ')
                parametr = input('Параметры профиля: ')
                massa = input('Масса погонного метра, кг: ')
                gost13737.write(parametr + '\n')
                gost13737.write(massa + '\n')
                print('Добавить еще одну запись?')
                another = input('д - да, остальное - нет: ')     
            gost13737.close()
            print('Данные добавлены.')
        
    
def display_typ():
    print('1. Уголок стальной равнополочный ГОСТ 8509-86')
    print('2. Уголок стальной неравнополочный ГОСТ 8510')
    print('3. Труба стальная квадратная ГОСТ 8639-82')
    print('4. Труба стальная прямоугольная ГОСТ 8645-68')
    print('5. Профиль алюминиевый гост 13737-90')
    

