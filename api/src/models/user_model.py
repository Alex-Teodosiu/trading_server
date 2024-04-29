
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, email, firstname, lastname, password):
        #self._id = id
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._password = generate_password_hash(password, method='pbkdf2:sha256:1000000')

    def to_dict(self):
        return {
            'firstname': self._firstname,
            'lastname': self._lastname,
            'email': self._email,
            'password': self._password
        }

    # Getters
    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    
    # Setters
    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @lastname.setter
    def lastname(self, value):
        self._lastname = value

    @email.setter
    def email(self, value):
        self._email = value

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value, method='pbkdf2:sha256:1000000')

    def check_password(self, password):
        return check_password_hash(self._password, password)

    def __str__(self):
        return f"Firstname: {self._firstname}, Lastname: {self._lastname}, Username: {self._username}, Email: {self._email}, Password: {self._password}"