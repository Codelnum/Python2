from telebot import TeleBot, types
import pandas as pd
import os

Token = '5809540569:AAE-lQUxyJu16mMOo0GTuQq5_64N8UfpQEk'
 
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