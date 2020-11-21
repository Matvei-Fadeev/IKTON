import telebot
from queue_bot_token import bot_token
from telebot import types

bot = telebot.TeleBot(bot_token)

@bot.message_handler(content_types=["text"])
def main_display(message):
    initials = ""
    bot.send_message(message.chat.id, "Введите ФИО")
    initials = message.test
    bot.send_message(message.chat.id, "Введите команду /start.")

def make_the_queue(message):
    lable = ""
    bot.send_message(message.from_user.id, 'Отправь короткую ссылку для создания очереди.')
    lable = message.text
    # отправили вопрос "Отправь короткую ссылку"
    # (((желательно дисциплина и группа будет содержаться в имени ссылки)))
    # link = input()
    # создается файл БД с этим именем
    # join_to_queue_display(link)



@bot.message_handler(commands=["start"])
def welcome_start():
    main_display(message)
    @bot.message_handler(content_types=["text"])
    def get_button(message):
        bot.send_message(message.chat.id, "Варианты действий")
        keyboard = types.InlineKeyboardMarkup()
        set_queue_button = types.InlineKeyboardButton(text="Создать очередь", callback_data="set")
        keyboard.add(set_queue_button)
        enter_queue = types.InlineKeyboardButton(text="Вступить в очередь", callback_data="enter")
        keyboard.add(enter_queue)
        bot.send_message(message.from_user.id, "Нажмити на кнопку:", reply_markup=keyboard)

        # @bot.callback_query_handler(func=lambda call: True)
        # def callback_worker(call):
        #     if call.data == "set":
        #         bot.send_message(call.message.chat.id, "set_work")
        #     if call.data == "enter":
        #         bot.send_message(call.message.chat.id, "enter_work")

@bot.message_handler(commands=["help"])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Список команд:/help, /start')

# link = то, что выбрал юзер
# def join_to_queue_display(link):
#     после выбора идет подтверждение записи и откроется очередь с уже
#     записавшимися людьми
#     live_queue(link)
#         if (кнопка == "Текущая очередь"):
#              live_queue(link)
#     elif (кнопка == "Вступить/Покинуть"): # Если вступлен, то "Выйти из очереди" всесто вступить
#         if ("Вступить"):
#             #внести человека в очередь и отобразить новую очередь
#         if ("Покинуть"):
#             #удаление человека из очереди с текущим telegram ID
#
#         live_queue(link)
#         join_to_queue_display(link)
#     elif (кнопка == "Закрыть"):
#         после нажатия которой возвращает на начальный экран
#         set_main_display()
#
# def live_queue(link):
#     отображает текущий список очереди с ключом link
#
# def set_main_display():
#     показать на главный экран
#
#  send /start
# def set_main_display():
#     должна быть какая-то авторизация (попросить ввести фамилию
#     и, если бот не умеет брать telegram ID, то спросить и его)
#     if (кнопка == "Вступить в очередь"):
#         join_to_queue_display(link)
#     elif (кнопка == "Создать очередь"):
#         link = make_the_queue()
#
bot.polling(none_stop=True, interval=0)