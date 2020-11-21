import cfg

"""
    import

"""

def add_user(label, name, telegram_id):
    pass

def remove_user(label, name, telegram_id):
    pass


def db_exist(path) -> bool:
    """
        check for existing of file in Unix system
        find function
    """

def create_table(label):
    # current folder is IKTON/engine
    # path "./db_queues/kigk3122.sql"
    path = cfg.db_files_location + label + ".sql"
    if db_exist(path):
        return false
    else:
        """ Creating the new db
            Lib for working with Linux
            Function to copy file using template.sql
        """

def get_table(label):
    """
        Check existing of file by label
            Read table
        Else
    """


def process_user_data(data):
    if !data:
        return cfg.g_empty_response

    """
        Parse data
        #user_data = data.split(cfg.separateSymbol)
    """
    response = [] # !! hz

    cmd = user_data[cfg.CMD]
    if cmd == "create":
        create_table(label)
    elif cmd == "show":
        response = get_table(label)
    elif len(user_data) >= cfg.DATA_COUNT:
        label = user_data[cfg.LABEL].lower()
        name = user_data[cfg.NAME].lower()
        telegram_id = user_data[cfg.TID]

        if cmd == "add":
            add_user(label, name, telegram_id)
        elif cmd == "remove":
            remove_user(label, name, telegram_id)


    print(data)
