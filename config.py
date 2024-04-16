import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import sqlite3

token = ''
bot = telebot.TeleBot(token)
delete = ReplyKeyboardRemove()

# главные словари
replys: dict = {} 
buttons: dict = {}

language = {
    'uz': KeyboardButton(text="O'zbek tili"),
    'ru': KeyboardButton(text="Русский язык"),
    
}

#переменные с информацией о пользователях
grade = None
have_ielts = None
countryy = None
contact = None





#Приветствие
@bot.message_handler(commands=["start"])
def choose_lang(message):
    conn = sqlite3.connect('db_client.sql')
    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, grade varchar(50), have_ielts TEXT NOT NULL, country TEXT NOT NULL, contact TEXT NOT NULL )')
    conn.commit()
    cursor.close()
    conn.close()
    
    
    
    
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(language['uz'], language['ru'])
    
    bot.send_message(message.chat.id, "Выберите язык\nTilni tanlang", reply_markup=btn)
    
    
#Функция определет язык Рус./Uzb.
@bot.message_handler(content_types=["text"])
def answer(message):
    global replys, buttons, language
    
    if message.text == "O'zbek tili":
        from uzb import reply1 as uzb_replay
        from uzb import button1 as uzb_button
        # импорт текстов на узбекском
        replys.update(uzb_replay)
        buttons.update(uzb_button)
            
    elif message.text == "Русский язык":
        from rus import reply1 as rus_reply
        from rus import button1 as rus_button
        # импорт текстов на русском
        replys.update(rus_reply)
        buttons.update(rus_button)
        
    else:
        bot.send_message(message.chat.id, "Что то пошло не так, пожалуйста выберите предоставленный вариант ответа.\nKechirasiz xato yuz berdi, iltimos, taqdim etilgan javob variantlaridan birini tanlang.")
        return      
    
    bot.send_message(message.chat.id, replys.get('greeting'), reply_markup=delete)
    bot.send_message(message.chat.id, replys.get('grade')) # вот тут вот запрос на то в каком классе либо курсе учится клиент
    bot.register_next_step_handler(message, ielts)

# функция выводит информацию о уровне английского пользователя 
def ielts(message):
    global grade
    grade = message.text # школьник ? студент ? )))
    
    
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(buttons.get('yes'), buttons.get('no'), buttons.get('preparing'))
    bot.send_message(message.chat.id, replys.get('ielts'), reply_markup=btn)
    bot.register_next_step_handler(message, ielts2)
    
# обработка данных с функции выше
def ielts2(message):
        
    if message.text not in ['Ha', 'Да']:
        country(message)
        
    else:
        bot.send_message(message.chat.id, replys.get("ielts2"), reply_markup=delete)
        bot.register_next_step_handler(message, country)
        
# страна
def country(message):
    global have_ielts
    have_ielts = message.text # есть айлз?
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(buttons.get('america'), buttons.get('europe')) 
    bot.send_message(message.chat.id, replys.get('country'), reply_markup=btn)
    bot.register_next_step_handler(message, contact1)
    
# получение контакта пользователя 
def contact1(message):
    global countryy
    if message.text.lower() not in ['америка', 'европа', 'evropa', 'america']:  #полученный текст преобразуется в нижний регистер и проходит проверку
        bot.send_message(message.chat.id, replys.get('none'))
        country(message)
        
    else:
        countryy = message.text # куда ты хочеш?
        btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text=buttons.get('share'), request_contact=True))
        bot.send_message(message.chat.id, replys.get('contact'), reply_markup=btn)
        bot.register_next_step_handler(message, conv_end)

#пасибо за ответ
def conv_end(message):
    global grade, have_ielts, countryy, contact
    if message.content_type == "contact":
        contact = str(message.contact.phone_number)
    else:
        contact = message.text #номер пользователя
        
    
    
    conn = sqlite3.connect('db_client.sql')
    cursor = conn.cursor()
  
    
    #добавление в базу данных информацию о пользователях
    cursor.execute("INSERT INTO Users (grade, have_ielts, country, contact) VALUES ('%s', '%s', '%s', '%s')" % (grade, have_ielts, countryy, contact))
    conn.commit()
    cursor.close()
    conn.close()

    
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, replys.get("thanks"), reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('db_client.sql')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    
    #вывод списка пользователей
    info = ''
    for el in users:
        info += f" ID : {el[0]},\n Класс :{el[1]},\nIelts : {el[2]},\nСтрана : {el[3]},\nКонтакт : {el[4]} " #вывод списка пользователей
        print(info)
    
    cursor.close()
    conn.close()
    
    bot.send_message(call.message.chat.id, info)


bot.infinity_polling()


