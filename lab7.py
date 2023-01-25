from random import randint
import logging
logging.basicConfig(level=logging.INFO, filename="LOGLAB7.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
k = int(input('k: '))
logging.info('Пользователь выбрал данное число k: ' + str(k))
l = int(input('l: '))
logging.info('Пользователь выбрал данное число l: ' + str(l))
m = int(input('m: '))
logging.info('Пользователь выбрал данное число k: ' + str(m))
n = int(input('n: '))
logging.info('Пользователь выбрал данное число n: ' + str(k))

figure = input('Выберите номер фигуры :\n1 Ферзь\n2 Ладья\n3 Слон\n4 Конь\n')
logging.info('Пользователь выбрал номер фигуры:')
# if (figure!='1' or figure!='2' or figure!='E' or figure!='H'):
#   print('Некорректные значения')
#  exit()
if ((figure == '1' and (k == m or l == n or k - l == m - n or k + l == m + n)) or
        (figure == '2' and (k == m or l == n)) or
        (figure == '3' and (k - l == m - n or k + l == m + n)) or
        (figure == '4' and ((abs(k - m) == 1 and abs(l - n) == 2) or (abs(k - m) == 2 and abs(l - n) == 1)))):
    attack = 1
else:
    attack = 0
figure2 = input('Выберите номер фигуры для второй задачи : \n1 Ферзь\n2 Ладья\n3 Слон\n')
logging.info('Пользователь выбрал номер фигуры для 2 задачи:')

if (k + l + m + n) % 2 == 0:
    print('а) Поле', (k, l), 'и поле', (m, n), 'одного цвета')
    logging.info('Программа выала поле одного цвета:')
else:
    print('а) Поле', (k, l), 'и поле', (m, n), 'не одного цвета')
logging.info('Программа выдала поле  не одного цвета:')
if attack == 1:
    print('б) Фигура', figure, 'с координатами', (k, l), 'угрожает полю', (m, n))
    logging.info('Программа выдала фигуру с координатами, которая угрожает полю:')
else:
    print('б) Фигура', figure, ' с координатами', (k, l), 'не угрожает полю', (m, n))
logging.info('Программа выдала фигуру с координатами, которая  не угрожает полю:')
if ((figure2 == '1' and (k == m or l == n or k - l == m - n or k + l == m + n)) or
        (figure2 == '2' and (k == m or l == n)) or  #ладья по горизонтали, вертикали
        (figure2 == '3' and (k - l == m - n or k + l == m + n))):  #слон по диагонали
    print('в) Фигура', figure2, 'с координатами', (k, l), 'может одним ходом попасть на поле', (m, n))
    logging.info('Программа выдала фигуру с координатами, которая может одним ходом попасть на поле:')
else:
    print('в) Фигура', figure2, 'с координатами', (k, l), 'не может одним ходом попасть на поле', (m, n))
    logging.info('Программа выдала фигуру с координатами, которая  не может одним ходом попасть на поле:')
    if figure2 == 1 or figure2 == 2:  #для ферзя и ладьи это ход по вертикали
        print('Можно попасть за два хода. Следующий ход на клетку:', (k, n))
        logging.info('Программа выдала информацию о том, что можно попасть за два хода:')
    elif figure2 == 3:
        if (k + l + m + n) % 2 == 0:
            for i in range(1, 9):
                for o in range(1, 9):  #перебор клеток
                    if (i == k and o == l) or (i == m and o == n):
                        continue
                    if (k - l == i - o or k + l == i + o) and (
                            i - o == m - n or i + o == m + n):  #если текущая клетка досягаема для слона
                        print('Можно попасть за два хода. Следующий ход на клетку:', (i, o))
                        logging.info('Программа выдала информацию о том, что можно попасть за два хода:')
                        break
        else:  #слон не может перейти на другой цвет
            print('в) Фигура', figure2, 'на', (k, l), 'не может попасть на поле', (m, n))
