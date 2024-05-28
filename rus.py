from telebot.types import KeyboardButton, ReplyKeyboardMarkup

reply1: dict = {
    "none": "Что то пошло не так, пожалуйста выберите предоставленный вариант ответа",
    "grade": "Какая у вас степень образования?",
    "sch": "Школьник",
    "uni": "Студент",
    "alert": "Упс, что-то пошло не так. Пожалуйста, проверь указанный номер и повтори попытку😊",
    "sch2": "Напишите в каком вы классе или курсе вы учитесь?",


    "ielts2": "Пожалуйста введите свой IELTS в формате «5.7»",

    "contact": "Отлично, а теперь введи свой номер телефона. Это можно сделать, "
               "используя кнопку внизу, либо отправить сообщение в формате  998ХХХХХХХХХ",
    "thanks": "Благодарим за ответ.",



    "ielts": "Ваш уровень английского?",
    "name": "Введите свое имя",
    "greeting": "Здравствуйте! Ответьте на эти вопросы, чтобы мы могли связаться с вами",
    "country": "В какую страну вы бы хотели поступить?",
    "intro": "Спасибо за ваши ответы. Мы свяжемся с вами в ближайшее время."
             " Если хотите связаться с нами, позвоните по номеру +998908260440"
}
button1: dict = {
    "yes": KeyboardButton(text='Да'),
    "no": KeyboardButton(text='Нет'),
    "sch": KeyboardButton(text='Школьник'),
    "uni": KeyboardButton(text='Студент'),
    "preparing":KeyboardButton(text='Готовлюсь'),
    "europe": KeyboardButton(text='Европа'),
    "america": KeyboardButton(text='Америка'),
    "share": 'Отправить контакт',

    "english1": KeyboardButton(text='Я не знаю английского'),
    "english2": KeyboardButton(text='A1-B2/средний/IELTS 5,5-6,5'),
    "english3": KeyboardButton(text='C1-C2/продвинутый уровень/IELTS 7.0-9.0'),
    "english4": KeyboardButton(text='Я готовлюсь к IELTS'),

    "country1": KeyboardButton(text='США'),
    "country2": KeyboardButton(text='Канада'),
    "country3": KeyboardButton(text='Великобритания'),
    "country4": KeyboardButton(text='Германия'),
    "country5": KeyboardButton(text='Италия'),
    "country6": KeyboardButton(text='Турция'),
}
