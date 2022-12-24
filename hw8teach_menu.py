from hw8teachers_list import *
from hw8login import *
from hw8logger import log_str
# Задать домашнее задание
# Общение с учениками

lesson = teach_dict[f'{user}']

# def teachers_choice(lesson):
#     sel = int(input('Выберите действие:\n 1.Задать домашнее задание\n 2.Общение с учениками\n  '))
#     if sel == 1:
#         with open(f'hw8lesson_{lesson}.txt', 'r') as file:
#             print(file.read())
#         with open(f'hw8lesson_{lesson}.txt', 'a') as file:
#             text = input('write your message:  ')
#             file.write(f'{text}  -{log_str}\n')
#     elif sel == 2:
#         with open(f'hw8chat_{lesson}.txt', 'r') as file:
#             print(file.read())
#         with open(f'hw8chat_{lesson}.txt', 'a') as file:
#             text = input('write your message:  ')
#             file.write(f'{text}  -{log_str}\n') 
#     else:
#         print('Wrong choice')
#         teachers_choice(lesson)

# teachers_choice(lesson)