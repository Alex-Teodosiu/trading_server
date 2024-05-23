import pyodbc
import pytest

def test_azure_connection():
    server = 'tradingplatformserver.database.windows.net'
    database = 'tradingplatformdb'
    username = 'CloudSA25ca4491'
    password = 'Azure123!'
    driver= '{ODBC Driver 17 for SQL Server}'

    cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()

    email = 'john@gmail.com'
    password = 'Qwerty123!'

    cursor.execute("INSERT INTO [user] (email, password) VALUES (?, ?)", email, password)
    cnxn.commit()

    cursor.execute("SELECT * FROM [user] where email = ? and password = ?", email, password)
    rows = cursor.fetchall()
    for row in rows:
        assert row[1] == email and row[2] == password

    cnxn.close()


