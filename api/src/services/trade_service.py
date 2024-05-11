import json
from src.config.dev_config import DevConfig
from src.data_access.trading_account_repository import TradingAccountRepository
#  broker --> from src.models.trading_account_model import TradingAccount
from alpaca.trading.client import TradingClient
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
    
    def get_trading_account(self):
        account = self._trading_client.get_account()
        return account
    

    def create_trade(self, account_id, trade):
        url = f"{self._base_url}/v1/trading/accounts/{account_id}/orders"
        response = requests.post(url, headers=self._headers, data=json.dumps(trade))
        print(response.text)

        if response.status_code != 200:
            raise Exception(f"Request to create trade failed with status {response.status_code}. Response: {response.text}")

        return response.json()