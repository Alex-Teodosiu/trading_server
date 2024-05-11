
class User:
    def __init__(self, email, password):
        self._email = email
        self._password = password


    def to_dict(self):
        return {
            'email': self._email,
            'password': self._password
        }


    def __str__(self):
        return f"Email: {self._email}, Password: {self._password}"
