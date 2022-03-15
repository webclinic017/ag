from dataclasses import dataclass
from datetime import datetime


@dataclass
class Bar:
    open: float
    high: float
    low: float
    close: float
    timestamp: datetime