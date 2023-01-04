# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

#==========================================( КРЕСТИКИ - НОЛИКИ )===========================================
# import random
# import emoji

# desk = ' _1_ | _2_ | _3_ |\n _4_ | _5_ | _6_ |\n _7_ | _8_ | _9_ |'

# for i in range(0,5):
#     cell = input(emoji.emojize(f"{desk}\n \n В какую ячейку ставим :red_heart:  ?:    "))
#     while cell not in desk:
#         print('\n         !!!wrong cell!!!\n')
#         cell = input(emoji.emojize(f"{desk}\n В какую ячейку ставим :red_heart:  ?:    "))
#     desk = emoji.emojize(desk.replace(f'_{cell}_',' :red_heart: '))
#     if '1'in desk or '2'in desk or '3'in desk or '4'in desk or '5'in desk or '6'in desk or '7'in desk or '8' in desk or '9' in desk:
#         cell2 = (f'{random.randint(1,9)}')
#         while cell2 not in desk:
#             cell2 = (f'{random.randint(1,9)}')
#         if cell2 in desk:
#             desk = emoji.emojize(desk.replace(f'_{cell2}_',' :thumbs_up:'))
#     else:
#         print(desk) 
#         break
# print('finish!')

#==========================================(БОТ - КАЛЬКУЛЯТОР)===========================================

# from telebot import TeleBot, types
# import time
# seconds = time.time()
# local_time = time.ctime(seconds)

# Token = ''
 
# bot = TeleBot(Token)

# def save_log(some_string):
#     file = open('lesson7log.txt', 'a')
#     file.write(f'{some_string} ({local_time})\n')
#     file.close()


# @bot.message_handler(commands = ['start', 'help'])
# def answer(msg: types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text = 'Список доступных команд:\n/help - хэлп\n/math - считалка\n/log - смотрелка\n/dwnld_log -скачать логфайл')

# op_list = ['+', '-', '*', '/']

# @bot.message_handler(commands = ['math'])

# def first_msg(msg: types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text='Введите первое число')
#     @bot.message_handler()
#     def first_num(msg: types.Message):
#         global a
#         a = msg.text
#         if a.isdigit() or 'j' in a:
#             save_log(f"input first num = {a}")
#             bot.register_next_step_handler(msg, operator)
#             bot.send_message(chat_id=msg.from_user.id, text=f'{op_list}')
#             bot.send_message(chat_id=msg.from_user.id, text='Введите операцию:  ')
#         else:
#             bot.send_message(chat_id=msg.from_user.id, text=f'"{a}" не число. Введите  первое число: ')
#     bot.register_next_step_handler(msg, first_num)


# def operator(msg: types.Message):
#     global op
#     op = msg.text
#     if op not in op_list:
#         bot.send_message(chat_id=msg.from_user.id, text='Неверная операция. Введите первое число:   ')
#     else:      
#         save_log(f"input operation = {op}")
#         bot.register_next_step_handler(msg, second_num)
#         bot.send_message(chat_id=msg.from_user.id, text='Введите второе число:  ')

# def second_num(msg: types.Message):
#     global b
#     b = msg.text
#     if b.isdigit() or 'j' in b:
#         save_log(f"input second num = {b}")
#         result = math(msg, a, op, b)
#         bot.send_message(chat_id=msg.from_user.id, text=f'{a} {op} {b} = {result}')    
#         bot.send_message(chat_id=msg.from_user.id, text = 'Список доступных команд:\n/help - хэлп\n/math - считалка\n/log - смотрелка\n/dwnld_log -скачать логфайл')
#     else:
#         bot.send_message(chat_id=msg.from_user.id, text=f'"{b}" не число. Введите первое число: ')

# def math(msg:types.Message, a, op, b):
#     if 'j' in a or 'j' in b:
#         def operations(a, op, b):
#             operation = {'+': lambda a,b: complex(a)+complex(b),
#                         '-': lambda a,b: complex(a)-complex(b),
#                         '*': lambda a,b: complex(a)*complex(b),
#                         '/': lambda a,b: complex(a)/complex(b)}
#             return operation[op](a,b) 
#     else:
#         a = int(a)
#         b = int(b)
#         def operations(a,op,b):
#             operation = {'+': lambda a, b: a + b,
#                         '-': lambda a, b: a - b,
#                         '*': lambda a, b: a * b,
#                         '/': lambda a, b: a / b}
#             return operation[op](a, b)
#     result_math = operations(a, op, b)
#     save_log(f"result = {result_math}")
#     return result_math 



# @bot.message_handler(commands=['log'])
# def answer(msg: types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text = 'Число строк лога:  ')
#     @bot.message_handler()
#     def answer_log(msg: types.Message):
#         n = msg.text
#         if n.isdigit():
#             num =int(n)
#             with open ('lesson7log.txt', 'r') as file:
#                 log_list = file.readlines()
#                 out_list=[]
#                 out_text=''
#                 for i in range(1,num+1):
#                     out_list.append(log_list[-i])       
#                 for i in range(0,num):
#                     out_text = out_text+out_list[i]
#                 bot.send_message(chat_id=msg.from_user.id, text = out_text)
#                 bot.send_message(chat_id=msg.from_user.id, text = 'Список доступных команд:\n/help - хэлп\n/math - считалка\n/log - смотрелка\n/dwnld_log -скачать логфайл')
#         else:
#             bot.send_message(chat_id=msg.from_user.id, text = msg.text +' не  число, введите число')
#     bot.register_next_step_handler(msg, answer_log)



