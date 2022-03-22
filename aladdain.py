from dataclasses import dataclass
from typing import List
from agent import Agent
from brokers.alpaca import Alpaca

@dataclass
class agent_data:
    broker: str
    symbol: str


class Bot:
    def __init__(self) -> None:
        self.agents_data:List(agent_data) = [
            agent_data(
                broker='alpaca',
                symbol='ETHUSD'
            )
        ]


    def start_agent(self, agent:agent_data):
        pass


    def start(self):
        for _agent in self.agents_data:
            start_agent(_agent)
            


def start_agent(symbol:str, broker_name: str):
    if broker_name == 'alpaca':
        broker = Alpaca(paper=True)
    
    agent = Agent(symbol, broker)
    agent.start()



if __name__ == '__main__':
    # start agents here
    # one or multiple agent 
    # one symbol and one broker per agent
    start_agent('ETHUSD', 'alpaca')