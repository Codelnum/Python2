from hw8pass_list import *


def enter():
    inp = int(input("выберите пункт:\n 1.Вход для преподавателей\n 2.Вход для учеников\n"))
    if inp == 1:
        res = login_check(t_dict)
        if res != False:
            return res
        else:
            enter()
    elif inp == 2:
        res = login_check(s_dict)
        if res != False:
            return res
        else:
            enter()
    else:
        print('--WRONG CHOICE!--')  
        enter()                   #после попадания сюда res == None, как сделать чтобы возвращался res от вложенной функции?
 

def login_check(some_dict):
    user = input("Username:  ")
    passw = input("Password:  ")
    if user in some_dict:
        if some_dict[f'{user}']==passw: 
            print(f'WELCOME {user}!')
            return user
        else:
            print('=WRONG PASS!=')
            return False
    else:
        print('Wrong login')
        return False

user = enter()
print(user)

