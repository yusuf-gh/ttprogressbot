import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

token = '6349297067:AAHSS3iLXO_wgbKPhyusQ0xCO9ckdV5pwEs'
bot = telebot.TeleBot(token)
delete = ReplyKeyboardRemove()

# главные словари
replys: dict = {} 
buttons: dict = {}

language = {
    'uz': KeyboardButton(text="O'zbek tili"),
    'ru': KeyboardButton(text="Русский язык"),
    
}


#Приветствие
@bot.message_handler(commands=["start"])
def choose_lang(message):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(language['uz'], language['ru'])
    
    bot.send_message(message.chat.id, "Выберите язык\nTilni tanlang", reply_markup=btn)
    
    
#Функция определет язык Рус./Uzb.
@bot.message_handler(content_types=["text"])
def answer(message):
    global replys, buttons, language
    
    if message.text == "O'zbek tili":
        from uzb import reply1 as uzb_replay
        from uzb import button1 as uzb_button
        # импорт текстов на узбекском
        replys.update(uzb_replay)
        buttons.update(uzb_button)
            
    elif message.text == "Русский язык":
        from rus import reply1 as rus_reply
        from rus import button1 as rus_button
        # импорт текстов на русском
        replys.update(rus_reply)
        buttons.update(rus_button)
        
    else:
        bot.send_message(message.chat.id, "Что то пошло не так, пожалуйста выберите предоставленный вариант ответа.\nKechirasiz xato yuz berdi, iltimos, taqdim etilgan javob variantlaridan birini tanlang.")
        return      
    
    bot.send_message(message.chat.id, replys.get('greeting'), reply_markup=delete)
    bot.send_message(message.chat.id, replys.get('grade'))
    bot.register_next_step_handler(message, ielts)

# функция получает информацию о уровне английского пользователя 
def ielts(message):
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
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(buttons.get('america'), buttons.get('europe')) 
    bot.send_message(message.chat.id, replys.get('country'), reply_markup=btn)
    bot.register_next_step_handler(message, contact1)
    
# получение контакта пользователя 
def contact1(message):
    if message.text.lower() not in ['америка', 'европа', 'evropa', 'america']:  #полученный текст преобразуется в нижний регистер и проходит проверку
        bot.send_message(message.chat.id, replys.get('none'))
        country(message)
        
    else:
        btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text=buttons.get('share'), request_contact=True))
        bot.send_message(message.chat.id, replys.get('contact'), reply_markup=btn)
        bot.register_next_step_handler(message, conv_end)

#пасибо за ответ
def conv_end(message):
    bot.send_message(message.chat.id, replys.get("thanks"), reply_markup=delete)



bot.infinity_polling()