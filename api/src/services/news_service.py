import requests
import json

from src.data_access.trading_account_repository import TradingAccountRepository

class NewsService:
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()

    def fetch_historical_news(self, user_id, symbols, start_date, end_date):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            api_secret = trading_account.api_secret
        except Exception as e:
            return {"error": str(e)}, 500

        url = f'https://data.alpaca.markets/v1beta1/news?start={start_date}&end={end_date}&symbols={symbols}'
        headers = {
            'content-type': 'application/json',
            'Apca-Api-Key-Id': api_key,
            'Apca-Api-Secret-Key': api_secret
        }
        response = requests.get(url, headers=headers)
        print(response)
        
        if response.status_code != 200:
            return {"error": response.text}, response.status_code
        
        response_dict = response.json()
        return response_dict, 200
