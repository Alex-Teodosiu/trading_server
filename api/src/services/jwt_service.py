from flask_jwt_extended import create_access_token, decode_token
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.user_model import User
from src.data_access.user_repository import UserRepository

class JWTService:
    def __init__(self):
        self._user_repository = UserRepository()

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
        
    def signup(self, email, password):
        hashed_password = generate_password_hash(password)
        user = User(email=email, password=hashed_password)
        self._user_repository.save(user)
        return create_access_token(identity=email)

    def signin(self, email, password):
        user = self._user_repository.find_by_email(email)
        if user and check_password_hash(user.password, password):
            return create_access_token(identity=email)
        return None