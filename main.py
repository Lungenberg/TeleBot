import telebot
import random
from telebot import types
bot = telebot.TeleBot("5887260814:AAGRMeQwwq-HEoKYBmC0kgDSAfZijdl_tzw")
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Random Number")
    item2 = types.KeyboardButton("How are you?")
    item3 = types.KeyboardButton("phones")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Welcome, {0.first_name}! \n I am - <b>{1.first_name}</b>, "
                     "Я бот оладушек.".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def dialogue(message):
    if message.chat.type == 'private':
        if message.text == 'Random Number':
            bot.send_message(message.chat.id, str(random.randint(0, 1000)))
        elif message.text == "How are you?":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Good", callback_data='good')
            item2 = types.InlineKeyboardButton("Bad", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Nice, you?', reply_markup=markup)
        elif message.text == "phones":
            from Lesson2 import scrape_data
            phones = scrape_data()
            bot.send_message(message.chat.id, random.choice(phones))
        else:
            bot.send_message(message.chat.id, "Error")

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "good":
                bot.send_message(call.message.id, 'Nice')
            elif call.data == 'bad':
                bot.send_message(call.message.id, 'Ok')
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="How are you?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=True,
                                      text="Test Alert")
    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)








