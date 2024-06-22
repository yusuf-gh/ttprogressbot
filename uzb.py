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
    "greeting": "Assalomu aleykum. Siz bilan aloqaga chiqishimiz uchun ushbu savollarga javob bering!",
    "country": "Qaysi Davlatga topshirmoqchisiz?",
    "intro": "Javoblaringiz uchun rahmat. Biz siz bilan tez orada aloqaga chiqamiz. "
             "Biz bilan aloqaga chiqish uchun ushbu raqamga qo’ng’iroq qiling: \n+998908260440 \n+998908264004",
    "what": "Qaysi xizmatimizdan foydalanmoqchisiz?",

    "answer1": "To’liq mentorlik xizmati",
    "answer2": "1 oylik kurslar",
    "answer3": "1 soatlik ekspert Konsultatsiyaga yozilmoqchiman",

    "month1": "Scholarship Bootcamp",
    "month2": "Research Bootcamp",
    "month3": "Activities Bootcamp",

    "call1": "Menejerimiz konsultatsiya vaqtini tasdiqlash uchun qisqa vaqt ichida sizga qo'ng'iroq qiladi",
    "cources": 'Kursni tanlang',


    "consulting": "Konsultatsiya quyidagilarni o'z ichiga oladi:\n\n"
                  "✅ Qabul qilish imkoniyatini baholash;\n"
                  "✅ Grant olish uchun keyingi qadamlaringiz;\n"
                  "✅ Yo'nalishingizni biz aniqlaymiz;\n"
                  "✅ Barcha savollaringizga javob beramiz;\n"
                  "✅ Maslahat yakunida biz sizni toʻliq mentorlik uchun tariflarimiz bilan tanishtiramiz.\n"
                  "🧑‍💻 Konsultatsiya onlayn yoki oflayn rejimda ofisda olib boriladi.\n"
                  "⏰ Davomiyligi 60 min",

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
                   "Darslar online tarzda zoom orqali live olib boriladi.",

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
                   "Darslar online tarzda zoom orqali live olib boriladi.",
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
    "english4": KeyboardButton(text='IELTSga tayyorlanayabman'),

    "country1": KeyboardButton(text='USA'),
    "country2": KeyboardButton(text='Canada'),
    "country3": KeyboardButton(text='UK'),
    "country4": KeyboardButton(text='Germany'),
    "country5": KeyboardButton(text='Italy'),
    "country6": KeyboardButton(text='Turkiye'),

    "func1": KeyboardButton(text="To’liq mentorlik xizmati"),
    "func2": KeyboardButton(text="1 oylik kurslar"),
    "func3": KeyboardButton(text="1 soatlik ekspert Konsultatsiyaga yozilmoqchiman"),

    "funcmonth1": KeyboardButton(text="Scholarship Bootcamp"),
    "funcmonth2": KeyboardButton(text="Research Bootcamp"),
    "funcmonth3": KeyboardButton(text="Activities Bootcamp"),

    'back': KeyboardButton(text="Вернуться к услугам")
}
