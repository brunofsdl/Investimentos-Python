import pandas as pd
import seaborn as sn
import yfinance as yf
import matplotlib.pyplot as plt


tickers = ['ABEV3.SA', 'JBSS3.SA', 'ITUB4.SA', 'B3SA3.SA', 'VALE3.SA', 'SUZB3.SA', 'TAEE11.SA', 'SULA11.SA', 'BRML3.SA', 'MULT3.SA']

prices = pd.DataFrame()

for t in tickers:
    prices[t] = yf.download(t, start='2022-01-01', end='2022-12-04')['Adj Close']

retornos = prices.pct_change()

#renomear
retornos.rename(columns={'ABEV3.SA': 'ABEV3', 'JBSS3.SA':'JBSS3'}, inplace=True)

#correlação
correlation = retornos.corr()

#plot
plot = sn.heatmap(correlation, annot = True, fmt=".1f", linewidths=.6)
print(plt.show())

