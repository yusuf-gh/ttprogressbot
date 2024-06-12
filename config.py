import os

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import re
import requests

token = '6242109060:AAGzAu-Cqt8nDa30SOoTLNCHTKLoqd4NprI'
backend = "http://127.0.0.1:8000/"
bot = telebot.TeleBot(token)
delete = ReplyKeyboardRemove()
group_id = "-1002075066553"
info = dict({})
info_post = {
        "id": 0,
        "username": None,
        "language": 0
    }

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
    info_post.update({"id": message.chat.id})

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
        info_post.update({"language": 1})

    elif message.text == "Русский язык":
        from rus import reply1 as rus_reply
        from rus import button1 as rus_button
        # импорт текстов на русском
        replys.update(rus_reply)
        buttons.update(rus_button)
        info.update({"язык": "Русский язык"})
        info_post.update({"language": 2})

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
    info_post.update({"username": message.text})
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(buttons['english1'], buttons['english2'],
                                                                     buttons['english3'],
                                                                     buttons['english4'])
    bot.send_message(message.chat.id, replys.get('ielts'), reply_markup=btn)
    a = requests.post(f"{backend}users", json=info_post)
    bot.register_next_step_handler(message, ielts)


def ielts(message):
    info.update({"english": message.text})
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(buttons["country1"], buttons["country2"],
                                                                     buttons["country3"],
                                                                     buttons["country4"], buttons["country5"],
                                                                     buttons["country6"])

    bot.send_message(message.chat.id, replys.get("country"), reply_markup=btn)
    bot.register_next_step_handler(message, country)


def country(message):
    info.update({"country": message.text})
    btn = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(text=buttons.get('share'), request_contact=True))
    bot.send_message(message.chat.id, replys.get('contact'), reply_markup=btn)
    bot.register_next_step_handler(message, conv_end)


def conv_end(message):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(buttons['func1'], buttons['func2'],
                                                                     buttons['func3'])
    if message.content_type == "contact":
        info.update({"номер": str(message.contact.phone_number)})
        bot.send_message(message.chat.id, replys['intro'], reply_markup=delete)
        # bot.send_message(group_id, f"Имя: {info['name']}\n"
        #                            f"Язык: {info['язык']}\n"
        #                            f"IELTS: {info['english']}\n"
        #                            f"Страна: {info['country']}\n"
        #                            f"Номер: {info['номер']}\n")
        a = bot.send_message(message.chat.id, replys['what'], reply_markup=btn)
        bot.register_next_step_handler(a, function)

    else:
        if len(message.text) == 12 and re.match(r'^(998)[\d]{9}$', message.text):
            info.update({
                'номер': int(message.text)
            })
            bot.send_message(message.chat.id, replys['intro'], reply_markup=delete)
            # bot.send_message(group_id, f"Имя: {info['name']}\n"
            #                            f"Язык: {info['язык']}\n"
            #                            f"IELTS: {info['english']}\n"
            #                            f"Страна: {info['country']}\n"
            #                            f"Номер: {info['номер']}\n")
            a = bot.send_message(message.chat.id, replys['what'], reply_markup=btn)
            bot.register_next_step_handler(a, function)
        else:
            btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text=buttons.get('share'),
                                                                               request_contact=True))
            phone = bot.send_message(message.chat.id, replys["alert"], reply_markup=btn)
            bot.register_next_step_handler(phone, conv_end)


def function(message):
    if message.text == replys['answer1']:
        if info['язык'] == "O'zbek tili":
            response_get_webinar = requests.get(f"{backend}data/uzb/").json()

        else:
            response_get_webinar = requests.get(f"{backend}data/rus/").json()

        try:

            pdf_url = response_get_webinar[0]['date']

            if pdf_url:
                response = requests.get(pdf_url)

                if response.status_code == 200:
                    file_path = 'prosal.pdf'
                    with open(file_path, 'wb') as f:
                        f.write(response.content)

                    with open(file_path, 'rb') as f:
                        bot.send_document(message.chat.id, f, reply_markup=ReplyKeyboardRemove())
                        os.remove(file_path)


            else:
                bot.send_message(message.chat.id, "PDF файл не найден в ответе сервера.")

        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")

        bot.send_message(message.chat.id, replys['call1'])
        # bot.send_message(group_id, f"Имя: {info['name']}\n"
        #                            f"Язык: {info['язык']}\n"
        #                            f"IELTS: {info['english']}\n"
        #                            f"Страна: {info['country']}\n"
        #                            f"Номер: {info['номер']}\n"
        #                            f"\n выбрал услугу [Полное сопровождение]")

    elif message.text == replys['answer2']:
        btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(buttons['funcmonth1'],
                                                                         buttons['funcmonth2'], buttons['funcmonth3'])
        a = bot.send_message(message.chat.id, replys['cources'], reply_markup=btn)
        bot.register_next_step_handler(a, one_month)

    elif message.text == replys['answer3']:
        bot.send_message(message.chat.id, replys['consulting'], reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id, replys['call1'])
        # bot.send_message(group_id, f"Имя: {info['name']}\n"
        #                            f"Язык: {info['язык']}\n"
        #                            f"IELTS: {info['english']}\n"
        #                            f"Страна: {info['country']}\n"
        #                            f"Номер: {info['номер']}\n"
        #                            f"\n выбрал услугу [Хочу записаться на 1-часовую консультацию специалиста]")


def one_month(message):
    if message.text == replys['month1']:
        bot.send_message(message.chat.id, replys['consulting2'], reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id, replys['call1'])
        # bot.send_message(group_id, f"Имя: {info['name']}\n"
        #                            f"Язык: {info['язык']}\n"
        #                            f"IELTS: {info['english']}\n"
        #                            f"Страна: {info['country']}\n"
        #                            f"Номер: {info['номер']}\n"
        #                            f"\n выбрал услугу [1-месячные курсы {replys['month1']}]")

    elif message.text == replys['month2']:
        bot.send_message(message.chat.id, replys['consulting3'], reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id, replys['call1'])
        # bot.send_message(group_id, f"Имя: {info['name']}\n"
        #                            f"Язык: {info['язык']}\n"
        #                            f"IELTS: {info['english']}\n"
        #                            f"Страна: {info['country']}\n"
        #                            f"Номер: {info['номер']}\n"
        #                            f"\n выбрал услугу [1-месячные курсы {replys['month2']}]")

    elif message.text == replys['month3']:
        bot.send_message(message.chat.id, replys['consulting2'], reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id, replys['call1'])
        # bot.send_message(group_id, f"Имя: {info['name']}\n"
        #                            f"Язык: {info['язык']}\n"
        #                            f"IELTS: {info['english']}\n"
        #                            f"Страна: {info['country']}\n"
        #                            f"Номер: {info['номер']}\n"
        #                            f"\n выбрал услугу [1-месячные курсы {replys['month3']}]")


bot.infinity_polling()
