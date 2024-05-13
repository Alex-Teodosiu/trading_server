from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.security import generate_password_hash
from src.models.trading_account_model import TradingAccount
from src.services.trading_account_service import TradingAccountService
from flask_restx import Namespace, Resource


tradingaccounts = Namespace('trading_accounts')
api = Namespace('api') 

class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._trading_account_service = TradingAccountService()


@tradingaccounts.route('/validateaccount')
@api.doc(params={'user_id':'User ID is required', 'api_key': 'Api key is required', 'secret': 'Secret is required'})
class AccountDetail(BaseResource):
    def post(self):
        user_id = request.args.get('user_id')
        api_key = request.args.get('api_key')
        secret = request.args.get('secret')
        return self._trading_account_service.get_account_by_credentials(user_id, api_key, secret), 200


@tradingaccounts.route('/deleteaccount')
@api.doc(params={'user_id':'User ID is required', 'api_key': 'Api key is required'})
class AccountDetail(BaseResource):
    def delete(self):
        user_id = request.args.get('user_id')
        api_key = request.args.get('api_key')
        return self._trading_account_service.delete_account(user_id, api_key), 200

    
