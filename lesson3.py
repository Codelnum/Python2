# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.

# from time import time
# n=int(input('введите допустимую разрядность числа: '))
# def get_num():
#     t = time()
#     t = round((t * 10000) // 1) % 10**n
#     return t

# print(get_num())

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в
# заданном списке строк некое число.
# ['22', '33', '123', 'fwefe', 'ytyy', '55']

# first_list = ['22', '55', '123', 'fwefe', 'ytyy', '55']
# num = str(input('enter num:  ')) 

# def check_list(list, n):
#     i=0
#     count=0
#     while i < len(list): 
#         if list[i] == n:
#             count+=1
#             i+=1
#         else:
#             i+=1
#     return count
# print(f'{num} встречается в списке: {check_list(first_list, num)}')

# 3. Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

main_list = str(input('задайте список строк через пробел:  ')).split()

word = str(input('enter chars: '))

def check_list(list, wrd):
    i=0
    count=0
    pos = 0
    while i < len(list):
        if list[i] == wrd:
            count+=1
            if count==2:
                pos = i
            else:
                i+=1
        else:
            i+=1
    return pos

if check_list(main_list, word) == 0:
    print('Второе вхождение отсутствует')
else: 
    print(f'индекс второго вхождения {word} в строке: {check_list(main_list, word)}')