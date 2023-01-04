from telebot import TeleBot, types
import os
 
TOKEN = '5809540569:AAE-lQUxyJu16mMOo0GTuQq5_64N8UfpQEk'
 
bot = TeleBot(TOKEN)
 
 
# Функция для сохранения документа, отправленного боту
@bot.message_handler(content_types=['document'])
def answer(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу логыыыы')
    os.remove(filename)
 
 
@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    lst = ['+', '-']
    bot.send_message(chat_id=msg.from_user.id, text=f'Введите арифметическую операцию \n{" ".join(lst)}')
 
 
@bot.message_handler(commands=['log'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')
 
 
@bot.message_handler()
def answer(msg: types.Message):
 
    text = msg.text
    if text == '+':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
    elif text == '-':
        bot.register_next_step_handler(msg, answer2)
        bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
                                                        ', а должны были арифметическое действие')
 
 
def answer1(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')
 
 
def answer2(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')
 
 
bot.polling()
 
 