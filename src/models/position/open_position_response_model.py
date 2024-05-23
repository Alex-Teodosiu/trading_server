from enum import Enum
from uuid import UUID

class AssetClass(Enum):
    CRYPTO = 'crypto'
    US_EQUITY = 'us_equity'

class AssetExchange(Enum):
    CRYPTO = 'CRYPTO'
    US_EQUITY = 'US_EQUITY'
    ARCA = 'ARCA'
    BATS = 'BATS'
    OTC = 'OTC'
    NYSE = 'NYSE'
    NASDAQ = 'NASDAQ'
    AMEX = 'AMEX'

class PositionSide(Enum):
    LONG = 'long'
    SHORT = 'short'

class Position:
    def __init__(self, asset_class, asset_id, asset_marginable, avg_entry_price, avg_entry_swap_rate, change_today, cost_basis, current_price, exchange, lastday_price, market_value, qty, qty_available, side, swap_rate, symbol, unrealized_intraday_pl, unrealized_intraday_plpc, unrealized_pl, unrealized_plpc, usd):
        self.asset_class = asset_class
        self.asset_id = asset_id
        self.asset_marginable = asset_marginable
        self.avg_entry_price = avg_entry_price
        self.avg_entry_swap_rate = avg_entry_swap_rate
        self.change_today = change_today
        self.cost_basis = cost_basis
        self.current_price = current_price
        self.exchange = exchange
        self.lastday_price = lastday_price
        self.market_value = market_value
        self.qty = qty
        self.qty_available = qty_available
        self.side = side
        self.swap_rate = swap_rate
        self.symbol = symbol
        self.unrealized_intraday_pl = unrealized_intraday_pl
        self.unrealized_intraday_plpc = unrealized_intraday_plpc
        self.unrealized_pl = unrealized_pl
        self.unrealized_plpc = unrealized_plpc
        self.usd = usd

    def to_dict(self):
        return {
            'asset_class': self.asset_class.value,
            'asset_id': str(self.asset_id),
            'asset_marginable': self.asset_marginable,
            'avg_entry_price': self.avg_entry_price,
            'avg_entry_swap_rate': self.avg_entry_swap_rate,
            'change_today': self.change_today,
            'cost_basis': self.cost_basis,
            'current_price': self.current_price,
            'exchange': self.exchange.value,
            'lastday_price': self.lastday_price,
            'market_value': self.market_value,
            'qty': self.qty,
            'qty_available': self.qty_available,
            'side': self.side.value,
            'swap_rate': self.swap_rate,
            'symbol': self.symbol,
            'unrealized_intraday_pl': self.unrealized_intraday_pl,
            'unrealized_intraday_plpc': self.unrealized_intraday_plpc,
            'unrealized_pl': self.unrealized_pl,
            'unrealized_plpc': self.unrealized_plpc,
            'usd': self.usd,
        }