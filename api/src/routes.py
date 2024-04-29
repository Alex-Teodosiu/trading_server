from flask_restx import Api
from .controllers.user_controller import users
from .controllers.trading_account_controller import tradingaccounts

def initialize_routes(api: Api):
    api.add_namespace(users, path="/users")
    api.add_namespace(tradingaccounts, path="/trading_accounts")
    # Add more namespaces as needed