from hw8pass_list import *


def login_check(some_dict):
    user = input("Username:  ")
    passw = input("Password:  ")
    if user in some_dict:
        if some_dict[f'{user}']==passw: 
            print(f'WELCOME {user}!')
            return True
        else:
            print('=WRONG PASS!=')
            return False
    else:
        print('Wrong login')
        return False

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
        print('--WRONG CHOICE!--')  
        enter()                   #после попадания сюда inp == None, как сделать чтобы возвращался inp от вложенной функции?
 
# print(enter())


