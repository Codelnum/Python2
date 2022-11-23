# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

num = int(input('input day number 1-7: '))
if 0 < num < 8:
    if num==7 or num==8:
        print('weekend')
    else:
        print('weekday')
else:
    print('wrong number')


#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('enter  x:  '))
y = int(input('enter y:  '))
z = int(input('enter z:  '))
left = not (x or y or z)
right = not x and not y and not z

if left == right:
    print('true')
else:
    print('false')


#3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x= int(input('enter x:  '))
y= int(input('enter y:  '))
if x == y == 0:
    print("zero")
elif x == 0 and y != 0:
    print("axis X")
elif x != 0 and y == 0:
    print("axis Y")
else:
    if x > 0 and y > 0:
        print("1st quarter")
    elif x >0 and y < 0:
        print("4th quarter")
    elif x < 0 and y > 0:
        print('2nd quarter')
    else:
        print('3rd quarter')

#4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

qnum = int(input('enter qarter number(1-4):  '))
if qnum == 1:
    print('0 < x < +inf;  0 < y < +inf') 
elif qnum == 2:
    print('-inf < x < 0;  0 < y < +inf')
elif qnum == 3:
    print('-inf < x < 0;  -inf < y < 0')
elif qnum == 4:
    print('0 < x < +inf;  -inf < y < 0')
else:
    print('wrong number')

#5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math
x1 = int(input('enter x1 for A(x1;y1):  '))     #  
y1 = int(input('enter y1 for A(x1;y1):  '))     #  1; -4
x2 = int(input('enter x2 for B(x2;y2):  '))     #  
y2 = int(input('enter y2 for B(x2;y2):  '))     #  -5; -3
length = round((math.sqrt((abs(y1 - y2)) ** 2 + abs((x1 - x2)) ** 2)), 2)
print(length)