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


@trades.route('/create-trade/<account_id>')
class TradeCreation(BaseResource):
    @api.expect(TradingAccount)
    def post(self, account_id):
        # trade = api.payload
        trade = {
          "symbol": "AAPL",
          "qty": 1,
          "side": "buy",
          "type": "market",
          "time_in_force": "day"
        }
        return self._trade_service.create_trade(account_id, trade), 201