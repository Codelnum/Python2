# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# input_list= list(input('enter numbers with space:  ').split())
# int_list = list(map(int, input_list))
# sum = 0
# for i in range(0, len(int_list)):
#     if i % 2 == 0:
#         pass
#     else:
#         sum = sum + int_list[i]
# print(sum)


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# input_list= list(input('enter numbers with space:  ').split())
# int_list = list(map(int, input_list))
# print(int_list)
# mult_list =[]
# i=0
# while i < len(int_list)/2:
#     mult_list.append(int_list[i]*int_list[-i-1])
#     i+=1
# print(mult_list)


#3.  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# input_list = list(input('enter numbers with space:  ').split())
# float_list = list(map(float, input_list))
# maxvl_list = []
# for i in range(0,len(float_list)):
#     tmp = round(float_list[i]%1, 3)
#     if tmp!=0:
#         maxvl_list.append(tmp)
# spread = max(maxvl_list) - min(maxvl_list)
# print(spread)

#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input('enter num:  '))
# res = ''
# while num > 0:

#     res = str(num%2)+res
#     num =num//2
# print(res)


#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('enter num:  '))
neg = -num
nfib1 = 1
nfib2 = -1
fibo_list = [0]
for i in range (neg,0):
    nfib3=nfib1-nfib2
    fibo_list.insert(0,nfib1)
    nfib1=nfib2
    nfib2=nfib3

fib1 = 1
fib2 = 1
for i in range(0,num):
    fib3=fib2+fib1
    fibo_list.append(fib1)
    fib1=fib2
    fib2=fib3
print(fibo_list)

