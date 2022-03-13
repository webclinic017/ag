from broker import Broker


class Currencycom(Broker):
    def __init__(self, name: str, api_key: str, api_secret: str, api_url: str, paper: bool) -> None:
        super().__init__(name, api_key, api_secret, api_url, paper)