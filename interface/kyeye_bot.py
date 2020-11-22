import telebot
from telebot import types

from queue_bot_token import bot_token

from keyboard import *
#from questions import *
import cfg
from server_interface import send_data_to_server

bot = telebot.TeleBot(bot_token)

queue_name = ''
state = cfg.MENU

"""
    (1, 'matvei fadeev', 913446742, None, None, 0)
    (2, 'notclacker', 1388600539, None, None, 0)

    1) matvei fadeev
"""
def parsing_data_from_server(queue_name):
    response = send_data_to_server("show|%s|||" % (queue_name))
    users = response.split('|')
    result = ""
    for i in range(len(users)):
        user_data = users[i].split("'")
        if len(user_data) >= 2:
            user = user_data[1]
            result += str(i) + ") " + user.title().strip() + "\n"
    return result

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(
		message.chat.id,
		"Добро пожаловать. " + message.from_user.username + " ✌",
		reply_markup=main_display_keyboard())

@bot.message_handler(content_types=["text"])
def bot_text_handler(message):
    global state
    global queue_name
    chat_id = message.chat.id

    true_name = message.from_user.username
    if message.from_user.first_name is not None and message.from_user.last_name is not None:
        true_name = message.from_user.first_name + " " + message.from_user.last_name
    telegram_id = "1337" if message.from_user.id is None else str(message.from_user.id)

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

    elif message.text == "Занять":
        state = cfg.JOIN_TO_CURRENT_QUEUE
        request = "add|%s|%s|%s|" % (queue_name, true_name, telegram_id)
        response = send_data_to_server(request)
        bot.send_message(message.from_user.id, 'Ответ сервера : %s' % (response))
        if "err" in response:
            text = '❌ ошибка сервера : %s' % (response)
        else:
            text = '✅ успешно добавлен в очередь - %s' % (queue_name)
        bot.send_message(chat_id, text, parse_mode='HTML',reply_markup=in_queue_display_keyboard())


    elif message.text == "Покинуть очередь":
        state = cfg.GET_OUT_CURRENT_QUEUE

        request = "remove|%s|%s|%s|" % (queue_name, true_name, telegram_id)
        response = send_data_to_server(request)
        bot.send_message(message.from_user.id, 'Ответ сервера : %s' % (response))

        text = '✅ Вы покинули очередь. \n\n'
        bot.send_message(chat_id, text, parse_mode='HTML',reply_markup=queue_display_keyboard())

    elif message.text == "Список":
        state = cfg.PRINT_QUEUE
        response = parsing_data_from_server(queue_name)
        #response = send_data_to_server("show|%s|||" % (queue_name))
        text = '✅ Вот текущая очередь. \n\n'
        bot.send_message(message.from_user.id, '🚻 Список людей в очереди ℹ️:\n %s' % (response))
        bot.send_message(chat_id, text, parse_mode='HTML',reply_markup=queue_display_keyboard())


        """
            Ниже происходит перехват сообщений пользователя
            , а также вывод данных по запросу пользователя
        """
    else:
        #queue_name = message.text
        if state != cfg.MENU:
            #label = message.text
            queue_name = message.text

        if state == cfg.CREATE_GET_LABEL:
            #bot.send_message(message.from_user.id, 'Хочешь создать очередь %s?' % (queue_name))
            response = send_data_to_server("create|%s|||" % (queue_name))
            if "err" in response:
                bot.send_message(message.from_user.id, '❌ ошибка сервера : %s' % (response))
            else:
                bot.send_message(message.from_user.id, '✅ успешно созданна очередь - %s' % (queue_name))

        elif state == cfg.JOIN_GET_LABEL:
            response = parsing_data_from_server(queue_name)
            #response = send_data_to_server("show|%s|||" % (queue_name))
            bot.send_message(message.from_user.id, '🚻 Список людей в очереди ℹ️:\n %s' % (response))
        # elif state == cfg.JOIN_TO_CURRENT_QUEUE:
        #
        # elif state == cfg.GET_OUT_CURRENT_QUEUE:
        else:
            bot.send_message(message.from_user.id, 'WTF is happend : %d' % (state))


def first_bot_start():
    bot.polling()
