#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# a = int(input('input a:  '))
# b = int(input('input b:  '))
# if a*a == b or b*b==a :
#     print("yes")
# else:
#     print("no")


#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
max= float('-inf')
i=1
for i in range(1,6):
    num = int(input(f"input num {i}: "))
    if num > max:
        max=num
print(max)