from flask import request
from flask_restx import Namespace, Resource, fields
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


@tradingaccounts.route('/getaccount')
@api.doc(params={'api_key': 'Api key is required', 'secret': 'Secret is required'})
class AccountDetail(BaseResource):
    def get(self):
        api_key = request.args.get('api_key')
        secret = request.args.get('secret')
        return self._trading_account_service.get_account_by_credentials(api_key, secret), 200
    


# @tradingaccounts.route('/createaccount')
# class AccountCreation(BaseResource):
#     @api.expect(TradingAccount)
#     def post(self):
#         account = api.payload
#         return self._trading_account_service.create_account(account), 201

# @tradingaccounts.route('/create-ach-relationship/<account_id>')
# class ACHRelationshipCreation(BaseResource):
#     def post(self, account_id):
#         ach_info = {
#             "account_owner_name": "Awesome Alpaca",
#             "bank_account_type": "CHECKING",
#             "bank_account_number": "32131231abc",
#             "bank_routing_number": "121000358",
#             "nickname": "Bank of America Checking"
#         }
#         try:
#             return self._trading_account_service.create_ACH_relationship(account_id, ach_info), 201
#         except Exception as e:
#             return {"error": str(e)}, 409
        
    
# @tradingaccounts.route('/make-ach-transfer/<account_id>')
# class ACHTransfer(BaseResource):
#     def post(self, account_id):
#         #account id
#         # e7b48113-819b-41d5-8dfe-45b9de82c375
#         transfer_info = {
#             "transfer_type": "ach",
#             "amount": "100",
#             "direction": "INCOMING",
#             "ach_relationship_id": "cef60a72-afb5-49ff-a707-794ab62bc89d"
#         }
#         return self._trading_account_service.make_ACH_transfer(account_id, transfer_info), 201


@tradingaccounts.route('/getaccounts')
class AccountList(BaseResource):
    def get(self):
        return self._trading_account_service.get_accounts(), 200



@tradingaccounts.route('/validateaccount')  
class AccountValidation(BaseResource):
    @api.expect(TradingAccount)
    def post(self):
        account = api.payload
        return self._trading_account_service.validate_account(account), 200
    