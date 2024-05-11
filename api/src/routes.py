from flask_restx import Api
from .controllers.user_controller import users
from .controllers.trading_account_controller import tradingaccounts
from .controllers.asset_controller import assets
from .controllers.trade_controller import trades
from .controllers.market_data_controller import market_data
from .controllers.algorithm_controller import algorithm

def initialize_routes(api: Api):
    api.add_namespace(users, path="/users")
    api.add_namespace(tradingaccounts, path="/trading_accounts")
    api.add_namespace(assets, path="/assets")
    api.add_namespace(trades, path="/trades")
    api.add_namespace(market_data, path="/market_data")
    api.add_namespace(algorithm, path="/algorithm")