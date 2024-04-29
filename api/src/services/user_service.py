import re
from src.services.jwt_service import JWTService
from src.data_access.user_repository import UserRepository
from werkzeug.security import check_password_hash
from src.models.user_model import User


class UserService:
    def __init__(self):
        self._user_repository = UserRepository()
        self._jwt_service = JWTService()

    def get_user_by_email(self, email):
        user_row = self._user_repository.get_user_by_email(email)
        if user_row is not None:
            user = User(user_row[1], user_row[2], user_row[3], user_row[4])
            user = user.to_dict()
            print(user.__str__())
        else:
            user = None
        return user

    def signup(self, email, password):
        self.validate_email(email)
        self.validate_password(password)
        token = self._jwt_service.signup(email, password)
        return token

    def signin(self, email, password):
        user = self._user_repository.find_by_email(email)
        if user and check_password_hash(user.password, password):
            token = self._jwt_service.signin(email, password)
            return token
        return None

    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        

    def validate_password(self, password):
        # Add your password validation logic here
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