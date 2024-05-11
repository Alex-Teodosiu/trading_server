
import pytest
from src.services import user_service

user_service = user_service.UserService()

def test_sign_up(mocker):
    
    username = 'Test User'
    password = 'Test Password'
    mocker.patch('src.services.UserService', return_value={'id': 1, 'username': username})
    user = user_service.signup(username, password)
    assert user == {'id': 1, 'username': username}


