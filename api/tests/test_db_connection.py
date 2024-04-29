from src.data_access import user_repository

def test_get_users():
    users = user_repository.get_users()
    print(users)

def test_get_user_by_id():
    user = user_repository.get_user_by_id(1)  # replace 1 with an actual user_id
    print(user)

def test_db_connection():
    test_get_users()
    test_get_user_by_id()

if __name__ == "__main__":
    test_db_connection()