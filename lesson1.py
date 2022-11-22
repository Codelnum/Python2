#Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
a = int(input('input a:  '))
b = int(input('input b:  '))
if a*a == b or b*b==a :
    print("yes")
else:
    print("no")