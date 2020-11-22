import telebot

nickname = ''

def get_nickname(message):
	bot.send_message(message.from_user.id, 'Назови своё имя.')
	global nickname
	nickname = message.text
