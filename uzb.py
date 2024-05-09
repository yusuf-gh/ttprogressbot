from telebot.types import KeyboardButton, ReplyKeyboardMarkup

reply1 : dict = {
    "name": "Davom etamiz, ismingizni kiriting",
    "none": "Kechirasiz xato yuz berdi, iltimos, taqdim etilgan javob variantlaridan birini tanlang",
    "greeting": "Assalomu aleykum!😊\nOzingiz xaqida ma'lumot bersangiz, siz bilan tez orada bog'lanamiz!",
    "grade": "Maktab o'quvchisi? Student?",
    "sch": "Maktab o'quvchisi",
    "alert": "Nimadir hato ketdi. Katta ehtimol bilan raqam noto'g'ri. Iltimos, "
             "raqamni tekshiring va qayta urinib ko'ring😊",
    "uni": "Student",
    "sch2": "Nechinchi sinifdasiz?",
    "uni2": "Nechinchi kursdasiz?",
    "ielts": "IELTS sertifikatingiz bormi?",
    "ielts2": "Iltimos, IELTS-ni «5.7» formatida kiriting",
    "country": "Qaysi davlatga topshimoqchisiz?",
    "contact": "Super, endi telefon raqamingizni kiriting. "
               "Buni pastdagi tugma yordamida amalga oshirish mumkin yoki 998XXXXXXXX formatida habar yuboring",
    "thanks": "Javobingiz uchun rahmat."
}
button1 : dict = {
    "yes": KeyboardButton(text='Ha'),
    "no": KeyboardButton(text='Yoq'),
    "sch": KeyboardButton(text="Maktab o'quvchisi"),
    "uni": KeyboardButton(text='Student'),
    "preparing":KeyboardButton(text='Tayorlanyapman'),
    "europe": KeyboardButton(text='Evropa'),
    "america": KeyboardButton(text='America'),
    "share": 'Raqamni yuborish',
}
