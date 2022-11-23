#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# a = int(input('input a:  '))
# b = int(input('input b:  '))
# if a*a == b or b*b==a :
#     print("yes")
# else:
#     print("no")


# #2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
# max= float('-inf')
# i=1
# for i in range(1,6):
#     num = int(input(f"input num {i}: "))
#     if num > max:
#         max=num
# print(max)

# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# list=[]
# n = int(input('enter n:  '))   #3
# for i in range(-n, n+1):
#     i=-n
#     list.append(i) #-3
#     n=(n-1)
# print(list)

# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

num = float(input("enter float num:  "))
if num % 1 == 0:
    print('no')
else:
    num = int(num % 1 * 10)
    print(num)