import cfg
import os.path
import shutil


def add_user(label, name, telegram_id):
    pass

def remove_user(label, name, telegram_id):
    pass

def db_exist(path) -> bool:
    return os.path.isfile(path)

def create_table(label):
    # current folder is IKTON/engine
    # path "./db_queues/kigk3122.sql"
    path = cfg.db_files_location + label + ".sql"
    if db_exist(path):
        return false
    else:
        current_path = "./template.sql"
        # ON LINUX : cp template.sql db_queues/new_name.sql
        shutil.copyfile("./template.sql", path)


def get_table(label):
    """
        Check existing of file by label
            Read table
        Else
    """
    path = ""
    if ():
        conn = sqlite3.connect(cfg.g_user_db_path)
        cursor = conn.cursor()
        try:
            row =
            column_name =
            table_name =
            request = "SELECT %s FROM %s WHERE %s = '%s'" % (row, table_name, column_name, license_key)
            cursor.execute(request)
            user_row = cursor.fetchone()
        except sqlite3.DatabaseError as err:
            time.sleep(cfg.g_error_sleep_sec)

        conn.close()
        if user_row == None:
            user_row = []
        return user_row
    else:
        return []


def process_user_data(data):
    print(data)
    if data == b'':
        return cfg.g_empty_response

    user_data = data.split(cfg.separateSymbol)

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
