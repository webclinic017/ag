from enum import Enum


class Channel(Enum):
    Trades  = 'trades'
    Quotes  = 'quotes'
    Bars    = 'bars'
    Account = 'account'