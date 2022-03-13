from datetime import datetime
from attr import dataclass


@dataclass
class Quote:
    ask_price: float
    bid_price: float
    ask_size: float
    bid_size: float
    symbol: str
    timestamp: datetime