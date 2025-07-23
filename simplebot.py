# Бот на Аiogram
#
from turtledemo.penrose import start

token='8021793572:AAHgJru99rMWEVLeHSq_aFx4WDvtQFhMwfM'

import telebot
from telebot import types
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Я запущен и буду повторять за Вами')

@bot.message_handler(content_types=['text'])
def parrot(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling(none_stop=True)
