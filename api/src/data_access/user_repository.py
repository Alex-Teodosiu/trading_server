from src.data_access.azure_sql_database import AzureSQLDatabase

class UserRepository:
    def __init__(self):
        self._db = AzureSQLDatabase()

    def get_users(self):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [user]")
        users = cursor.fetchall()
        conn.close()
        return users
    
    def get_user_by_email(self, email):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [user] WHERE email = ?", email)
        user = cursor.fetchone()
        print("User from repo")
        print(user)

        conn.close()
        return user


    def save_user(self, user):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO [user] (email, password) VALUES (?, ?)", 
                       (user.get_email(), user.get_password()))

        conn.commit()
        conn.close()