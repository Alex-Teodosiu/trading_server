from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.security import generate_password_hash
from src.models.trading_account_model import TradingAccount
from src.services.trading_account_service import TradingAccountService
from src.services.trade_service import TradeService
from flask_restx import Namespace, Resource


trades = Namespace('trades')
api = Namespace('api') 

class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._trade_service = TradeService()

# Will need the either the account id or trading account id that I will join to get the api key
# For now, use default credz
@trades.route('/create-trade')
class TradeCreation(BaseResource):
    def post(self):
        return self._trade_service.create_order(), 201
    
@trades.route('/create-limit-trade')
class LimitTradeCreation(BaseResource):
    def post(self):
        return self._trade_service.create_limit_order(), 201
    
@trades.route('/get-all-trades')
class GetAllTrades(BaseResource):
    def get(self):
        return self._trade_service.get_all_orders(), 200
    

# Make this an update or delete request
@trades.route('/cancel-all-orders')
class CancelAllOrders(BaseResource):
    def post(self):
        return self._trade_service.cancel_all_orders(), 200
    
  
@trades.route('/get-all-open-trades')
class GetAllOpenTrades(BaseResource):
    def get(self):
        return self._trade_service.get_all_open_trades(), 200
    

@trades.route('/close-all-open-positions')
class CloseAllOpenPositions(BaseResource):
    def post(self):
        return self._trade_service.close_all_open_positions(), 200