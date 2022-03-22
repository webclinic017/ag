from pandas import DataFrame, Series
import pandas as pd
import numpy as np

from bar import Bar


class Indicator:
    def __init__(self) -> None:
        self.df:DataFrame = pd.DataFrame(columns=['open', 'high', 'low', 'close', 'timestamp'], index=None)


    def append(self, bar:Bar):
        self.df.loc[len(self.df)] = [bar.open, bar.low, bar.high, bar.close, bar.timestamp]
        print(self.df.head())


    def ema(self, source:Series, length:int) -> Series:
        return source.ewm(span=length).mean()

    
    def tema(self, source:Series, length:int) -> Series:
        e1 = self.ema(source, length)
        e2 = self.ema(e1, length)
        e3 = self.ema(e2, length)
        out = 3 * (e1 - e2) + e3
        return out


    def smooth(self, smooth_factor:int=10):
        pass


    def smoother(self, smooth_factor:int=0):
        pass


    def crossunder(self, s1:Series, s2:Series) -> Series:
        prev_s1 = s1.shift(1)
        prev_s2 = s2.shift(1)
        cross = (prev_s1 >= prev_s2) & (s1 <= s2)
        return cross


    def crossover(self, s1:Series, s2:Series) -> Series:
        prev_s1 = s1.shift(1)
        prev_s2 = s2.shift(1)
        cross = (prev_s1 <= prev_s2) & (s1 >= s2)
        return cross