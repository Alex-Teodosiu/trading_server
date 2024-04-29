import pyodbc
from dotenv import load_dotenv

def get_db_connection():
    load_dotenv()

    server = 'tradingplatformserver.database.windows.net'
    database = 'tradingplatformdb'
    username = 'CloudSA25ca4491'
    password = 'Azure123!'
    driver= '{ODBC Driver 17 for SQL Server}'

    connection = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    return connection