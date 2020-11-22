from process_data import *

"""
1 Vasya
2 Dan
3 Kek
"""

if "__main__" == __name__:
    path = "./db_queues/table.sql"

    if not db_exist(path):
        print("Not exist")
        create_table(path)

    if db_exist(path):
        print("Already exist")

    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    name = "Vasya"
    tid = "412142"

    add_user(cursor, conn, name, tid)
    add_user(cursor, conn, name, tid)
    add_user(cursor, conn, name, tid)
    #add_user(cursor, name+"1", tid+"5")

    result = get_table(cursor)
    for elem in result:
        print(elem)

    remove_user_by_tid(cursor, conn, tid)

    result = get_table(cursor)
    for elem in result:
        print(elem)

    conn.commit()
    conn.close()


    pass
