
def make_the_queue():
    # отправили вопрос "Отправь короткую ссылку"
    #(((желательно дисциплина и группа будет содержаться в имени ссылки)))
    link = input()
    #создается файл БД с этим именем
    join_to_queue_display(link)

#link = то, что выбрал юзер
def join_to_queue_display(link):
    #после выбора идет подтверждение записи и откроется очередь с уже
    #записавшимися людьми
    live_queue(link)
        # if (кнопка == "Текущая очередь"):
        #     live_queue(link)
    elif (кнопка == "Вступить/Покинуть"): # Если вступлен, то "Выйти из очереди" всесто вступить
        if ("Вступить"):
            #внести человека в очередь и отобразить новую очередь
        if ("Покинуть"):
            #удаление человека из очереди с текущим telegram ID

        live_queue(link)
        join_to_queue_display(link)
    elif (кнопка == "Закрыть"):
        #после нажатия которой возвращает на начальный экран
        set_main_display()

def live_queue(link):
    #отображает текущий список очереди с ключом link

def set_main_display():
    #показать на главный экран

# send /start
def set_main_display():
    #должна быть какая-то авторизация (попросить ввести фамилию
    #и, если бот не умеет брать telegram ID, то спросить и его)
    if (кнопка == "Вступить в очередь"):
        join_to_queue_display(link)
    elif (кнопка == "Создать очередь"):
        link = make_the_queue()
    

#
