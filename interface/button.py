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

@bot.message_handler(content_types=["text"])
def default_test(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)

