import pandas as pd

def add_person(some_string):
    with open('homework7base.txt', 'a') as hw7b:
        hw7b.write(some_string)
# ___________________________________________________________EXEL______________________________________________
# name = input('Name: ')
# surname = input('Surname: ')
# number = input('Number: ')
# info = input('Something else: ')

# def add_data(name, surname, number, info):
#     df = pd.DataFrame({'Name':[f'{name}'],
#                             'Surname':[f'{surname}'],
#                             'Number': [f'{number}'],
#                             'Info': [f'{info}']})
#     return df

# cols=[1,2,3,4]
# file = pd.read_excel('./data.xlsx', usecols=cols)

# new_data = add_data(name, surname, number, info)

# new_file = pd.concat([file, new_data], ignore_index=True)

# new_file.to_excel('./data.xlsx')


