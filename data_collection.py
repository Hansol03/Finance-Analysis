import yfinance as yf 
import pandas as pd

stock_data = yf.download('AAPL', start='2020-01-01', end='2024-12-31')
print(stock_data.head())