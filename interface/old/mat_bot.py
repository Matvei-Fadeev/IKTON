import telebot
from queue_bot_token import bot_token

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

state = 1

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global state
    if state == 0:
        print("ZERO STATE")
        text = "Hi, " + message.text + " !"
        bot.reply_to(message, text)
    elif state == 1:
        print("FIRST STATE")
        text = "aaaaaa " + message.text + " !"
        bot.reply_to(message, text)


bot.polling()
