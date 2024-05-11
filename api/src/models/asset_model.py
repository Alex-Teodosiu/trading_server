class Asset:
    def __init__(self, id, asset_class, exchange, symbol, name, status, tradable, marginable, maintenance_margin_requirement, shortable, easy_to_borrow, fractionable):
        self.id = id
        self.asset_class = asset_class
        self.exchange = exchange
        self.symbol = symbol
        self.name = name
        self.status = status
        self.tradable = tradable
        self.marginable = marginable
        self.maintenance_margin_requirement = maintenance_margin_requirement
        self.shortable = shortable
        self.easy_to_borrow = easy_to_borrow
        self.fractionable = fractionable

    def to_dict(self):
        return {
            'id': self.id,
            'asset_class': self.asset_class,
            'exchange': self.exchange,
            'symbol': self.symbol,
            'name': self.name,
            'status': self.status,
            'tradable': self.tradable,
            'marginable': self.marginable,
            'maintenance_margin_requirement': self.maintenance_margin_requirement,
            'shortable': self.shortable,
            'easy_to_borrow': self.easy_to_borrow,
            'fractionable': self.fractionable
        }
