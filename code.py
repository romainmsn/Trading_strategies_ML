import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

#import data



#Different Trading Strategies
class CoveredCall:
    def __init__(self, initial_stock_price, strike_price, premium):
        self.initial_stock_price = initial_stock_price
        self.strike_price = strike_price
        self.premium = premium

    def payoff_CoveredCall(self, final_stock_price):
        #Rappel covered call --> long sur stock et short sur call 
        stock_payoff = (final_stock_price - self.initial_stock_price)
        call_payoff = self.premium - max(0,final_stock_price- self.strike_price)
        total_payoff = stock_payoff + call_payoff
        return total_payoff

class CoveredPut:
    def __init__(self, initial_stock_price, strike_price, premium):
        self.initial_stock_price = initial_stock_price
        self.strike_price = strike_price
        self.premium = premium
    
    def payoff_CoveredPut(self, final_stock_price):
        #Rappel covered put --> short sur stock et short sur put 
        total_payoff = self.initial_stock_price - final_stock_price - max(0,self.strike_price-final_stock_price) +self.premium
        return total_payoff

class ProtectiveCall:
    def __init__(self,initial_stock_price, strike_price, premium):
        self.initial_stock_price = initial_stock_price
        self.strike_price = strike_price
        self.premium = premium

    def payoff_ProtectiveCall(self, final_stock_price):
        #Rappel protective call --> long call et short ss jacent
        total_payoff = self.initial_stock_price - final_stock_price + max(0,final_stock_price-self.strike_price) - self.premium
        return total_payoff 

class ProtectivePut:
    def __init__(self,initial_stock_price, strike_price, premium):
        self.initial_stock_price = initial_stock_price
        self.strike_price = strike_price
        self.premium = premium

    def payoff_ProtectivePut(self, final_stock_price):
        #Rappel protective put --> long put et ss jacent
        total_payoff = final_stock_price -self.initial_stock_price + max(0,self.strike_price-final_stock_price) - self.premium
        return total_payoff
    

class BullCallSpread:
    def __init__(self,initial_stock_price, strike_price_1, strike_price_2, premium_1, premium_2):
        self.initial_stock_price = initial_stock_price
        self.strike_price_1 = strike_price_1
        self.strike_price_2 = strike_price_2 #strike_price_1 < strike_price_2
        self.premium_1 = premium_1
        self.premium_2 = premium_2
    
    def payoff_BullCall_Spread(self, final_stock_price)
        #Rappel Bull Call Spread --> long call K1, short call K2, K1<K2
        total_payoff = max(0,final_stock_price - self.strike_price_1) - max(0,final_stock_price - self.strike_price_2) - self.premium_1 + self.premium_2
        return total_payoff

#test
