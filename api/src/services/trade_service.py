from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from src.config.dev_config import DevConfig
from src.data_access.trading_account_repository import TradingAccountRepository
#  broker --> from src.models.trading_account_model import TradingAccount
import requests

class TradeService():
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()
        # For now, we'll use my personal Alpaca API keys.
        # We'll need to use the user's key and secret in the future.
        # This can be done by pulling the user's API key and secret from the database.
        # From the trading_account table using the user_id foreign key.
        config = DevConfig()
        self._api_key = config.ALPACA_API_KEY
        self._secret_key = config.ALPACA_API_SECRET
        self._trading_client = TradingClient(self._api_key, self._secret_key, paper=True)
    

    def create_order(self):
        # preparing orders
        market_order_data = MarketOrderRequest(
                            symbol="SPY",
                            qty=0.023,
                            side=OrderSide.BUY,
                            time_in_force=TimeInForce.DAY
                            )
        # Market order
        market_order = self._trading_client.submit_order(
                        order_data=market_order_data
                       )

        return market_order
    

    def create_limit_order(self):
        limit_order_data = LimitOrderRequest(
                    symbol="BTC/USD",
                    limit_price=17000,
                    notional=4000,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.FOK
                   )
        # Limit order
        limit_order = self._trading_client.submit_order(
                        order_data=limit_order_data
                      )
        return limit_order
    

    def get_all_orders(self):
        # params to filter orders by
        request_params = GetOrdersRequest(
                            status=QueryOrderStatus.OPEN,
                            side=OrderSide.SELL
                         )
        # orders that satisfy params
        orders = self._trading_client.get_orders(filter=request_params)
        return orders


    def cancel_all_orders(self):
        # attempt to cancel all open orders
        cancel_statuses = self._trading_client.cancel_orders()
        return cancel_statuses


    def get_all_open_trades(self):
        # get all open trades
        open_trades = self._trading_client.get_all_positions()
        return open_trades
    

    def close_all_open_trades(self):
        # closes all position AND also cancels all open orders
        self._trading_client.close_all_positions(cancel_orders=True)
