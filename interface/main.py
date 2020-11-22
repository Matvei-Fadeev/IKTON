from kyeye_bot import first_bot_start

if "__main__" == __name__:
    print("Start")
    while True:
        try:
            first_bot_start()
        except Exception as err:
            pass
