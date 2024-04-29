
class TradingAccount:
    def __init__(self, ID, api_key, password, user_id):
        self._id = ID
        self._api_key = api_key
        self._password = password
        self._user_id = user_id
    
    def to_dict(self):
        return {
            'id': self._id,
            'api_key': self._api_key,
            'password': self._password,
            'user_id': self._user_id
        }

    @property
    def ID(self):
        return self._ID

    @property
    def api_key(self):
        return self._api_key

    @property
    def password(self):
        return self._password

    @property
    def user_id(self):
        return self._user_id

    @ID.setter
    def ID(self, value):
        self._ID = value

    @api_key.setter
    def api_key(self, value):
        self._api_key = value

    @password.setter
    def password(self, value):
        self._password = value

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def __str__(self):
        return f"ID: {self._ID}, API Key: {self._api_key}, Password: {self._password}, User ID: {self._user_id}"