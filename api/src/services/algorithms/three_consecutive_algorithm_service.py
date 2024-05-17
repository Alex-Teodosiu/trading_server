import time
import alpaca_trade_api as tradeapi
from ..order_service import OrderService

class ThreeConsecutiveAlgorithmService:
    def __init__(self):
        self.order_service = OrderService()

    def trade_algorithm(self, user_id, symbol, qty):
        try:
            trading_account = self.order_service._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            client = tradeapi.REST(api_key, secret_key, "https://paper-api.alpaca.markets", api_version='v2')

            # Fetch recent market data
            barset = client.get_barset(symbol, 'minute', limit=5)
            bars = barset[symbol]

            if len(bars) < 5:
                return {"error": "Not enough data to make a decision"}

            # Simple momentum strategy
            if bars[-1].c > bars[-2].c and bars[-2].c > bars[-3].c:
                response = self.order_service.create_order(user_id, symbol, qty, 'buy')
            elif bars[-1].c < bars[-2].c and bars[-2].c < bars[-3].c:
                response = self.order_service.create_order(user_id, symbol, qty, 'sell')
            else:
                response = {"message": "No trade made"}

            return response
        except Exception as e:
            return {"error": str(e)}

    def run_algorithm(self, user_id, symbol, qty, interval=60):
        while True:
            response = self.trade_algorithm(user_id, symbol, qty)
            print(response)
            time.sleep(interval)
