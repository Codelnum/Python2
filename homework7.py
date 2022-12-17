# Создать телефонный справочник с возможностью импорта\экспорта в нескольких форматах (подразумевается система хранения построково или в строку с разделителем (либо json, scv, html и тд).
# Пункты меню:
# 1. Добавить запись
# 2. Вывод справочника на экран
# 3. Импортировать справочник
# 4. Экспортировать справочник
# --------------------
# 5. Поиск имени
# 6. Удаление записи
from homework7add import add_person
from homework7print import print_list
from homework7import import import_list
from homework7export import export_list
print("select item:\n 1.Add person\n 2.Print list\n 3.Import list\n 4.Export list")
sel = int(input(''))

def select(sel):
    if sel == 1:
        add_person(input('1.Add person: '))      #add_person
    elif sel == 2:
        print_list(int(input('1 - by sting\n2 - in line:  ')))             #print_list
    elif sel == 3:
        import_list(input('Enter file_name: ' ))  #import_list
    elif sel == 4:
       export_list(input('Enter filename: ' ))   #export_list 
    else:
        print('wrong select')

select(sel)