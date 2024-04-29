from .azure_sql_database import get_db_connection

class UserRepository:
    def get_users():
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM [user]")
        users = cursor.fetchall()

        conn.close()
        return users
    
    def get_user_by_email(self, email):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM [user] WHERE email = ?", email)
        user = cursor.fetchone()
        print(user)

        conn.close()
        return user


    def save_user(user):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO [user] (email, password, firstname, lastname) VALUES (?, ?, ?, ?)", 
                       (user['email'], user['password'], user['firstname'], user['lastname']))

        conn.commit()
        conn.close()