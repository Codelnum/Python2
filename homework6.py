# 1. предложить улучшения кода для четырёх уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# ==================================================================================================
# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#-------------------------------------------------------------------------------
# Было:
# 
# input_list= list(input('enter numbers with space:  ').split())
# int_list = list(map(int, input_list))
# sum = 0
# for i in range(0, len(int_list)):
#     if i % 2 == 0:
#         pass
#     else:
#         sum = sum + int_list[i]
# print(sum)
# ------------------------------------------------------------------------
# Стало:
# 
# input_list= list(input('enter numbers with space:  ').split())
# int_list = list(map(int, input_list))
# summa=0
# summa = sum([summa + int_list[i] for i in range(0,len(int_list)) if i%2 != 0]) #почему-то не хочет складывать без sum?
# print(summa)


# =============================================================================
# 2. Напишите программу, удаляющую из файла все слова, содержащие "hjf".
#--------------------------------------------------------------------------------------
# Так и было:

# .# with open('lsn5(1).txt', 'r') as file:
#     text = file.read()
# print(text)
# text_list = text.split()
# print(text_list)
# result_text = list(filter(lambda x: not 'hjf' in x, text_list))

# file = open('lsn5(1).txt', 'a')
# file.write('\n')
# file.write(''.join(result_text))
# file.close()
# print(result_text)
# 

# =============================================================================
# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

# ----------------------------------------------------------------------------------
# Было
# 
# input_list = (input('enter numbers with space: ').split())
# result_list = []
# for i in input_list:
#     if input_list.count(i) < 2:
#         result_list.append(i)
# print(result_list)

# ----------------------------------------------------------------------------------
# Стало: почему-то заполняет пустыми значениями
# input_list = (input('enter numbers with space: ').split())
# result_list = []
# result_list = [result_list.append(i) for i in input_list if input_list.count(i) < 2]
# print(result_list)

# =====================================================================================
# 4. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# ---------------------------------------------------------------------
# Так и было:

# input_list= list(input('enter numbers with space:  ').split())
# int_list = list(map(int, input_list))
# print(int_list)
# mult_list =[]
# i=0
# while i < len(int_list)/2:
#     mult_list.append(int_list[i]*int_list[-i-1])
#     i+=1
# print(mult_list)
# ===============================================================================================

# 2* Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;

# 7-(8+3*2-1)*5+1+1+2*3+1

with open('lsn6.txt', 'r') as file:
    in_str = file.read()
in_list = list(in_str)
print(f'input_list: {in_list}')

def get_br_list (some_list):
    br_list=[]
    k=0
    while k < len(some_list)-1:
        if some_list[k] != '(':
            k+=1
        else:
            k+=1
            while some_list[k] != ')':
                br_list.append(some_list[k])
                k+=1         
    return br_list

print(f'br contain: {get_br_list(in_list)}')

def calc (s_list):
    calc_list=[]
    n=0
    c=0
    while n < len(s_list):
        if s_list[n] != '*':
            calc_list.append(s_list[n])
            c+=1
            n+=1
        else:
            mult=(int(s_list[n-1])*int(s_list[n+1]))
            calc_list.pop(c-1)
            calc_list.append(mult)
            n+=2       
    return calc_list

def sum_list(s_list):
    sum_list=[]
    m=0
    while m < len(s_list):
        if s_list[m] == '+':
            sum_list.append(int(s_list[m+1]))
            m+=2
        elif s_list[m] == '-':
            sum_list.append(-int(s_list[m+1]))
            m+=2
        else:
            sum_list.append(int(s_list[m]))
            m+=1            
    return sum(sum_list)

mult_list = calc(get_br_list(in_list))
print(f'sum br contain: {sum_list(mult_list)}')


i=0
res_list = []
while i < len(in_list): 
    if in_list[i] == '(':
        while in_list[i] != ')':
         i+=1
        i+=1
        res_list.append(sum_list(calc(get_br_list(in_list)))) 
    else:
        res_list.append(in_list[i])
        i+=1

print(f'lst wout br: {res_list}')
print(f'sum list: {sum_list(calc(res_list))}')