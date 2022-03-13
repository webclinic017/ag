from broker import Broker


class Agent():
    def __init__(self, symbol:str, broker:Broker) -> None:
        self.symbol = symbol
        self.broker = broker