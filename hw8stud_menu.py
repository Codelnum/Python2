from hw8lessons import print_list, l_list
from hw8logger import log_str
import sys

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

l_dict = {} # словарь с заданиями
for z in range(0,len(l_list)):
    l_dict[z+1] = f'hw8lesson_{l_list[z]}.txt'

ch_dict = {} # словарь с чатами
for z in range(0,len(l_list)):
    ch_dict[z+1] = f'hw8chat_{l_list[z]}.txt'


def les_choice(any_list):
    print_list(l_list)
    print(f'{len(l_list)+1}. выход')
    les = int(input('выбери предмет:  '))

    while les <=0 or  les > (len(any_list)+1):
        print('Wrong choice')
        les = int(input('выбери предмет:  '))
    if les == (len(any_list)+1):
        print('Bye!')
        sys.exit()
    elif 0 < les or les < len(any_list):
        return les


les = les_choice(l_list)


def select(les):
    do = int(input(' 1.посмотрть задание\n 2.Написать преподавателю\n 3. к выбору предмета\n что сделать:  '))
    if do == 1:    
        with open(f'{l_dict[les]}', 'r') as file:
            print(file.read())
            select(les)
    elif do == 2:
        with open(f'{ch_dict[les]}', 'r') as file:
            print(file.read())
        with open(f'{ch_dict[les]}', 'a') as file:
            text = input('write your message:  ')
            file.write(f'\n{text}  -{log_str}\n')
            select(les)
    elif do ==3:
        les = les_choice(l_list)
        select(les)
    else:
        print('wrong select')
        select(les)
