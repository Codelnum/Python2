# 1 Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$ 
# d = float(input('enter d: '))
# n=2
# m=3
# n2=4
# pi=1
# count=0
# while count < 1/d:
#     pi = pi* (n/m) * (n2/m)
#     n=n+2
#     m=m+2
#     n2=n2+2
#     count+=1
# pi = pi*4
# print(pi)



# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]
# n = int(input('enter N:  '))
# n_list = []
# x=2
# while n//x!=0:
#     if n%x==0:
#         n_list.append(x)
#         n=n//x
#     else:
#         x=x+1

# print(n_list)


# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

# input_list = (input('enter numbers with space: ').split())
# result_list = []
# for i in input_list:
#     if input_list.count(i)<2:
#         result_list.append(i)
# print(result_list)

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# k = random.randint(1,5)

# def a(x):
#     a = random.randint(2, 10*x)
#     return a

# result_list = []

# def mult(x):
#     mult_string =(f'{a(x)}*x**{x}')
#     while x>1:
#         mult_string =mult_string+ ' + ' +(f'{a(x)}*x**{x-1}')
#         x-=1 
#     return mult_string

# file = open('hw4(1).txt', 'w')
# file.write(mult(k) + ' + ' +(f'{a(k)} = 0'))
# file.close()


# k = random.randint(1,5)
# file = open('hw4(2).txt', 'w')
# file.write(mult(k) + ' + ' +(f'{a(k)} = 0'))
# file.close()



# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

file = open('hw4(1).txt', 'r')
str1 = file.read()
file.close()
str1= str1.replace('*','').replace('+','').replace('= 0','')
lst1=list(str1.split())
lst1.reverse()
print(lst1)


# file = open('hw4(2).txt', 'r')
# str2 = file.read()
# file.close()
# str2= str2.replace('*','').replace('+','').replace('= 0','')
# lst2=list(str2.split())
# lst2.reverse()
# print(lst2)
