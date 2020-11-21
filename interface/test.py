import telebot
from queue_bot_token import bot_token
from telebot import types


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def welcome_start(message):
	bot.send_message(message.chat.id, 'Добрый день, User.')

def welcome_help(message):
	bot.send_message(message.chat.id, 'Как тебе помочь?')


name = ''
surname = ''
age = 0

def get_surname(message):
	bot.send_message(message.from_user.id, 'Назови свою фамилию.')
	global surname
	surname = message.text

def get_name(message):
	bot.send_message(message.from_user.id, "Как тебя зовут?")
	global name
	name = message.text


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "Начать очередь":
		keyboard = types.InLineKeyboardMarkup()
		key_list = types.InLineKeyboardButton(text="Создание списка", callback_data="list_set")
		keyboard.add(key_list)
		options = "Возможные действия:"
		bot.send_message(message.from_user.id, text=options, reply_markup=keyboard)
	elif message.text == '/reg':
		bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
	else:
		bot.send_message(message.from_user.id, "Напиши /help.")

def start(message):
	if message.text == '/reg':
		bot.send_message(message.from_user.id, "Как тебя зовут?")
		bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
		bot.register_next_step_handler(message, getsurname)
	else:
		bot.send_message(message.from_user.id, 'Напиши /reg')

bot.polling(none_stop=True, interval=0)
