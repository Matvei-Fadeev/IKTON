import sqlite3
import time
import cfg
import os.path
import shutil


def add_user(cursor, conn, name, telegram_id):
    check_request = """
    SELECT * FROM queue
    WHERE telegramID = '%s'
    """ % (telegram_id)
    cursor.execute(check_request)
    user_rows = cursor.fetchall()
    if not user_rows:
        request = """
            INSERT INTO queue (nickname, telegramID, priority)
            VALUES ('%s', '%s', 0)
        """ % (name, telegram_id)
        cursor.execute(request)
        conn.commit()
        return cfg.err_success
    else:
        return cfg.err_already_added


def remove_user_by_tid(cursor, conn, telegram_id):
    request = """
    DELETE FROM queue
    WHERE telegramID = '%s'
    """ % (telegram_id)
    # ================
    cursor.execute(request)
    conn.commit()
    return cfg.err_success


def db_exist(path) -> bool:
    return os.path.isfile(path)
def create_table(path):
    current_path = "./template.sql"
    # ON LINUX : cp template.sql db_queues/new_name.sql
    shutil.copyfile(current_path, path)

def get_table(cursor):
    request = "SELECT %s FROM %s" % (cfg.full_row, cfg.table_name)
    cursor.execute(request)
    user_rows = cursor.fetchall()

    if user_rows == None:
        return [()]
    return user_rows

def sort_by_priority(users):
    priority_users = []
    not_priority_users = []
    for i in range(len(users)):
        if users[i][5]:
            priority_users.append(users[i])
        else:
            not_priority_users.append(users[i])

    new_users = priority_users + not_priority_users
    return new_users

def process_user_data(bytes_data):
    print("\n\n")
    data = bytes_data.decode('ascii').lower()
    print(data)
    if data == b'':
        return cfg.g_empty_response

    user_data = data.split(cfg.separateSymbol)
    print(user_data)
    if len(user_data) <= 1:
        return cfg.err_bad_response

    cmd = user_data[cfg.CMD]
    label = user_data[cfg.LABEL]
    if cmd not in cfg.cmds or ((cmd == "add" or cmd == "remove") and len(user_data) < cfg.DATA_COUNT):
        return cfg.err_bad_response

    print("CMD =", cmd, "LABEL =", label)
    path = cfg.db_files_location + label + ".sql"
    print(path)
    print(db_exist(path))

    if cmd == "create":
        if db_exist(path):
            return cfg.err_already_created
        else:
            create_table(path)
            return cfg.err_success

    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    try:
        if db_exist(path):
            if len(user_data) >= cfg.DATA_COUNT:
                name = user_data[cfg.NAME]
                telegram_id = user_data[cfg.tID]
                print("name =", name, "tid =", telegram_id)
                if cmd == "show":
                    unsorted_users = get_table(cursor)
                    print("FILENAME = ", path)
                    print(unsorted_users)
                    sorted_users = sort_by_priority(unsorted_users)
                    res = "|".join(str(i) for i in sorted_users)
                    # for elem in sorted_users:
                    #     print(elem)
                    #     res = "".join(str(i) for i in sorted_users)
                    return res
                elif cmd == "add":
                    return add_user(cursor, conn, name, telegram_id)
                elif cmd == "remove":
                    return remove_user_by_tid(cursor, conn, telegram_id)
        else:
            return cfg.err_not_exist
    except sqlite3.DatabaseError as err:
        print("exception")
        time.sleep(cfg.g_error_sleep_sec)
    conn.close()
    return cfg.err

"""=============================================================================
    SOME TESTS
"""
if "__main__" == __name__:
    users = [[ 1, "qwerty", '@qwerty', None, None, False]
            , [2, "Qwerty1", "@Qwerbgcbvty1", None, None, True]
            , [ 3, "1qoerty", '@qwttyerty', None, None, True]
            , [ 4, "2qwpoty", '@qwepxcuurty', None, None, False]
            , [ 5, "3qxcvberty", '@qweyyrty', None, None, True]
            , [ 6, "qwejbpk,ty", '@qwegfghrty', None, None, False]]
    print(sort_by_priority(users))
    #
    data = ["CMD|KIGK3122|MySuperNickname|TelegramID|",
    "create|QWE|Vasya|Petya",
    "create|IKTK3122|Vasyaas|Petyaas|",
    "add|IKTK3122|Ghdfhkdjf|gflkbijgf|",
    "add|IKTK3122|asGhdfhkdjf|ASDgflkbijgf|",
    "show|IKTK3122|Ghdfhkdjf|gflkbijgf|",
    "show|IKTK3122|||",
    "add|KIGK3122|QWERTY|ASDFGH|",
    "remove|KIGK3122|QWERTY|ASDFGH|",
    "remove|KIGK3122|QWERT|ASDFG|"]

    for elem in data:
        byte_data = bytes(elem, encoding = 'ascii')
        process_user_data(byte_data)
