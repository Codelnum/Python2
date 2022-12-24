from hw8lessons import *
from hw8logger import log_str
#     выберите предмет:
#     1.Литература
#         1.посмотрть задание
#         2.чат с преподавателем
#     2.География
#         1.посмотрть задание
#         2.чат с преподавателем
#     3.Математика
#         1.посмотрть задание
#         2.чат с преподавателем



def les_choice(any_list):
    print_list(any_list)
    les = int(input('выберите предмет: '))
    if 0 < les < len(any_list):
        return les
    else:
        print('Wrong choice')
        les_choice(any_list) # после прохода тут не возвращает les и все ломает?



def select(les):
    do = int(input(' 1.посмотрть задание\n 2.Написать преподавателю\n что сделать:  '))
    if do == 1:    
        with open(f'{l_dict[les]}', 'r') as file:
            print(file.read())
    elif do == 2:
        with open(f'{ch_dict[les]}', 'r') as file:
            print(file.read())
        with open(f'{ch_dict[les]}', 'a') as file:
            text = input('write your message:  ')
            file.write(f'\n{text}  -{log_str}\n')
    else:
        print('wrong select')
        select()


select(les_choice(l_list))