import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import re

token = '6782654814:AAGPAO6tqJHaETbVJynAki5mzEssLRzjr0I'
bot = telebot.TeleBot(token)
delete = ReplyKeyboardRemove()
group_id = "-1002075066553"
info = dict({})

replys: dict = {}
buttons: dict = {}

language = {
    'uz': KeyboardButton(text="O'zbek tili"),
    'ru': KeyboardButton(text="Русский язык"),

}


# Приветствие
@bot.message_handler(commands=["start"])
def choose_lang(message):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(language['uz'], language['ru'])

    bot.send_message(message.chat.id, "Выберите язык\nTilni tanlang", reply_markup=btn)


# Функция определет язык Рус./Uzb.
@bot.message_handler(content_types=["text"])
def answer(message):
    global replys, buttons, language

    if message.text == "O'zbek tili":
        from uzb import reply1 as uzb_replay
        from uzb import button1 as uzb_button
        # импорт текстов на узбекском
        replys.update(uzb_replay)
        buttons.update(uzb_button)
        info.update({"язык": "O'zbek tili"})

    elif message.text == "Русский язык":
        from rus import reply1 as rus_reply
        from rus import button1 as rus_button
        # импорт текстов на русском
        replys.update(rus_reply)
        buttons.update(rus_button)
        info.update({"язык": "Русский язык"})

    else:
        bot.send_message(message.chat.id,
                         "Что то пошло не так, пожалуйста выберите предоставленный вариант "
                         "ответа.\nKechirasiz xato yuz berdi, iltimos, taqdim etilgan javob "
                         "variantlaridan birini tanlang.")
        return

    bot.send_message(message.chat.id, replys.get('greeting'), reply_markup=delete)
    name_get = bot.send_message(message.chat.id, replys.get('name'))
    bot.register_next_step_handler(name_get, get_name_func)


def get_name_func(message):
    info.update({"name": message.text})
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(buttons.get("sch"), buttons.get("uni"))
    bot.send_message(message.chat.id,
                     replys.get('grade'),
                     reply_markup=btn)  # вот тут вот запрос на то в каком классе либо курсе учится клиент
    bot.register_next_step_handler(message, grade_1)


# студент либо школьник
def grade_1(message):
    if message.text == replys.get("uni"):
        info.update({"статус": message.text})
        bot.send_message(message.chat.id, replys.get("uni2"), reply_markup=delete)
        bot.register_next_step_handler(message, ielts)


    elif message.text == replys.get("sch"):
        info.update({"статус": message.text})
        bot.send_message(message.chat.id, replys.get("sch2"), reply_markup=delete)
        bot.register_next_step_handler(message, ielts)

    else:
        bot.send_message(message.chat.id,
                         "Что то пошло не так, пожалуйста выберите предоставленный вариант "
                         "ответа.\nKechirasiz xato yuz berdi, iltimos, taqdim etilgan javob "
                         "variantlaridan birini tanlang.")
        return


# функция выводит информацию о уровне английского пользователя
def ielts(message):
    info.update({"класс/курс": message.text})

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

    info.update({"айлз": message.text})  # есть айлз?
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(buttons.get('america'), buttons.get('europe'))
    bot.send_message(message.chat.id, replys.get('country'), reply_markup=btn)
    bot.register_next_step_handler(message, contact1)


# получение контакта пользователя 
def contact1(message):
    global countryy
    if message.text.lower() not in ['америка', 'европа', 'evropa',
                                    'america']:  # полученный текст преобразуется в нижний регистер и проходит проверку
        bot.send_message(message.chat.id, replys.get('none'))
        country(message)

    else:

        info.update({"страна": message.text})  # куда ты хочешь?
        btn = ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton(text=buttons.get('share'), request_contact=True))
        bot.send_message(message.chat.id, replys.get('contact'), reply_markup=btn)
        bot.register_next_step_handler(message, conv_end)


# пасибо за ответ
def conv_end(message):
    global grade, have_ielts, countryy, contact
    if message.content_type == "contact":
        info.update({"номер": str(message.contact.phone_number)})
        bot.send_message(message.chat.id, replys['thanks'], reply_markup=delete)
        bot.send_message(group_id, f"Имя: {info['name']}\n"
                                   f"Язык: {info['язык']}\n"
                                   f"Статус: {info['статус']}\n"
                                   f"Класс/Курс:{info['класс/курс']}\n"
                                   f"Айлз: {info['айлз']}\n"
                                   f"Страна: {info['страна']}\n"
                                   f"Номер: {info['номер']}\n")

    else:
        if len(message.text) == 12 and re.match(r'^(998)[\d]{9}$', message.text):
            info.update({
                'номер': int(message.text)
            })
            bot.send_message(message.chat.id, replys['thanks'], reply_markup=delete)
            bot.send_message(group_id, f"Имя: {info['name']}\n"
                                       f"Язык: {info['язык']}\n"
                                       f"Статус: {info['статус']}\n"
                                       f"Класс/Курс:{info['класс/курс']}\n"
                                       f"Айлз: {info['айлз']}\n"
                                       f"Страна: {info['страна']}\n"
                                       f"Номер: {info['номер']}\n")
        else:
            btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text=buttons.get('share'),
                                                                               request_contact=True))
            phone = bot.send_message(message.chat.id, replys["alert"], reply_markup=btn)
            bot.register_next_step_handler(phone, conv_end)


bot.infinity_polling()
