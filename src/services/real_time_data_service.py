from alpaca.data.live import CryptoDataStream, StockDataStream
from src.config.dev_config import DevConfig
import asyncio

class RealTimeDataService:
    def __init__(self):
        config = DevConfig()
        self.api_key = config.ALPACA_API_KEY
        self.secret_key = config.ALPACA_API_SECRET
        self._crypto_websocket_client = CryptoDataStream(self.api_key, self.secret_key)
        self._stock_websocket_client = StockDataStream(self.api_key, self.secret_key)

    # async handler
    # Websocket
    async def stream_stock_data(self, symbol):
        async def quote_data_handler(data):
            print(data)

        self._stock_websocket_client.subscribe_quotes(quote_data_handler, symbol)
        await self._stock_websocket_client.run()


    async def stream_crypto_data(self, symbol):
        async def quote_data_handler(data):
            print(data)

        self._crypto_websocket_client.subscribe_quotes(quote_data_handler, symbol)
        await self._crypto_websocket_client.run()


    # asyncio.run(stream_stock_data('PKFYPB97OWCB1M3CVPBN', '9MkEQw9h0d7Pf79OvT14k8ludqOZt05JYaMF4DAd', 'SPY'))
