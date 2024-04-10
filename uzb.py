from telebot.types import KeyboardButton, ReplyKeyboardMarkup

reply1 : dict = {
    "none": "Kechirasiz xato yuz berdi, iltimos, taqdim etilgan javob variantlaridan birini tanlang",
    "greeting": "Assalomu aleykum!😊\nOzingiz xaqida ma'lumot bersangiz, siz bilan tez orada bog'lanamiz!",
    "grade": "Kaysi sinif/kursda oqisiz?",
    "ielts": "IELTS sertifikatingiz bormi?",
    "ielts2": "Iltimos, IELTS-ni «5.7» formatida kiriting",
    "country": "Qaysi davlatga topshimoqchisiz?",
    "contact": "Raqamingizni qoldiring",
    "thanks": "Javobingiz uchun rahmat."
}
button1 : dict = {
    "yes": KeyboardButton(text='Ha'),
    "no": KeyboardButton(text='Yoq'),
    "preparing":KeyboardButton(text='Tayorlanyapman'),
    "europe": KeyboardButton(text='Evropa'),
    "america": KeyboardButton(text='America'),
    "share": 'Raqamni yuborish',
}
