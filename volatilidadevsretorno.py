""" IMPORTANTE QUE NESTE CASO, O RISCO TA SENDO ADOTADO COMO A VOLATILIDADE
QUE É CALCULADA COM O DESVIO PADRÃO DOS RETORNOS DIARIOS"""
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['ABEV3.SA', 'JBSS3.SA', 'ITUB4.SA', 'B3SA3.SA', 'VALE3.SA', 'SUZB3.SA', 'TAEE11.SA', 'SULA11.SA', 'BRML3.SA', 'MULT3.SA']

prices = pd.DataFrame()

for t in tickers:
    prices[t] = yf.download(t, start='2022-01-01', end='2022-12-04',progress=False)['Adj Close']

returns = prices.pct_change()

volatility = pd.DataFrame(returns.std(), columns=['Vol'])
m_returns = pd.DataFrame(returns.mean(), columns = ['Returns'])
vol_return = pd.concat([m_returns, volatility], axis=1)
vol_return.insert(loc=0, column = 'Company', value = tickers)

print(vol_return.head())

fig, ax = plt.subplots()

for index, vol in vol_return.iterrows():
  ax.scatter(x='Vol', y = 'Returns', label=vol['Company'], data=vol)

legend = ax.legend(tickers, loc=1 , title= "STOCKS", bbox_to_anchor=(1.2, 1), ncol=2)

ax.set_title('Matriz de Retorno e Volatilidade')
ax.set_xlabel("Volatilidade")
ax.set_ylabel("Retorno")
fig.set_figheight(6)
fig.set_figwidth(10)
#ax.set_facecolor('#4B0082')
#fig.patch.set_facecolor('#4B0082')

print(plt.show())


