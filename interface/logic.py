
def get_link_from_user():
    # Спросили узера
    # отправили вопрос "Отправь короткую ссылку"
    # вернуть эту ссылку
    #(((желательно дисциплина и группа будет содержаться в имени ссылки)))
    link = input()
    #создается файл БД с этим именем
    #будет предложено вступить в эту очередь
    #добавить кнопку выйти, вдруг админ заранее создает очередь
    if (кнопка == "Вступить в эту очередь"):
        join_to_queue(link)
    if (кнопка == "Выход"):
        exit()
        #возвращенеи на главный экран


def join_to_queue(link):
    #появляется кнопка "Выбрать очередь"
    #link = то, что выбрал юзер
    #выкатывается список доступных очередей, надо выбрать очередь, далее
    #появятся кнопки с выбором даты и времени
    #после выбора идет подтверждение записи и откроется очередь с уже
    #записавшимися людьми


    #должна быть кнопка "Завершить выбор",
    #после нажатия которой возвращает на начальный экран


def available_queues():
    #это экран с доступными очередями
    #должна быть кнопка "Выход" и "Создать очередь"
    if (кнопка == "Выход"):
        exit()
    elif (кнопка == "Создать очередь"):
        get_link_from_user()



def exit():
    #возвразение на главный экран

# send /start
def start():
    #должна быть какая-то авторизация (попросить ввести фамилию
    #и, если бот не умеет брать телеграм ID, то спросить и его)
    if (кнопка == "Вступить в очередь"):
        join_to_queue(link)
    elif (кнопка == "Создать очередь"):
        link = get_link_from_user()
    elif (кнопка == "Просмотр очередей"):
        available_queues()















#
