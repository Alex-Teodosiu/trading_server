from .azure_sql_database import get_db_connection

class TradingAccountRepository:

    def get_accounts(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM trading_account")
        accounts = cursor.fetchall()

        conn.close()
        return accounts

    def get_account_by_id(self, id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM trading_account WHERE ID = ?", id)
        account = cursor.fetchone()
        print(account)

        conn.close()
        return account

    def validate_account(self, account):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM trading_account WHERE ID = ? AND api_key = ? AND password = ?", account['ID'], account['api_key'], account['password'])
        valid_account = cursor.fetchone()

        conn.close()
        return valid_account is not None