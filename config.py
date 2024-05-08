import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

token = '6242109060:AAFtW5ckwhwUyEbqIQh3auxa6UTzVNrBLMY'
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

grade = None
have_ielts = None
countryy = None
contact = None


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
    bot.send_message(message.chat.id,
                     replys.get('grade'))  # вот тут вот запрос на то в каком классе либо курсе учится клиент
    bot.register_next_step_handler(message, ielts)


# функция выводит информацию о уровне английского пользователя
def ielts(message):
    global grade

    info.update({"статус": message.text})  # школьник ? студент ? )))

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
                                   f"Айлз: {info['айлз']}\n"
                                   f"Страна: {info['страна']}\n"
                                   f"Номер: {info['номер']}\n")

    else:
        info.update({"номер": message.text})
        bot.send_message(message.chat.id, replys['thanks'], reply_markup=delete)
        bot.send_message(group_id, f"Имя: {info['name']}\n"
                                   f"Язык: {info['язык']}\n"
                                   f"Статус: {info['статус']}\n"
                                   f"Айлз: {info['айлз']}\n"
                                   f"Страна: {info['страна']}\n"
                                   f"Номер: {info['номер']}\n")


bot.infinity_polling()