# @bot.message_handler(commands=['dwnld_log'])
# def answer(msg: types.Message):
#     file = open('lesson7log.txt', 'rb')
#     bot.send_document(msg.chat.id, file, 'log file')
#     bot.send_message(chat_id=msg.from_user.id, text = 'Список доступных команд:\n/help - хэлп\n/math - считалка\n/log - смотрелка\n/dwnld_log -скачать логфайл')

 
 
# bot.polling()

#________________________________________БОТ - ЗАПИСНАЯ КНИЖКА________________________________________

from telebot import TeleBot, types
import pandas as pd
import os

Token = ''
 
bot = TeleBot(Token)

@bot.message_handler(commands = ['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text = 'menu:\n/help\n/add\n/print\n/import\n/export')

@bot.message_handler(commands = ['add'])
def first_msg(msg: types.Message):
    bot.register_next_step_handler(msg, add_name)
    bot.send_message(chat_id=msg.from_user.id, text='enter Name: ')

def add_name(msg: types.Message):
    global name
    name = msg.text
    bot.register_next_step_handler(msg, add_surname)
    bot.send_message(chat_id=msg.from_user.id, text=f'{name} (enter Surname):  ')

def add_surname(msg: types.Message):
    global surname
    surname = msg.text
    bot.register_next_step_handler(msg, add_number)
    bot.send_message(chat_id=msg.from_user.id, text=f'{name} {surname} (enter Number):  ')

def add_number(msg: types.Message):
    global number
    number = msg.text
    bot.register_next_step_handler(msg, add_info)
    bot.send_message(chat_id=msg.from_user.id, text=f'{name} {surname} {number} (enter Some info):  ')

def add_info(msg: types.Message):
    global info
    info = msg.text
    def add_data(name, surname, number, info):
        df = pd.DataFrame({'Name':[f'{name}'],
                                'Surname':[f'{surname}'],
                                'Number': [f'{number}'],
                                'Info': [f'{info}']})
        return df
    cols=[1,2,3,4]
    file = pd.read_excel('./data.xlsx', usecols=cols)
    new_data = add_data(name, surname, number, info)
    new_file = pd.concat([file, new_data], ignore_index=True)
    new_file.to_excel('./data.xlsx')
    bot.send_message(chat_id=msg.from_user.id, text=f'Added: {name} {surname} {number} {info}')
    bot.send_message(chat_id=msg.from_user.id, text = 'menu:\n/help\n/add\n/print\n/import\n/export')


@bot.message_handler(commands = ['print'])
def show(msg: types.Message):
    rows=[1,2,3,4]
    file = pd.read_excel('./data.xlsx', usecols=rows)
    data_dict = file.to_dict('index')
    out_text=''
    for i in range(0,len(data_dict)):
        out_text = out_text + str(data_dict[i]).replace("'",'').replace("{",'').replace("}",'')+'\n'
    bot.send_message(chat_id=msg.from_user.id, text = out_text)
    bot.send_message(chat_id=msg.from_user.id, text = 'menu:\n/help\n/add\n/print\n/import\n/export')


@bot.message_handler(commands = ['export'])

def export_choice(msg: types.Message):
    choice_list=['1 - file.txt','2 - file.xlsx']
    bot.register_next_step_handler(msg, make_choice)
    bot.send_message(chat_id=msg.from_user.id, text=f'Formats:\n{choice_list[0]}\n{choice_list[1]}')
    bot.send_message(chat_id=msg.from_user.id, text='enter num:  ')

def make_choice(msg: types.Message):
    choice = msg.text
    if choice == '1':
        cols=[1,2,3,4]
        file = pd.read_excel('./data.xlsx', usecols=cols)
        ex_string = file.to_string()
        with open('data_file.txt','w') as f:
            f.write(ex_string)
        txt_file = open('data_file.txt', 'rb')
        bot.send_document(msg.chat.id, txt_file, 'TXT_file')
    elif choice == '2':
        file = open('data.xlsx', 'rb')
        bot.send_document(msg.chat.id, file, 'EXEL_file')
    else:
        bot.register_next_step_handler(msg, make_choice)
        bot.send_message(chat_id=msg.from_user.id, text='enter correct num:  ')
    bot.send_message(chat_id=msg.from_user.id, text = 'menu:\n/help\n/add\n/print\n/import\n/export')

@bot.message_handler(commands = ['import'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text = 'Send me .xlxs file')

@bot.message_handler(content_types=['document'])
def answer(msg: types.Message):
    input_file = msg.document.file_name
    with open(input_file, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
        cols=[1,2,3,4]
        my_data = pd.read_excel('./data.xlsx', usecols=cols)
        in_data = pd.read_excel(f'./{input_file}', usecols=cols)
        new_data = pd.concat([my_data, in_data], ignore_index=True)
        new_data.to_excel('./data.xlsx')
    bot.send_message(chat_id=msg.from_user.id, text='Done')
    os.remove(input_file)


bot.polling()