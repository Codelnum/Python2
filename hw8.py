from hw8login import *


def enter():
    inp = int(input("выберите пункт:\n 1.Вход для преподавателей\n 2.Вход для учеников\n"))
    if inp == 1:
        res = login_check(t_dict)
        if res == True:
            return inp
        else:
            enter()
    elif inp == 2:
        res = login_check(s_dict)
        if res == True:
            return inp
        else:
            enter()
    else:
        print('=WRONG CHOICE!=')
        enter()
res = enter()
print(res)


