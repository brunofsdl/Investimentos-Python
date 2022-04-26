import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt

tickers = ['ABEV3.SA', 'JBSS3.SA', 'ITUB4.SA', 'B3SA3.SA', 'VALE3.SA', 'SUZB3.SA', 'TAEE11.SA', 'SULA11.SA', 'BRML3.SA', 'MULT3.SA'] #pedimos os ativos para criar carteira e comparar

database = pd.DataFrame()
for t in tickers:
    database[t] = web.DataReader(t, data_source='yahoo', start='2022-01-01', end='2022-12-04')['Adj Close']


print (database)
database_config = database / database.iloc[0] *100 #fazemos *100 para normalizar os dados de retorno

print (database_config.plot(figsize=(15,6)))
print (plt.show())

