# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import random
import emoji

desk = ' _1_ | _2_ | _3_ |\n _4_ | _5_ | _6_ |\n _7_ | _8_ | _9_ |'

for i in range(0,5):
    cell = input(emoji.emojize(f"{desk}\n \n В какую ячейку ставим :red_heart:  ?:    "))
    while cell not in desk:
        print('\n         !!!wrong cell!!!\n')
        cell = input(emoji.emojize(f"{desk}\n В какую ячейку ставим :red_heart:  ?:    "))
    desk = emoji.emojize(desk.replace(f'_{cell}_',' :red_heart: '))
    if '1'in desk or '2'in desk or '3'in desk or '4'in desk or '5'in desk or '6'in desk or '7'in desk or '8' in desk or '9' in desk:
        cell2 = (f'{random.randint(1,9)}')
        while cell2 not in desk:
            cell2 = (f'{random.randint(1,9)}')
        if cell2 in desk:
            desk = emoji.emojize(desk.replace(f'_{cell2}_',' :thumbs_up:'))
    else:
        print(desk) 
        break
print('finish!')