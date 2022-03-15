from pandas import Series
import pandas as pd
import numpy as np

from bar import Bar


class Indicator:
    def __init__(self) -> None:
        self.df = None


    def append(self, bar:Bar):
        pass


    def ema(self, source:Series, length:int):
        return source.ewm(span=length).mean()
        

    def smooth(self, smooth_factor:int=10):
        pass


    def crossover(self):
        pass 