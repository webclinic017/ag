from datetime import datetime
from bar import Bar
from broker import Broker
from alpaca_trade_api.rest import REST
from alpaca_trade_api.stream import Stream
from order import Order, Side, OrderStatus
from quote import Quote

class Alpaca(Broker):
    def __init__(self, paper: bool) -> None:
        super().__init__(
            name='Alpaca', 
            api_key='PKJZ06PN3IZMEGHUOOQ5', 
            api_secret='ipLvRsG9eyfD0yBHwNb5kmwUcqubEUZSIPEmc0sC', 
            api_url='https://paper-api.alpaca.markets', 
            paper=paper,
            shorting_allowed=False
        )

    
    def init_rest_api(self):
        self.api = REST(
            key_id=self.api_key,
            secret_key=self.api_secret
        )


    def init_socket(self):
        self.socket = Stream(
            key_id=self.api_key,
            secret_key=self.api_secret,
            base_url=self.api_url,
        )


    def start(self):
        if self.socket:
            self.socket.run()


    def subscribe_quotes(self, cb, symbols):
        self.socket.subscribe_crypto_quotes(cb,  ','.join(symbols))


    def subscribe_trades(self, cb, symbols):
        self.socket.subscribe_crypto_trades(cb, ','.join(symbols))


    def subscribe_bars(self, cb, symbols):
        self.socket.subscribe_crypto_bars(cb, ','.join(symbols))


    def subscribe_account(self, cb):
        self.socket.subscribe_trade_updates(cb)


    def cancel_order(self, id: str):
        return self.api.cancel_order(id)


    def submit_order(self, symbol: str, side: str, qty: int, type: str = 'market', time_in_force: str = 'day', limit: float = None, stop: float = None):
        return self.api.submit_order(
            symbol=symbol,
            side=side,
            qty=qty,
            type=type,
            time_in_force=time_in_force,
            limit_price=limit,
            stop_price=stop
        )

    
    def parse_quote(self, quote) -> Quote:
        return Quote(
            ask_price=float(quote.ask_price),
            bid_price=float(quote.bid_price),
            bid_size=float(quote.bid_size),
            ask_size=float(quote.ask_size),
            symbol=quote.symbol,
            timestamp=quote.timestamp
        )

    
    def parse_order(self, order) -> Order:
        return Order(
            id=order.client_order_id,
            symbol=order.symbol,
            side=Side.BUY if order.side == 'buy' else Side.SELL,
            status=OrderStatus.Filled if order.status == 'filled' else OrderStatus.Canceled if order.status == 'canceled' else OrderStatus.Pending 
        )


    def parse_bar(self, bar) -> Bar:
        return Bar(
            open=float(bar.open),
            high=float(bar.high),
            low=float(bar.low),
            close=float(bar.close),
            timestamp=bar.timestamp
        )