with open('hw8lessons_list.txt', 'r') as file:    #добавлять уроки надо в файл txt
    l_list = list(file.read().split())
    print(l_list)

i =0
while i < len(l_list):
    with open(f'hw8lesson_{l_list[i]}.txt', 'a')as f:   # создает файлы дз по списку уроков
        f.close
    with open(f'hw8chat_{l_list[i]}.txt', 'a')as f:   # создает файлы чата по списку уроков
        f.close
    print(f'{i+1}. {l_list[i]}')
    i+=1

l_dict = {} # словарь с заданиями
for z in range(0,len(l_list)):
    l_dict[z+1] = f'lesson_{l_list[z]}.txt'
print(l_dict)

ch_dict = {} # словарь с чатами
for z in range(0,len(l_list)):
    ch_dict[z+1] = f'chat_{l_list[z]}.txt'
print(ch_dict)

