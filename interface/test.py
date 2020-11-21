import telebot
bot = telebot.TeleBot('1465761077:AAF1MCjRHGKLO9PLwZ76opefreE2btD9bIw')


@bot.message_handler(commands=['start', 'help'])
def welcome_start(message):
	bot.send_message(message.chat.id, 'Добрый день, User.')

def welcome_help(message):
	bot.send_message(message.chat.id, 'Как тебе помочь?')


name = ''
surname = ''
age = 0

def get_name(message):
	global name
	name = message.text
	bot.send_message(message.from_user.id, 'Назови свою фамилию.')
	bot.register_next_step_handler(message, getsurname)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "Начать очередь":
		bot.send_message(message.from_user.id, "Создание списка")
	elif message.text == '/reg':
		bot.send_message(message.from_user.id, "Как тебя зовут?")
		bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
	else:
		bot.send_message(message.from_user.id, "Напиши /help.")

def start(message):
	if message.text == '/reg':
		bot.send_message(message.from_user.id, "Как тебя зовут?")
		bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
	else:
		bot.send_message(message.from_user.id, 'Напиши /reg')

def get_surname(message):
	global surname
	surname = message.text

bot.polling(none_stop=True, interval=0)
