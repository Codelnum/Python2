# 1. Задайте строку из набора чисел. Напишите программу,
#     которая покажет большее и меньшее число.
#     В качестве символа-разделителя используйте пробел.
# input_list= list(input('enter numbers with space:  ').split())
# input_list = list(map(int, input_list))
# print(f'min: {min(input_list)} max: {max(input_list)}')


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     С помощью математических формул нахождения корней квадратного уравнения
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print(f"Дискриминант D = {round(discr,2)}")

if discr > 0:
    x1 = (-b + (discr**0.5)) / (2 * a)
    x2 = (-b - (discr**0.5)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")

#     solve(a, b, c)

# 3. Задайте два числа. Напишите программу, которая найдёт НОК
#    (наименьшее общее кратное) этих двух чисел.
# num1 = int(input('enter num1: '))  #12
# num2 = int(input('enter num2: '))  #20
# n=1
# while (num1*n) % num2!=0:
#     n+=1
# nok=num1*n
# print(f'НОК = {nok}') 