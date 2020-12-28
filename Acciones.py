#ROBOT DE TRADING RUBEN GUEVARA

# IMPORTAR ACCIONES DE alpha_vantage

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib
import matplotlib.pyplot as plt
#import os
# Make plots bigger
matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)
import pandas as pd
from datetime import datetime

ts = TimeSeries(key='FH69CNJPTEAVXKHO',output_format='pandas')

aapl, meta_data = ts.get_intraday(symbol='AAPL',interval='1min', outputsize='compact')
aapl = aapl.rename(columns = {'1. open':'open','2. high':'high','3. low':'low','4. close':'close','5. volume':'volume'})
print(aapl.head())