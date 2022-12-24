
def get_list(any_file):
    with open(f'{any_file}', 'r') as file:    #добавлять уроки надо в файл txt
        l_list = list(file.read().split())
    return l_list

l_list = get_list('hw8lessons_list.txt')


def print_list(any_list):
    i=0
    while i < len(any_list):
        print(f'{i+1}. {any_list[i]}')
        i+=1

def create_files(any_list):
    i =0
    while i < len(any_list):
        with open(f'hw8lesson_{any_list[i]}.txt', 'a')as f:   # создает файлы дз по списку уроков
            f.close
        with open(f'hw8chat_{any_list[i]}.txt', 'a')as f:   # создает файлы чата по списку уроков
            f.close
        i+=1

# create_files(l_list)

l_dict = {} # словарь с заданиями
for z in range(0,len(l_list)):
    l_dict[z+1] = f'hw8lesson_{l_list[z]}.txt'
# print(l_dict)

ch_dict = {} # словарь с чатами
for z in range(0,len(l_list)):
    ch_dict[z+1] = f'hw8chat_{l_list[z]}.txt'
# print(ch_dict)

