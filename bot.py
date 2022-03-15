from agent import Agent
from brokers.alpaca import Alpaca


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