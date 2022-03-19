from typing import List
from bar import Bar
from channel import Channel
from order import Order
from quote import Quote


class Broker:
    def __init__(self, name: str, api_key: str, api_secret:str, api_url: str, paper:bool, shorting_allowed:bool=True) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_url = api_url
        self.paper = paper
        self.name = name
        self.socket = None
        self.api = None
        self.shorting_allowed = shorting_allowed


    def init(self, rest_api:bool=True, socket:bool=True):
        if rest_api:
            self.init_rest_api()
        if socket:
            self.init_socket()


    def init_rest_api(self):
        pass


    def init_socket(self):
        pass


    def start(self):
        pass


    def submit_order(self, symbol:str, side: str, qty: int, type: str = 'market', time_in_force: str = 'day', limit: float = None, stop: float = None):
        pass


    def cancel_order(self, id:str):
        pass


    def subscribe(self, channels: List[str], topics:List[str]= None, quotes_cb=None, bars_cb=None, trades_cb=None, account_cb=None):
        for ch in channels:
            if ch == 'quotes':
                self.subscribe_quotes(symbols=topics, cb=quotes_cb)
            elif ch == 'bars':
                self.subscribe_bars(symbols=topics, cb=bars_cb)
            elif ch == 'trades':
                self.subscribe_trades(symbols=topics, cb=trades_cb)
            elif ch == 'account':
                self.subscribe_account(cb=account_cb)
            


    def subscribe_quotes(self, cb, symbols):
        pass


    def subscribe_trades(self, cb, symbols):
        pass


    def subscribe_bars(self, cb, symbols):
        pass


    def subscribe_account(self, cb):
        pass


    def parse_quote(self, quote) -> Quote:
        pass


    def parse_order(self, order) -> Order:
        pass


    def parse_bar(self, bar) -> Bar:
        pass