# Создать телефонный справочник с возможностью импорта\экспорта в нескольких форматах (подразумевается система хранения построково или в строку с разделителем (либо json, scv, html и тд).
# Пункты меню:
# 1. Добавить запись
# 2. Вывод справочника на экран
# 3. Импортировать справочник
# 4. Экспортировать справочник
# --------------------
# 5. Поиск имени
# 6. Удаление записи
from homework7add import add_person, add_data
from homework7print import print_list
from homework7import import import_list
from homework7export import export_list
def menu():
    print("select item:\n 1.Add person\n 2.Print list\n 3.Import list\n 4.Export list")
    select = int(input(''))
    return select

sel = menu()

def select(sel):
    if sel == 1:
        name = input('Name: ')
        surname = input('Surname: ')
        number = input('Number: ')
        anything = input('Somethig else: ')
        input_string = f'{name} {surname} {number} {anything}'
        add_person(input_string)      #add_person
    elif sel == 2:
        print_list(int(input('1 - by sting\n2 - in line:  ')))             #print_list
    elif sel == 3:
        import_list(input('Enter file_name: ' ))  #import_list
    elif sel == 4:
       export_list(input('Enter filename: ' ))   #export_list 
    else:
        print('wrong select')
    sel=menu()
    select(sel)

select(sel)
