from src.models.limit_order_model import LimitOrder
from src.models.order_model import Order
from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.security import generate_password_hash
from src.models.trading_account_model import TradingAccount
from src.services.trading_account_service import TradingAccountService
from src.services.trade_service import TradeService
from flask_restx import Namespace, Resource


trades = Namespace('trades')
api = Namespace('api') 
trade_service = TradeService()

@trades.route('/create-order')
class TradeCreation(Resource):
    @trades.expect(Order)
    def post(self):
        data = request.json
        user_id = data['user_id']
        order = Order(
            symbol=data['symbol'],
            # qty=data['qty'],
            notional=data['notional'],
            side=data['side'],
            time_in_force=data['time_in_force']
        )
        result = trade_service.create_order(user_id, order)
        return result
    
    
@trades.route('/create-limit-order')
class LimitTradeCreation(Resource):
    @trades.expect(LimitOrder)
    def post(self):
        data = request.json
        user_id = data['user_id']
        limit_order = LimitOrder(
            symbol=data['symbol'],
            limit_price=data['limit_price'],
            notional=data['notional'],
            side=data['side'],
            time_in_force=data['time_in_force']
        )
        result = trade_service.create_limit_order(user_id, limit_order)
        return result
    
    
@trades.route('/get-all-orders')
@api.doc(params={'user_id':'User ID is required'})
class GetAllTrades(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        return trade_service.get_all_orders(user_id), 200
    

# Make this an update or delete request
@trades.route('/cancel-all-orders')
@api.doc(params={'user_id':'User ID is required'})
class CancelAllOrders(Resource):
    def delete(self):
        user_id = request.args.get('user_id')
        return trade_service.cancel_all_orders(user_id), 200
    
  
@trades.route('/get-all-open-positions')
@api.doc(params={'user_id':'User ID is required'})
class GetAllOpenTrades(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        return trade_service.get_all_open_positions(user_id), 200
    

@trades.route('/close-all-open-positions')
@api.doc(params={'user_id':'User ID is required'})
class CloseAllOpenPositions(Resource):
    def delete(self):
        user_id = request.args.get('user_id')
        return trade_service.close_all_open_positions(user_id), 200