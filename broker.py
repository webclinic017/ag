from typing import List
from channel import Channel
from order import Order
from quote import Quote


class Broker:
    def __init__(self, name: str, api_key: str, api_secret:str, api_url: str, paper:bool) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_url = api_url
        self.paper = paper
        self.name = name
        self.socket = None
        self.api = None


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


    def cancel_order(id:str):
        pass


    def subscribe(self, channels: List[Channel], topics: List[str] = None):
        pass


    def subscribe_quotes(self):
        pass


    def subscribe_trades(self):
        pass


    def subscribe_bars(self):
        pass


    def subscribe_account(self):
        pass


    def parse_quote(self, quote) -> Quote:
        pass


    def parse_order(self, order) -> Order:
        pass