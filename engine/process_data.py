import cfg
import os.path
import shutil

def add_user(cursor, name, telegram_id):
    request = """
    INSERT INTO queue (nickname, telegram_id, priority)
    VALUES ('%s', '%s', 0)
    """ % (name, telegram_id, 0)
    # ================
    cursor.execute(request)

def remove_user(label, name, telegram_id):
    # Удалять по столбцу никнейм если столбец nickname = name
    request = """

    DELETE FROM queue
    WHERE nickname = '%s'
    """ % (name)
    # ================
    cursor.execute(request)

def db_exist(path) -> bool:
    return os.path.isfile(path)

def create_table(path):
    current_path = "./template.sql"
    # ON LINUX : cp template.sql db_queues/new_name.sql
    shutil.copyfile(current_path, path)

def get_table(label):
    request = "SELECT %s FROM %s" % (cfg.full_row, cfg.table_name)
    cursor.execute(request)
    user_row = cursor.fetchone()

    if user_row == None:
        print(1)
        return []
    return user_row

def sort_by_priority(users):
    priority_users = []
    not_priority_users = []
    for i in range(len(users)):
        if users[i][5]:
            print(2)
            priority_users.append(users[i])
        else:
            print(3)
            not_priority_users.append(users[i])

    new_users = priority_users + not_priority_users
    return new_users

def process_user_data(data):
    print(data)
    if data == b'':
        print(4)
        return cfg.g_empty_response

    user_data = data.split(cfg.separateSymbol)
    print(user_data)
    cmd = user_data[cfg.CMD]
    label = user_data[cfg.LABEL]

    path = cfg.db_files_location + label + ".sql"
    conn = sqlite3.connect(cfg.g_user_db_path)
    cursor = conn.cursor()
    try:
        print("1")
        if db_exist(path):
            print("2")
            if cmd == "create":
                print(5)
                return cfg.err_already_created

            if len(user_data) >= cfg.DATA_COUNT:
                print(7)
                name = user_data[cfg.NAME]
                tid = user_data[cfg.tID]
                if cmd == "show":
                    print(9)
                    unsorted_users = get_table(cursor)

                    for elem in unsorted_users:
                        print(elem)

                    sorted_users = sort_by_priority(unsorted_users)
                    return sorted_users
                elif cmd == "add":
                    print("zxc")
                    return add_user(cursor, name, telegram_id)
                elif cmd == "remove":
                    print("fas")
                    return remove_user(cursor, name)
        else:
            if cmd == "create":
                print("a")
                create_table(path)
            else:
                print("b")
                return cfg.err_not_exist
    except sqlite3.DatabaseError as err:
        print("exception")
        time.sleep(cfg.g_error_sleep_sec)
    conn.close()

if "__main__" == __name__:
    users = [[ 1, "qwerty", '@qwerty', None, None, False]
            , [2, "Qwerty1", "@Qwerbgcbvty1", None, None, True]
            , [ 3, "1qoerty", '@qwttyerty', None, None, True]
            , [ 4, "2qwpoty", '@qwepxcuurty', None, None, False]
            , [ 5, "3qxcvberty", '@qweyyrty', None, None, True]
            , [ 6, "qwejbpk,ty", '@qwegfghrty', None, None, False]]
    print(sort_by_priority(users))
    #
    "CMD|KIGK3122|MySuperNickname|TelegramID|"
    "create|QWE|Vasya|Petya"
    "create|IKTK3122|Vasya|Petya|"
    "add|IKTK3122|Ghdfhkdjf|gflkbijgf|"
    "show|IKTK3122|Ghdfhkdjf|gflkbijgf|"
    "show|IKTK3122|||"
    "add|KIGK3122|QWERTY|ASDFGH|"
    "remove|KIGK3122|QWERTY|ASDFGH|"
    "remove|KIGK3122|QWERT|ASDFG|"
