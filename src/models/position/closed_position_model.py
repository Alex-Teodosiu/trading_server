from typing import Optional, Union, Dict
from uuid import UUID
from src.models.order.order_response_model import OrderResponse

class FailedClosePositionDetails:
    pass

class ClosedPositionResponse:
    def __init__(self, order_id: Optional[UUID] = None, status: Optional[int] = None, symbol: Optional[str] = None):
        self.order_id = order_id
        self.status = status
        self.symbol = symbol

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'status': self.status,
            'symbol': self.symbol,
            'body': self.body
        }