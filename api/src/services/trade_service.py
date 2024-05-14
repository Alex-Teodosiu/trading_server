from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from src.models.closed_position_model import ClosedPosition
from src.models.open_position_response_model import Position
from src.models.order_respnse_model import OrderResponse
from src.models.cancel_order_response_model import CancelOrderResponse
from src.data_access.trading_account_repository import TradingAccountRepository

class TradeService():
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()
    

    def create_order(self, user_id, order):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")
        api_key = trading_account.api_key
        secret_key = trading_account.api_secret
        temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        # prepare order data
        market_order_data = MarketOrderRequest(
                    symbol=order.get_symbol(),
                    # notionial only valid for day market orders
                    # else use the qty field
                    # qty=order.get_qty(),
                    notional=order.get_notional(),
                    side=order.get_side(),
                    time_in_force=order.get_time_in_force()
                    )
        # Market order
        try:
            market_order = temp_trading_client.submit_order(order_data=market_order_data)
        except Exception:
            return("Failed to submit order.")
        order_response = self.create_order_response(market_order)
        return order_response.to_dict()
    

    def create_limit_order(self, user_id, order):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")

        # prepare order data
        limit_order_data = LimitOrderRequest(
                    symbol=order.get_symbol(),
                    limit_price=order.get_limit_price(),
                    notional=order.get_notional(),
                    side=order.get_side(),
                    time_in_force=order.get_time_in_force()
                    )
        # Market order
        try:
            market_order = temp_trading_client.submit_order(order_data=limit_order_data)
        except Exception:
            return("Failed to submit order.")
        order_response = self.create_order_response(market_order)
        return order_response.to_dict()
    

    def get_all_orders(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided: "+user_id)
    
        # get all orders
        orders = temp_trading_client.get_orders()
        order_responses = []
        for order in orders:
            order_response = self.create_order_response(order)
            order_responses.append(order_response.to_dict())
        return order_responses


    def cancel_all_orders(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided: "+user_id)

        # attempt to cancel all open orders
        cancel_order_responses = temp_trading_client.cancel_orders()
        cancel_order_responses = []
        for response in cancel_order_responses:
            cancel_response = self.create_cancel_order_response(response)
            cancel_order_responses.append(cancel_response.to_dict())
        return cancel_order_responses
    
    # close order by id
    #
    #
    #


    def get_all_open_positions(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")

        # get all open trades
        try:
            open_trades = temp_trading_client.get_all_positions()
        except Exception:
            return("Failed to get open trades.")
        open_positions = []
        for position in open_trades:
            position_response = self.create_position_response(position)
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
        except Exception:
            return("Failed to get open trades.")
        closed_positions = []
        for position in closed_positions_response:
            closed_position = self.create_closed_position(position)
            closed_positions.append(closed_position)              
        return closed_positions
        

    def create_cancel_order_response(self, order):
        cancel_order_response = CancelOrderResponse(
            id=str(order.id),
            status=order.status
        )
        return cancel_order_response
    
    def create_order_response(self, order):
        order_response = OrderResponse(
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
        return order_response
    

    def create_position_response(self, position):
        position_response = Position(
            asset_class=position.asset_class,
            asset_id=position.asset_id,
            asset_marginable=position.asset_marginable,
            avg_entry_price=position.avg_entry_price,
            avg_entry_swap_rate=position.avg_entry_swap_rate,
            change_today=position.change_today,
            cost_basis=position.cost_basis,
            current_price=position.current_price,
            exchange=position.exchange,
            lastday_price=position.lastday_price,
            market_value=position.market_value,
            qty=position.qty,
            qty_available=position.qty_available,
            side=position.side,
            swap_rate=position.swap_rate,
            symbol=position.symbol,
            unrealized_intraday_pl=position.unrealized_intraday_pl,
            unrealized_intraday_plpc=position.unrealized_intraday_plpc,
            unrealized_pl=position.unrealized_pl,
            unrealized_plpc=position.unrealized_plpc,
            usd=position.usd
        )
        return position_response

    def create_closed_position(self, closed_position_data):
        closed_position = ClosedPosition(
            symbol=closed_position_data['symbol'],
            api_status=closed_position_data['status'],
            id=closed_position_data['body']['id'],
            client_order_id=closed_position_data['body']['client_order_id'],
            created_at=closed_position_data['body']['created_at'],
            updated_at=closed_position_data['body']['updated_at'],
            submitted_at=closed_position_data['body']['submitted_at'],
            filled_at=closed_position_data['body']['filled_at'],
            expired_at=closed_position_data['body']['expired_at'],
            canceled_at=closed_position_data['body']['canceled_at'],
            failed_at=closed_position_data['body']['failed_at'],
            replaced_at=closed_position_data['body']['replaced_at'],
            replaced_by=closed_position_data['body']['replaced_by'],
            replaces=closed_position_data['body']['replaces'],
            asset_id=closed_position_data['body']['asset_id'],
            asset_class=closed_position_data['body']['asset_class'],
            notional=closed_position_data['body']['notional'],
            qty=closed_position_data['body']['qty'],
            filled_qty=closed_position_data['body']['filled_qty'],
            filled_avg_price=closed_position_data['body']['filled_avg_price'],
            order_class=closed_position_data['body']['order_class'],
            order_type=closed_position_data['body']['order_type'],
            type=closed_position_data['body']['type'],
            side=closed_position_data['body']['side'],
            time_in_force=closed_position_data['body']['time_in_force'],
            limit_price=closed_position_data['body']['limit_price'],
            stop_price=closed_position_data['body']['stop_price'],
            status=closed_position_data['body']['status'],
            extended_hours=closed_position_data['body']['extended_hours'],
            legs=closed_position_data['body']['legs'],
            trail_percent=closed_position_data['body']['trail_percent'],
            trail_price=closed_position_data['body']['trail_price'],
            hwm=closed_position_data['body']['hwm'],
            subtag=closed_position_data['body']['subtag'],
            source=closed_position_data['body']['source']
        )
        return closed_position


