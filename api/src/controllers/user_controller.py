from flask_restx import Namespace, Resource
from flask import request  
from src.models.user_model import User  
from src.services.user_service import UserService  

users = Namespace('users')
api = Namespace('api')  # Add this line to define the 'api' object
user_service = UserService()  # Instantiate UserService


@users.route('/signin')
class SignIn(Resource):
    @users.expect(User)
    def post(self):
        data = request.json
        token = user_service.signin(data['email'], data['password'])
        if token:
            return {'message': 'Logged in successfully.', 'token': token}, 200
        return {'message': 'Invalid email or password.'}, 401


@users.route('/signup')
class SignUp(Resource):
    @users.expect(User)
    def post(self):
        data = request.json
        token = user_service.signup(data['email'], data['password'])
        if token:
            return {'message': 'Signed up successfully.', 'token': token}, 200
        return {'message': 'Email already exists.'}, 400
    
@users.route('/getuser/<email>')
class GetUser(Resource):
    def get(self, email):
        user = user_service.get_user_by_email(email)
        if user:
            return user, 200
        return {'message': 'User not found.'}, 404