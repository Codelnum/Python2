# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num_list = list(input('enter nums:  ').replace(',', '').replace('.',''))
# sum = 0
# i=0
# while i < len(num_list):
#     #почему не работает for i in num_list( list indices must be integers or slices, not str)?
#     sum = sum + int(num_list[i])
#     i+=1
# print(sum)


# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# num = int(input('enter num:  '))  #3
# mult_list=[]
# mult=1
# for i in range(1,num+1):
#     mult = mult*i
#     mult_list.append(mult)
# print(mult_list)


# 3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)
# .
#
# n = int(input('enter n:  '))

# list = []
# for i in range(1, n+1):
#     list.append(round(((1 + 1 / i)** i), 2))
# print(list)
# sum = 0
# for i in range(0, len(list)):
#     sum = sum + list[i]
# print(sum)


# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
# n = int(input('enter n:  '))
# list =[]
# for i in range(-n, n + 1):
#     list.append(-n)
#     n=n-1
# print(list)
# str = input('enter value1 value2 with space:  ')
# sum_value = list[int(str[0])] + list[int(str[2])]
# print(f'value sum = {sum_value}')

# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint
