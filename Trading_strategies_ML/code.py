import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

#import data



#Trading Strategies
class CoveredCall:
    def __init__(self, initial_stock_price, strike_price, premium):
        self.initial_stock_price = initial_stock_price
        self.strike_price = strike_price
        self.premium = premium

    def payoff(self, final_stock_price):
        #Rappel covered call --> long sur stock et short sur call 
        stock_payoff = (final_stock_price - self.initial_stock_price)
        call_payoff = self.premium - (max(self.strike_price,final_stock_price) - self.strike_price)
        total_payoff = stock_payoff + call_payoff
        total_payoff = self.premium + (final_stock_price - self.initial_stock_price)
        return total_payoff


chose = 150  # Prix initial de l'action 
call_strike_price = 160    # Prix d'exercice de l'option d'achat
call_premium = 2          # Prime de l'option d'achat
stock_quantity = 100       # Nombre d'actions détenues

covered_call_strategy = CoveredCall(chose, call_strike_price, call_premium)

# Simuler une variation du prix de l'action Apple
final_stock_price = 155  # Nouveau prix de l'action Apple

# Calcul du profit ou de la perte de la stratégie
profit_loss = covered_call_strategy.calculate_payoff(final_stock_price)
print(f"Profit/Loss at {final_stock_price}: {profit_loss}")
