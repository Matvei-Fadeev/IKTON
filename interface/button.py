import telebot
from queue_bot_token import bot_token
from telebot import types


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def welcome_start(message):
	bot.send_message(message.chat.id, 'welcome_start')

@bot.message_handler(commands=['help'])
def welcome_help(message):
	bot.send_message(message.chat.id, 'welcome_help')

@bot.message_handler(commands=['button'])
def get_button(message):
	bot.send_message(message.chat.id, 'Button')
    ## Button here


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	# Here is button realization
    bot.send_message(message.chat.id, 'get_text_messages')


bot.polling(none_stop=True, interval=0)
