t_dict = {'Ivanov': str(1234),
        'Petrov': str(12345),
        'Sidorov': str(123456)}

s_dict = {'Vasya': str(4321),
        'Petya': str(54321),
        'Vova': str(654321)}


def login(some_dict):
    user = input("Username:  ")
    passw = input("Password:  ")
    if user in some_dict:
        if some_dict[f'{user}']==passw: 
            print("Welcome!")
            return True
        else:
            print('wrong login or passw')
            return False
    else:
        print('wrong login or passw')
        return False

