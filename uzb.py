from telebot.types import KeyboardButton, ReplyKeyboardMarkup

reply1: dict = {

    "none": "Kechirasiz xato yuz berdi, iltimos, taqdim etilgan javob variantlaridan birini tanlang",

    "grade": "Sizning ta'lim darajangiz qanday?",
    "sch": "Maktab o'quvchisi",
    "alert": "Nimadir hato ketdi. Katta ehtimol bilan raqam noto'g'ri. Iltimos, "
             "raqamni tekshiring va qayta urinib ko'ring😊",
    "uni": "Student",
    "sch2": "Qaysi sinfda yoki kursda o'qiyotganingizni yozing?",

    "ielts2": "Iltimos, IELTS-ni «5.7» formatida kiriting",
    "contact": "Super, endi telefon raqamingizni kiriting. "
               "Buni pastdagi tugma yordamida amalga oshirish mumkin yoki 998XXXXXXXX formatida habar yuboring",


    "ielts": "Ingliz tili bilish darajangiz?",
    "name": "Ismingizni Yozing",
    "greeting": "Assalomaleykum. Siz bilan aloqaga chiqishimiz uchun ushbu savollarga javob bering!",
    "country": "Qaysi Davlatga topshirmoqchisiz?",
    "intro": "Javoblaringiz uchun rahmat. Biz siz bilan tez orada aloqaga chiqamiz. "
             "Biz bilan aloqaga chiqish uchun ushbu raqamga qo’ng’iroq qiling +998908260440",
    "what": "Qaysi xizmatimizdan foydalanmoqchisiz?",

    "answer1": "To’liq mentorlik xizmati",
    "answer2": "Scholarship Bootcamp",
    "answer3": "Research Bootcamp",
    "answer4": "Activities Bootcamp",
    "answer5": "1 soatlik ekspert Konsultatsiyaga yozilmoqchiman",
}
button1: dict = {
    "yes": KeyboardButton(text='Ha'),
    "no": KeyboardButton(text='Yoq'),
    "sch": KeyboardButton(text="Maktab o'quvchisi"),
    "uni": KeyboardButton(text='Student'),
    "preparing": KeyboardButton(text='Tayorlanyapman'),
    "europe": KeyboardButton(text='Evropa'),
    "america": KeyboardButton(text='America'),
    "share": 'Raqamni yuborish',

    "english1": KeyboardButton(text='Ingliz tilini bilmayman'),
    "english2": KeyboardButton(text='A1-B2/Intermediate/IELTS 5.5-6.5'),
    "english3": KeyboardButton(text='C1-C2/Advanced/IELTS 7.0-9.0'),
    "english4": KeyboardButton(text='IELTSga tayyorlanayapman'),

    "country1": KeyboardButton(text='USA'),
    "country2": KeyboardButton(text='Canada'),
    "country3": KeyboardButton(text='UK'),
    "country4": KeyboardButton(text='Germany'),
    "country5": KeyboardButton(text='Italy'),
    "country6": KeyboardButton(text='Turkiye'),

    "func1": KeyboardButton(text="To’liq mentorlik xizmati"),
    "func2": KeyboardButton(text="Scholarship Bootcamp"),
    "func3": KeyboardButton(text="Research Bootcamp"),
    "func4": KeyboardButton(text="Activities Bootcamp"),
    "func5": KeyboardButton(text="1 soatlik ekspert Konsultatsiyaga yozilmoqchiman")
}
