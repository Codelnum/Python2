
from telebot import TeleBot, types
import time
seconds = time.time()
local_time = time.ctime(seconds)

Token = '5809540569:AAE-lQUxyJu16mMOo0GTuQq5_64N8UfpQEk'
 
bot = TeleBot(Token)

def save_log(some_string):
    file = open('lesson7log.txt', 'a')
    file.write(f'{some_string} ({local_time})\n')
    file.close()


@bot.message_handler(commands = ['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text = 'Список доступных команд:\n/help - хэлп\n/math - считалка\n/log - смотрелка\n/dwnld_log -скачать логфайл')

op_list = ['+', '-', '*', '/']

@bot.message_handler(commands = ['math'])

def first_msg(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Введите первое число')
    @bot.message_handler()
    def first_num(msg: types.Message):
        global a
        a = msg.text
        if a.isdigit() or 'j' in a:
            save_log(f"input first num = {a}")
            bot.register_next_step_handler(msg, operator)
            bot.send_message(chat_id=msg.from_user.id, text=f'{op_list}')
            bot.send_message(chat_id=msg.from_user.id, text='Введите операцию:  ')
        else:
            bot.send_message(chat_id=msg.from_user.id, text=f'"{a}" не число. Введите  первое число: ')
    bot.register_next_step_handler(msg, first_num)


def operator(msg: types.Message):
    global op
    op = msg.text
    if op not in op_list:
        bot.send_message(chat_id=msg.from_user.id, text='Неверная операция. Введите первое число:   ')
    else:      
        save_log(f"input operation = {op}")
        bot.register_next_step_handler(msg, second_num)
        bot.send_message(chat_id=msg.from_user.id, text='Введите второе число:  ')

def second_num(msg: types.Message):
    global b
    b = msg.text
    if b.isdigit() or 'j' in b:
        save_log(f"input second num = {b}")
        result = math(msg, a, op, b)
        bot.send_message(chat_id=msg.from_user.id, text=f'{a} {op} {b} = {result}')    
        bot.send_message(chat_id=msg.from_user.id, text = 'Список доступных команд:\n/help - хэлп\n/math - считалка\n/log - смотрелка\n/dwnld_log -скачать логфайл')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'"{b}" не число. Введите первое число: ')

def math(msg:types.Message, a, op, b):
    if 'j' in a or 'j' in b:
        def operations(a, op, b):
            operation = {'+': lambda a,b: complex(a)+complex(b),
                        '-': lambda a,b: complex(a)-complex(b),
                        '*': lambda a,b: complex(a)*complex(b),
                        '/': lambda a,b: complex(a)/complex(b)}
            return operation[op](a,b) 
    else:
        a = int(a)
        b = int(b)
        def operations(a,op,b):
            operation = {'+': lambda a, b: a + b,
                        '-': lambda a, b: a - b,
                        '*': lambda a, b: a * b,
                        '/': lambda a, b: a / b}
            return operation[op](a, b)
    result_math = operations(a, op, b)
    save_log(f"result = {result_math}")
    return result_math 



@bot.message_handler(commands=['log'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text = 'Число строк лога:  ')
    @bot.message_handler()
    def answer_log(msg: types.Message):
        n = msg.text
        if n.isdigit():
            num =int(n)
            with open ('lesson7log.txt', 'r') as file:
                log_list = file.readlines()
                out_list=[]
                for i in range(1,num+1):
                    out_list.append(log_list[-i])       
                for i in range(0,num):
                    bot.send_message(chat_id=msg.from_user.id, text = out_list[i])
                bot.send_message(chat_id=msg.from_user.id, text = 'Список доступных команд:\n/help - хэлп\n/math - считалка\n/log - смотрелка\n/dwnld_log -скачать логфайл')
        else:
            bot.send_message(chat_id=msg.from_user.id, text = msg.text +' не  число, введите число')
    bot.register_next_step_handler(msg, answer_log)



@bot.message_handler(commands=['dwnld_log'])
def answer(msg: types.Message):
    file = open('lesson7log.txt', 'rb')
    bot.send_document(msg.chat.id, file, 'log file')
    bot.send_message(chat_id=msg.from_user.id, text = 'Список доступных команд:\n/help - хэлп\n/math - считалка\n/log - смотрелка\n/dwnld_log -скачать логфайл')

 
 
bot.polling()