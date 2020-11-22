# data to configurate server to working
separateSymbol = "|"
HOST = '0.0.0.0'
PORT = 2222

db_files_location = "./db_queues/"
g_count_of_received_symbols = 1000
# g_user_db_path = "user_db.sql"
g_empty_response = b"error"
g_max_attempts = 10
g_error_sleep_sec = 0.04

cmds = ["create", "add", "remove", "show"]
"CMD|KIGK3122|MySuperNickname|TelegramID|"
CMD = 0
LABEL = 1
NAME = 2
tID = 3
DATA_COUNT = 4


full_row = "*"
table_name = "queue"
column_name = "nickname"
column_tid = "telegramID"
column_data = "data"        #!!!!!!
column_pos = "position"     #!!!!!!
column_pri = "priority"


# Errors
err_bad_response = "err_bad_response"
err_already_created = "err_already_created"
err_already_added = "err_already_added"
err_not_exist = "err_not_exist"
err = "error"
err_success = "success"
