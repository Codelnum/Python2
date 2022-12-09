# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найдите это число.

# 5 6 7 8 9 10 12 13

# with open('lsn5.txt', 'r') as file:
#     lst = list(map(int, file.read().split()))
#     for i in range(1, len(lst)):
#         if lst[i] != lst[i-1] + 1:
#             print(lst[i]-1)


# # Используем filter
# 2. Напишите программу, удаляющую из текста все слова, содержащие "hjf".

# with open('lsn5(1).txt', 'r') as file:
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


# 3. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.

# *Пример:*

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

lst = list(map(int, input('enter nums with space: ').split()))
total_list = []
temp_list=[]
for n in range(0, len(lst)):
    min = lst[n]
    temp_list.append(min)
    for i in range(n,len(lst)):
        if lst[i]> min:
            min=lst[i]
            temp_list.append(lst[i])
    total_list.append(temp_list)
    temp_list=[]
print(total_list)
