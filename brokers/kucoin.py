from broker import Broker
from kucoin.client import Trade as KucoinClient
from kucoin.ws_client import KucoinWsClient
from kucoin.client import WsToken

class Kucoin(Broker):
    def __init__(self, paper: bool) -> None:
        super().__init__(
            name='Kucoin', 
            api_key='622d45732b968a0001531f58', 
            api_secret='44cca221-9e12-425c-b622-69256fa5cd68', 
            api_url='https://openapi-sandbox.kucoin.com', 
            paper=paper
        )
        self.passphrase = 'kazanova'

    
    def init_rest_api(self):
        self.api = KucoinClient(
            key=self.api_key, 
            secret=self.api_secret, 
            is_sandbox=self.paper, 
            url=self.api_url,
            passphrase=self.passphrase
        )


    def init_socket(self):
        client = WsToken(
            key=self.api_key,
            secret=self.api_secret,
            passphrase=self.passphrase,
            url=self.api_url,
            is_sandbox=self.paper
        )
        self.socket = KucoinWsClient.create(
            loop=None,
            client=client,
            private=True,
            callback=None
        )


    def subscribe_quotes(self):
        pass


    def submit_order(self, symbol: str, side: str, qty: int, type: str = 'market', time_in_force: str = 'day', limit: float = None, stop: float = None, margin:bool=False):
        return self.api.create_market_order(
            symbol=symbol, 
            side=side, 
            size=qty, 
            type=type
        )