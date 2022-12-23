t_dict = {'Ivanov': str(1234),
        'Petrov': str(12345),
        'Sidorov': str(123456)}

s_dict = {'Vasya': str(4321),
        'Petya': str(54321),
        'Vova': str(654321)}


def login_check(some_dict):
    user = input("Username:  ")
    passw = input("Password:  ")
    if user in some_dict:
        if some_dict[f'{user}']==passw: 
            print('=WELCOME!=')
            return True
        else:
            print('=WRONG PASS!=')
            return False
    else:
        print('Wrong login')
        return False

