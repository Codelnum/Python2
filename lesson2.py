# '1. Напишите программу, которая принимает на вход число N и выдаёт 
#     последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# n = int(input('enter N: ')) #5
# a = 1
# b = -3
# lst = []
# count = 1
# while count < n+1:
#     lst.append(a)
#     a=a*b
#     count+=1
# print (lst)


# 2. Для натурального n создать список, 
#    состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 4: [1, 4, 7, 10, 13] 
# n = int(input('enter n: '))
# lst = []
# x = 0
# for i in range(0,n):
#     f = 3*x+1
#     lst.append(f)
#     x=x+1
# print(lst)


# 3. Напишите программу, в которой пользователь будет задавать две строки, 
#    а программа - определять количество вхождений одной строки в другой.

# some_str_1 = input()
# some_str_2 = input()
# len_str_2 = len(some_str_2)
# i = 0
# count = 0
# while i < len(some_str_1):
#     if some_str_1[i:i + len_str_2] == some_str_2:
#         count += 1
#     i += 1
# print(count)