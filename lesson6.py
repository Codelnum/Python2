# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*
# 2+2 => 4;
# 7-8+3*5+1+1+2*3 => 22;

# a = '7-82+3*5+13+1+25*3'

# b = ['7', '-', '82', '+', '3', '*', '5', '+', '13', '+', '1', '+', '25', '*', '3']

# 7, -8, 15, 1, 1, 6
# 1-2*3 => -5;


# with open('lsn6.txt', 'r') as file:
#     in_str = file.read()
# in_list=list(in_str)

# def calc_list(in_list):
#     i=0
#     calc_list=[]
#     calc_list.append(int(in_list[i]))
#     while i < len(in_list)-1:
#         if in_list[i+3] == '*' and '/':
#             calc_list.append(int(in_list[i+2])*int(in_list[i+4]))
#             i+=4
#         elif in_list[i+1] =='-':
#             calc_list.append(-int(in_list[i+2]))
#             i+=2
#         elif in_list[i+1] == '+':
#             calc_list.append(int(in_list[i+2]))
#             i+=2
#         else:
#             calc_list.append(int(in_list[i]))
#             i+=1
#     return calc_list

# print(in_str)
# print(calc_list(in_list))
# print(sum(calc_list(in_list)))



# 2. Добавьте возможность использования скобок, меняющих приоритет операций.

# 1+2*3 => 7;
# (1+2)*3 => 9;
# 7-(8+3*2-1)*5+1+1+2*3


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