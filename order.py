from enum import Enum
from attr import dataclass


class Side(Enum):
    BUY  = 'buy'
    SELL = 'sell'


class OrderStatus(Enum):
    Filled   = 'filled'
    Canceled = 'canceled'
    Pending  = 'pending'


@dataclass
class Order:
    id: str
    symbol: str
    side: Side
    status: OrderStatus