#ROBOT DE TRADING RUBEN GUEVARA

# IMPORTAR ACCIONES DE alpha_vantage

#importar librerias
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

#llave de alpha_vantage
ts = TimeSeries(key='FH69CNJPTEAVXKHO',output_format='pandas')

#importar datos

#APPLE
aapl, meta_data = ts.get_intraday(symbol='AAPL',interval='1min', outputsize='full')
aapl = aapl.rename(columns = {'1. open':'open','2. high':'high','3. low':'low','4. close':'close','5. volume':'volume'})

#ALIBABA
baba, meta_data = ts.get_intraday(symbol='BABA',interval='1min', outputsize='full')
baba = baba.rename(columns = {'1. open':'open','2. high':'high','3. low':'low','4. close':'close','5. volume':'volume'})
print(aapl.head())

#FACEBOOK
fb, meta_data = ts.get_intraday(symbol='FB',interval='1min', outputsize='full')
fb = fb.rename(columns = {'1. open':'open','2. high':'high','3. low':'low','4. close':'close','5. volume':'volume'})

#NVIDIA
nvda, meta_data = ts.get_intraday(symbol='NVDA',interval='1min', outputsize='full')
nvda = nvda.rename(columns = {'1. open':'open','2. high':'high','3. low':'low','4. close':'close','5. volume':'volume'})

#MICROSOFT
msft, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
msft = msft.rename(columns = {'1. open':'open','2. high':'high','3. low':'low','4. close':'close','5. volume':'volume'})