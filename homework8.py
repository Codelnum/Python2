from login8 import *

def enter():
    inp = int(input("выберите пункт:\n 1.Вход для преподавателей\n 2.Вход для учеников\n"))
    if inp == 1:
        log = login(t_dict)
        print(inp, log)
        return inp, log
    elif inp == 2:
        log = login(s_dict)
        print(inp, log)
        return inp, log
    else:
        print('wrong variant')
        return False
ent = enter()
print(ent)

while ent !=(1, True) or ent != (2, True):
    enter()
#Где-то уходит в бесконечный цикл