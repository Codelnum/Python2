from hw8pass_list import *


input_num = int(input("1 - Вход для преподавателей\n2 - Вход для учеников\nВведите число:\n"))
while input_num != 1 and input_num !=2:
    print('-WRONG NUM-')
    input_num = int(input("1 - Вход для преподавателей\n2 - Вход для учеников\nВведите число:\n"))

def login_check(some_dict):
    user = input("Username:  ")
    passw = input("Password:  ")
    if user in some_dict:
        if some_dict[f'{user}'] == passw: 
            print(f'WELCOME {user}!')
            return user
        else:
            print('WRONG PASS!')
            return False
    else:                           
        print('WRONG LOGIN!')
        return False


def check(num):
    if num == 1:
        user = login_check(t_dict)
        while user == False:
            user = login_check(t_dict) 
        return user
    elif num ==2:
        user = login_check(s_dict)
        while user == False:
            user = login_check(s_dict) 
        return user
    else:
        print('wrong input_num!')
        return False

true_user = check(input_num)

if true_user == False:
    check(input_num)
else:
    pass     