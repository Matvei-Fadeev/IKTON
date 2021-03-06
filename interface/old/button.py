import telebot
from queue_bot_token import bot_token
from telebot import types


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=["start"])
def welcome_start(message):
	bot.send_message(message.chat.id, "welcome_start")

@bot.message_handler(commands=["help"])
def welcome_help(message):
	bot.send_message(message.chat.id, "Напиши Меню")

@bot.message_handler(content_types=["text"])

def get_button(message):
    bot.send_message(message.chat.id, "Начало")
    if message.text == "Меню":
        bot.send_message(message.chat.id, "Варианты действий")
        keyboard = types.InlineKeyboardMarkup() #Создание клавиатуры
        set_queue_button = types.InlineKeyboardButton(text="Создать очередь", callback_data="set")
        keyboard.add(set_queue_button)
        exist_queue_button = types.InlineKeyboardButton(text="Посмотреть очереди", callback_data="see")
        keyboard.add(exist_queue_button)
        add_person_button = types.InlineKeyboardButton(text="Добавить участника", callback_data="add")
        keyboard.add(add_person_button)
        delete_queue_button = types.InlineKeyboardButton(text="Удалить очередь", callback_data="delete")
        keyboard.add(delete_queue_button)

        bot.send_message(message.from_user.id, "Нажмити на кнопку:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Ответ')
    answer = ""
    arr = [1, 2, 3, 4]
    if call.data == "set":
        answer = "Введите короткую ссылку для очереди."
    if call.data == "see":
        answer = arr
    if call.data == "add":
        answer = arr.append(len(arr) + 1)
    if call.data == "delete":
        answer = ""
    bot.send_message(call.message.chat.id, answer)
bot.polling(none_stop=True, interval=0)