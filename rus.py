from telebot.types import KeyboardButton, ReplyKeyboardMarkup

reply1 : dict = {
    "none": "Что то пошло не так, пожалуйста выберите предоставленный вариант ответа",
    "greeting": "Здравствуйте!😊\nОставьте пожалуйста краткую информацию о себе и в скором времени мы с вами свяжемся!",
    "grade": "В каком классе/курсе учитесь?",
    "ielts": "Имеется ли у вас IELTS сертификат?",
    "ielts2": "Пожалуйста введите свой IELTS в формате «5.7»",
    "country": "Выберите страну в которую хотите подать",
    "contact": "Отправьте свой контакт",
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
