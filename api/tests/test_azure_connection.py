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

    first_name = 'John'
    last_name = 'Doe'

    cursor.execute("INSERT INTO Persons (FirstName, LastName) VALUES (?, ?)", first_name, last_name)
    cnxn.commit()

    cursor.execute("SELECT * FROM Persons")
    rows = cursor.fetchall()
    for row in rows:
        assert row[1] == first_name and row[2] == last_name

    cnxn.close()