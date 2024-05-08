from telebot.types import KeyboardButton, ReplyKeyboardMarkup

reply1 : dict = {
    "name": "Продолжим, отправь своё имя:",
    "none": "Что то пошло не так, пожалуйста выберите предоставленный вариант ответа",
    "greeting": "Здравствуйте!😊\nОставьте пожалуйста краткую информацию о себе и в скором времени мы с вами свяжемся!",
    "grade": "В каком классе/курсе учитесь?",
    "ielts": "Имеется ли у вас IELTS сертификат?",
    "ielts2": "Пожалуйста введите свой IELTS в формате «5.7»",
    "country": "Выберите страну в которую хотите подать",
    "contact": "Отлично, а теперь введи свой номер телефона. Это можно сделать, "
               "используя кнопку внизу, либо отправить сообщение в формате  998ХХХХХХХХХ",
    "thanks": "Благодарим за ответ."
}
button1 : dict = {
    "yes": KeyboardButton(text='Да'),
    "no": KeyboardButton(text='Нет'),
    "preparing":KeyboardButton(text='Готовлюсь'),
    "europe": KeyboardButton(text='Европа'),
    "america": KeyboardButton(text='Америка'),
    "share": 'Отправить контакт',
}
