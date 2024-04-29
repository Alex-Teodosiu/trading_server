from flask import request
from flask_restx import Namespace, Resource
from werkzeug.security import generate_password_hash
from src.models.trading_account_model import TradingAccount
from src.services.trading_account_service import TradingAccountService
from flask_restx import Namespace, Resource


tradingaccounts = Namespace('tradingaccounts')
api = Namespace('api') 

class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._trading_account_service = TradingAccountService()

@tradingaccounts.route('/getaccounts')
class AccountList(BaseResource):
    def get(self):
        return self._trading_account_service.get_accounts(), 200

@tradingaccounts.route('/getaccount/<id>')
class AccountDetail(BaseResource):
    def get(self, id):
        return self._trading_account_service.get_account_by_id(id), 200

@tradingaccounts.route('/validateaccount')  
class AccountValidation(BaseResource):
    @api.expect(TradingAccount)
    def post(self):
        account = api.payload
        return self._trading_account_service.validate_account(account), 200
    