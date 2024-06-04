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
             " Если хотите связаться с нами, позвоните по номеру +998908260440",
    "what": "Какими из наших услуг вы хотите воспользоваться?",

    "answer1": "Полное Сопровождение",
    "answer2": "1-месячные курсы",
    "answer3": "Хочу записаться на 1-часовую консультацию специалиста",

    "month1": "Scholarship Bootcamp",
    "month2": "Research Bootcamp",
    "month3": "Activities Bootcamp",

    "call1": "В ближайщее время наш менеджер позвнит вам на счет уточнения времени консультации",
    "cources": 'Выберите курс',

    "consulting": "В консультацию входит :\n\n"
                  "✅ Оценка ваших шансов на поступление;\n"
                  "✅ Ваши следующие шаги для получения грантов;\n"
                  "✅ Определим ваше направление;\n"
                  "✅ Ответим на все ваши вопросы;\n"
                  "✅ В конце консультации мы ознакомим вас нашими тарифами на полное сопровождение.\n"
                  "🧑‍💻 Консультация проводится онлайн или оффлайн в офисе.\n"
                  "⏰ Длительность 60мин",

    "consulting2": "Magistraturaga top 100 AQSh universitetlariga kirish uchun kurs birinchi marotaba o’zbek tilida! \n"
                   "Ushbu kursda siz quyidagilarni o’rganasiz:\n"
                   "1 Universitetlar ro’yhatini to’gri tuzish\n"
                   "2 Shaxsiy brend ustida ishlash \n"
                   "3 Statement of Purpose tuzish \n"
                   "4 Rezume AQSh tizimi bo’yicha tuzish \n"
                   "5 Email yozishni organish (Chat GPTsiz) \n"
                   "6 Graduate assistantship programmalarga topshirishni organish \n"
                   "7 Research Proposal yozish \n"
                   "8 Application fee waiver olish \n"
                   "9 Visa jarayoniga tayyorlanish\n"
                   "10 Pre-arrival jarayoni\n"
                   "Ushbu kurs orqali siz magistraturaga kirish uchun universitetlardan to’liq grant olishni"
                   " o’rganasiz\n"
                   "Ushbu kurs yordamida bizning studentlarimiz shu kungacha Carnegie Mellon, Boston University, "
                   "PennState\n"
                   " va shunga o’xshagan top Universitetlarga kirishgan.\n\n"
                   "Darslar online tarzda zoom orqali live olib boriladi. \nNarxi 7,500,000 so’m",

    "consulting3": "AQSh universitetlariga topshirishingiz uchun sizda 15 ta har xil yutuqlar bo’lishi kerakligini "
                   "bilarmidingiz?\n"
                   "Birinchi marta kompaniyamiz tarixida ushbu kursni siz uchun taqdim qilishga qaror qildik.\n\n\n"
                   "Top #10 universitetlar uchun Shaxsiy brendni rivojlantirish kursi! Ushbu kursda siz 14 kun davomida"
                   ":\n"
                   "✅ Volonyerstvalar\n"
                   "✅ Ijtimoiy proektlar\n"
                   "✅ Konferensiyalar\n"
                   "✅ Online kurslar\n"
                   "✅ Olimpiadalar\n"
                   "✅ Summer Camplar\n"
                   "Va eng asosiysi ...\n"
                   "⏰ Passion Project tuzish bo’yicha to’liq resurslar va yo’nalishlar olasiz.\n"
                   "Ushbu kurs super intensive kurs bo’ladi va siz bizning to’liq mentorlikda studentlarimiz nimalar "
                   "bilan shug’ullanishini 1 oy davomida kuzatasiz.\n"
                   "Kurs narxi 1,500,000 so’m\n"
                   "Darslar online tarzda zoom orqali live olib boriladi.",
}
button1: dict = {
    "yes": KeyboardButton(text='Да'),
    "no": KeyboardButton(text='Нет'),
    "sch": KeyboardButton(text='Школьник'),
    "uni": KeyboardButton(text='Студент'),
    "preparing": KeyboardButton(text='Готовлюсь'),
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

    "func1": KeyboardButton(text="Полное Сопровождение"),
    "func2": KeyboardButton(text="1-месячные курсы"),
    "func3": KeyboardButton(text="Хочу записаться на 1-часовую консультацию специалиста"),

    "funcmonth1": KeyboardButton(text="Scholarship Bootcamp"),
    "funcmonth2": KeyboardButton(text="Research Bootcamp"),
    "funcmonth3": KeyboardButton(text="Activities Bootcamp"),
}
