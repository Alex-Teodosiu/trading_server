import re
import traceback
from src.data_access.user_repository import UserRepository
from werkzeug.security import check_password_hash
from src.models.user_model import User
from flask import jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token, decode_token


class UserService:
    def __init__(self):
        self._user_repository = UserRepository()

    def get_user_by_email(self, email):
        user_row = self._user_repository.get_user_by_email(email)
        if user_row is not None:
            user = User(user_row[1], user_row[2])
            user = user.to_dict()
            print(user.__str__())
        else:
            user = None
        return user

    def signup(self, email, password):
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        print(hashed_password)
        print(email)
        user = User(email=email, password=hashed_password)
        print(user.__str__())
        self._user_repository.save_user(user)
        return self.generate_token(identity=email)

    def signin(self, email, password):
        try:
            user = self._user_repository.get_user_by_email(email)

            if user and check_password_hash(user.password, password):
                token = self.generate_token(identity=email)
                return {'access_token': token}, 200
            return jsonify({'error': 'Invalid email or password'}), 401

        except Exception as e:
            return jsonify({'error': 'An error occurred: ' + str(e)}), 500


    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        

    def validate_password(self, password):
        if len(password) < 5:
            raise ValueError("Password must be at least 5 characters long")
        if not re.search(r"\d", password):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password):
            raise ValueError("Password must contain at least one special character")
        pass

    
    def generate_token(self, identity):
        token = create_access_token(identity=identity)
        return token


    def decode_token(self, token):
        try:
            decoded_token = decode_token(token)
            return decoded_token
        except Exception as e:
            # Handle invalid token error
            return None