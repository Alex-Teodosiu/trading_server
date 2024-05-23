from alpaca.trading.client import TradingClient
from src.models.position.position_model import ClosedPosition
from src.models.order.order_response_model import OrderResponse
from src.data_access.trading_account_repository import TradingAccountRepository
import json

class PositionService():
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()


    def get_all_open_positions(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")
        # get all open positions
        try:
            open_trades = temp_trading_client.get_all_positions()
        except Exception as e:
            return(json.loads(str(e))['message'])
        open_positions = []
        for position in open_trades:
            position_response = self.create_order_response(position)
            open_positions.append(position_response.to_dict())
        return open_positions


    def close_all_open_positions(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")
        try:
            # closes all position 
            closed_positions_response = temp_trading_client.close_all_positions()
            print(f"closed_positions_response: {closed_positions_response}")
            print(f"Type of closed_positions_response: {type(closed_positions_response)}")
        except Exception as e:
            return(json.loads(str(e))['message'])
        return "Closed all positions"
       

    def close_position_by_symbol(self, user_id, symbol):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception as e:
            return("Failed to get trading account for user_id provided.")
        try:
            closed_positions_response = temp_trading_client.close_position(symbol)
            print(f"closed_positions_response: {closed_positions_response}")
            print(f"Type of closed_positions_response: {type(closed_positions_response)}")
        except Exception as e:
            return json.loads(str(e))['message'] if self.is_json(str(e)) else str(e)
        
        closed_position = self.create_order_response(closed_positions_response)
                         
        return closed_position.to_dict()


    @staticmethod
    def is_json(myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False
        return True

    
    
    def create_order_response(self, order):
        if isinstance(order, tuple):
            order = order[0]
        return OrderResponse(
            id=str(order.id),
            client_order_id=order.client_order_id,
            created_at=order.created_at.isoformat(),
            updated_at=order.updated_at.isoformat(),
            submitted_at=order.submitted_at.isoformat(),
            filled_at=order.filled_at.isoformat() if order.filled_at else None,
            expired_at=order.expired_at.isoformat() if order.expired_at else None,
            canceled_at=order.canceled_at.isoformat() if order.canceled_at else None,
            failed_at=order.failed_at.isoformat() if order.failed_at else None,
            replaced_at=order.replaced_at.isoformat() if order.replaced_at else None,
            replaced_by=order.replaced_by,
            replaces=order.replaces,
            asset_id=str(order.asset_id),
            symbol=order.symbol,
            asset_class=order.asset_class,
            notional=order.notional,
            qty=order.qty,
            filled_qty=order.filled_qty,
            filled_avg_price=order.filled_avg_price,
            order_class=order.order_class,
            order_type=order.order_type,
            type=order.type,
            side=order.side,
            time_in_force=order.time_in_force,
            limit_price=order.limit_price,
            stop_price=order.stop_price,
            status=order.status,
            extended_hours=order.extended_hours,
            legs=order.legs,
            trail_percent=order.trail_percent,
            trail_price=order.trail_price,
            hwm=order.hwm,
            # subtag=order.subtag,
            # source=order.source
        )



