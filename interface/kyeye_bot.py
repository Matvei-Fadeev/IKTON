import telebot
from telebot import types

from queue_bot_token import bot_token

from keyboard import *
#from questions import *
import cfg
from server_interface import send_data_to_server

bot = telebot.TeleBot(bot_token)

label = ''
state = cfg.MENU

def get_nickname(message):
    bot.send_message(message.from_user.id, 'Назови своё имя.')
    global nickname
    nickname = message.text

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(
		message.chat.id,
		"Добро пожаловать. " + message.from_user.username + " "
                                    + message.from_user.first_name + " "
                                    + message.from_user.last_name + " "
                                    + str(message.from_user.id) + " " + "✌",
		reply_markup=main_display_keyboard())

@bot.message_handler(content_types=["text"])
def bot_text_handler(message):
    global state
    chat_id = message.chat.id
    if message.text == 'Меню':
        state = cfg.MENU
        text = '✅ Основное меню \n\n'
        bot.send_message(chat_id, text, parse_mode='HTML',reply_markup=main_display_keyboard())

    elif message.text == 'Создать':
        state = cfg.CREATE_GET_LABEL
        text = '✅ Введите название очереди для создания. \n\n'
        bot.send_message(chat_id, text, parse_mode='HTML',reply_markup=default_keyboard())

    elif message.text == "Присоединиться":
        state = cfg.JOIN_GET_LABEL
        text = '✅ Введите название очереди для присоединения. \n\n'
        bot.send_message(chat_id, text, parse_mode='HTML',reply_markup=queue_display_keyboard())

    else:
        if state != cfg.MENU:
            global label
            label = message.text

        if state == cfg.CREATE_GET_LABEL:
            queue_name = message.text
            #bot.send_message(message.from_user.id, 'Хочешь создать очередь %s?' % (queue_name))
            response = send_data_to_server("create|%s|||" % (queue_name))
            if "error" in response:
                bot.send_message(message.from_user.id, '❌ ошибка сервера : %s?' % (response))
            else:
                bot.send_message(message.from_user.id, '✅ успешно созданна очередь - %s' % (queue_name))

        elif state == cfg.JOIN_GET_LABEL:
            #bot.send_message(message.from_user.id, 'Хочешь найти очередь %s?' % (message.text))
            queue_name = message.text
            response = send_data_to_server("show|%s|||" % (queue_name))
            bot.send_message(message.from_user.id, 'Ответ сервера : %s?' % (response))


        else:
            pass


def first_bot_start():
    bot.polling()
