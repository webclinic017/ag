from datetime import datetime
from broker import Broker
from channel import Channel


class Agent():
    def __init__(self, symbol:str, broker:Broker, debug:bool=True) -> None:
        self.symbol = symbol
        self.broker = broker
        self.debug = debug


    def start(self):
        self.broker.init(
            rest_api=True, 
            socket=True
        )
        self.broker.subscribe(
            channels=['bars'],
            topics=[self.symbol],
            quotes_cb=self.handle_quotes,
            bars_cb=self.handle_bars
        )
        self.broker.start()


    async def handle_quotes(self, quote):
        q = self.broker.parse_quote(quote)
        self.log('QUOTE', f'ask: {q.ask_price}, bid: {q.bid_price}')


    async def handle_bars(self, bar):
        b = self.broker.parse_bar(bar)
        self.log('BAR', f'close: {b.close}, ts: {b.timestamp}')
    

    async def handle_trades(self, trade):
        pass


    async def handle_updates(self, event):
        pass

    def log(self, tag:str, message:str):
        if not self.debug:
            return
        ts = datetime.now().strftime('%m-%d %H:%M:%S.%f')
        print(f'[{ts}][{tag}]: {message}')
