# data to configurate server to working
separateSymbol = '|'
HOST = '0.0.0.0'
PORT = 2222
g_count_of_received_symbols = 1000
# g_user_db_path = "user_db.sql"
g_empty_response = '0'
g_max_attempts = 10



class db_rows(object):
    ID = 0
    LICENSE_KEY = 1
    HWID = 2
    VALIDITY_DAYS = 3
    EXPIRATION_DATE = 4
    SUBSCRIBE_TYPE = 5
    ROWS_COUNT = 6

g_db_full_row = "*"
g_db_table_name = "users_licenses"
g_db_license_key = "license_key"
g_db_column_id = "user_id"
g_db_column_hwid = "hwid"
g_db_column_expiration_date = "expiration_date"
