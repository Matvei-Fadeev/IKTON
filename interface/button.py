import telebot
from queue_bot_token import bot_token
from telebot import types


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def welcome_start(message):
	bot.send_message(message.chat.id, 'welcome_start')

def welcome_help(message):
	bot.send_message(message.chat.id, 'welcome_help')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	# Here is button realization

def start(message):
	if message.text == '/reg':
		bot.send_message(message.from_user.id, "Как тебя зовут?")
		bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
		bot.register_next_step_handler(message, getsurname)
	else:
		bot.send_message(message.from_user.id, 'Напиши /reg')

bot.polling(none_stop=True, interval=0)
