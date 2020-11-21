import telebot

bot = telebot.TeleBot("%1465761077:AAF1MCjRHGKLO9PLwZ76opefreE2btD9bIw%")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, message.text)

bot.polling()
