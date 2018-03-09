# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	bot.send_message(message.chat.id, message.text)
	print config.name
	markup = types.ReplyKeyboardMarkup()
	markup.row('a', 'v')
	markup.row('c', 'd', 'e')
	bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)