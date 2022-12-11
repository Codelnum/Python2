# 1 Напишите программу, удаляющую из файла все слова, содержащие "hjf".

# .# with open('lsn5(1).txt', 'r') as file:
#     text = file.read()
# print(text)
# text_list = text.split()
# print(text_list)
# result_text = list(filter(lambda x: not 'hjf' in x, text_list))

# file = open('lsn5(1).txt', 'a')
# file.write('\n')
# file.write(''.join(result_text))
# file.close()
# print(result_text)
# .
# 2 Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


# import random 
# total = int(input('Введите кол-во конфет: '))
# print(f"Конфет в куче: {total}, берем по очереди от 1 до 28 конфет. Погнали.")

# while total != 0:
#     num1 = int(input('введите число от 1 до 28:  '))
#     if 0 < num1 <29:
#         total = total - num1
#         if total< 29:
#             num2 = total
#             total=total-num2
#             print(f'взято конфет:{num1}, бот вязл: {num2}, осталось: {total}. Восстание машин началось.')
#         elif total<57:
#             num2 = total-29
#             total = total - num2
#             print(f'взято конфет:{num1}, бот вязл: {num2}, осталось: {total}')
#         else:
#             num2 = random.randint(1,28)
#             total = total - num2
#             print(f'взято конфет:{num1}, бот вязл: {num2}, осталось: {total}')
#     else: 
#         print('wrong number')


# 3 Создайте программу для игры в "Крестики-нолики".

# Вариант интерфейса:

#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9
# .
# import random
# desk = '_1_|_2_|_3_|\n_4_|_5_|_6_|\n_7_|_8_|_9_|'

# for i in range(0,5):
#     cell = input(f"{desk}\n В какую ячейку ставим X?:  ")
#     while cell not in desk:
#         print('\n         !!!wrong cell!!!\n')
#         cell = input(f"{desk}\n В какую ячейку ставим X?:  ")
#     desk = desk.replace(f'{cell}','X')
#     if '1'in desk or '2'in desk or '3'in desk or '4'in desk or '5'in desk or '6'in desk or '7'in desk or '8' in desk or '9' in desk:
#         cell2 = (f'{random.randint(1,9)}')
#         while cell2 not in desk:
#             cell2 = (f'{random.randint(1,9)}')
#         if cell2 in desk:
#             desk = desk.replace(f'{cell2}','0')
#             print(f"{desk}\n В какую ячейку ставим x?:  ")
#     else:
#         print(desk) 
#         break
# print('finish!')

# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

# with open('hw5in.txt', 'r') as file:
#     in_str = file.read()
# out_str = ''
# count=1
# i=0
# while i<len(in_str)-1:
#     if in_str[i] == in_str[i+1]:
#         count+=1
#         i+=1
#     else:
#         out_str+=f'{count}{in_str[i]}'
#         count=1
#         i+=1
# out_str += f"{count}{in_str[i]}"
# print(out_str)
# with open('hw5out.txt', 'w') as file:
#     file.write(out_str)



# 5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

# *Пример:* 

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# lst = list(map(int, input('enter nums with space: ').split()))
# total_list = []
# temp_list=[]
# for n in range(0, len(lst)):
#     min = lst[n]
#     temp_list.append(min)
#     for i in range(n,len(lst)):
#         if lst[i]> min:
#             min=lst[i]
#             temp_list.append(lst[i])
#     total_list.append(temp_list)
#     temp_list=[]
# print(total_list)