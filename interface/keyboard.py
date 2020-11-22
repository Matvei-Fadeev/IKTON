import telebot
from telebot import types

# Основное меню, главное, при любом старте
def main_display_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	first_btn = types.KeyboardButton('Присоединиться')
	second_btn = types.KeyboardButton('Создать')
	markup.add(first_btn, second_btn)
	return markup


def queue_display_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	first_btn = types.KeyboardButton('Вступить')
	second_btn = types.KeyboardButton('Список')
	third_btn = types.KeyboardButton('Меню')
	markup.add(first_btn, second_btn, third_btn)
	return markup


def default_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn = types.KeyboardButton('Меню')
    markup.add(btn)
    return markup

# def join_keyboard():
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#     btnf = types.KeyboardButton("aaa")
#     btns = types.KeyboardButton("bbb")
#     markup.add(btnf, btns)
#     return markup
#
# def create_keyboard():
# 	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
# 	btn = types.KeyboardButton('Меню')
# 	markup.add(btn)
# 	return markup
