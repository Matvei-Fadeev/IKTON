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

@bot.message_handler(commands=['text'])
def get_button(message):
	if message.text == "Кнопка":
		keyboard = types.InlineKeyboardMarkup()
		callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
		keyboard.add(callback_button)
		bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	# Here is button realization
    bot.send_message(message.chat.id, 'get_text_messages')


bot.polling(none_stop=True, interval=0)
