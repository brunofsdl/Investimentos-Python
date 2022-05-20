import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import yfinance as yf


#INICIANDO A CARTEIRA 1
tickers1 = ['VALE3.SA', 'JBSS3.SA', 'CIEL3.SA']

mydata1 = pd.DataFrame()
for t in tickers1:
    mydata1[t] = wb.DataReader(t, data_source='yahoo', start='2017-01-19', end='2022-01-19')['Adj Close']

mydata1.rename(columns={'VALE3.SA': 'VALE3',
                        'JBSS3.SA': 'JBSS3',
                        'CIEL3.SA': 'CIEL3'}, inplace=True)

print (mydata1)
mydata1_config = mydata1 / mydata1.iloc[0] *100 #fazemos *100 para normalizar os dados

print (mydata1_config.plot(figsize=(15,6)))
print (plt.show())

carteira1 = {'VALE3': 10000, 'JBSS3': 10000, 'CIEL3': 10000}
    #criando o dicionário da carteira com o valor das compras de cada ação

carteira_df1 = pd.Series(data=carteira1, index=list(carteira1.keys()))

print (sum(carteira1.values())) #mostrando valor total da carteira

#pegando o preço dos ativos no primeiro dia do investimento
primeiro1 = mydata1.iloc[0]
qtd_acoes1 = carteira_df1/primeiro1
PL1 = mydata1 * qtd_acoes1

print (PL1.head(3))
print (PL1.tail(3))

#colocando coluna que contem a posição consolidada da carteira diariamente
PL1['Carteira 1'] = PL1.iloc[:].sum(axis = 1)
print (PL1.head())
print (PL1.tail())



#INICIANDO A CARTEIRA 2
tickers2 = ['VALE3.SA', 'JBSS3.SA', 'ABEV3.SA']

mydata2 = pd.DataFrame()
for t in tickers2:
    mydata2[t] = wb.DataReader(t, data_source='yahoo', start='2017-01-19', end='2022-01-19')['Adj Close']

mydata2.rename(columns={'VALE3.SA': 'VALE3',
                        'JBSS3.SA': 'JBSS3',
                        'ABEV3.SA': 'ABEV3'}, inplace=True)

print (mydata2)
mydata2_config = mydata2 / mydata2.iloc[0] *100 #fazemos *100 para normalizar os dados

print (mydata2_config.plot(figsize=(15,6)))
print (plt.show())

carteira2 = {'VALE3': 10000, 'JBSS3': 10000, 'ABEV3': 10000}
    #criando o dicionário da carteira com o valor das compras de cada ação

carteira_df2 = pd.Series(data=carteira2, index=list(carteira2.keys()))

print (sum(carteira2.values())) #mostrando valor total da carteira

#pegando o preço dos ativos no primeiro dia do investimento
primeiro2 = mydata2.iloc[0]
qtd_acoes2 = carteira_df2/primeiro2
PL2 = mydata2 * qtd_acoes2

print (PL2.head(3))
print (PL2.tail(3))

#colocando coluna que contem a posição consolidada da carteira diariamente
PL2['Carteira 2'] = PL2.iloc[:].sum(axis = 1)
print (PL2.head())
print (PL2.tail())

#INICIANDO A CARTEIRA 3
tickers3 = ['VALE3.SA', 'JBSS3.SA', 'JHSF3.SA']

mydata3 = pd.DataFrame()
for t in tickers3:
    mydata3[t] = wb.DataReader(t, data_source='yahoo', start='2017-01-19', end='2022-01-19')['Adj Close']

mydata3.rename(columns={'VALE3.SA': 'VALE3',
                        'JBSS3.SA': 'JBSS3',
                        'JHSF3.SA': 'JHSF3'}, inplace=True)

print (mydata3)
mydata3_config = mydata3 / mydata3.iloc[0] *100 #fazemos *100 para normalizar os dados

print (mydata3_config.plot(figsize=(15,6)))
print (plt.show())

carteira3 = {'VALE3': 10000, 'JBSS3': 10000, 'JHSF3': 10000}
    #criando o dicionário da carteira com o valor das compras de cada ação

carteira_df3 = pd.Series(data=carteira3, index=list(carteira3.keys()))

print (sum(carteira3.values())) #mostrando valor total da carteira

#pegando o preço dos ativos no primeiro dia do investimento
primeiro3 = mydata3.iloc[0]
qtd_acoes3 = carteira_df3/primeiro3
PL3 = mydata3 * qtd_acoes3

print (PL3.head(3))
print (PL3.tail(3))

#colocando coluna que contem a posição consolidada da carteira diariamente
PL3['Carteira 3'] = PL3.iloc[:].sum(axis = 1) #axis indica a posição da coluna, sendo 1 na direita
#iloc é usado para extrarir as linhas usando a posição, no caso : é pra pegar todos os dados e não
#de uma posição especifica
print (PL3.head())
print (PL3.tail())


#CRIANDO A COMPARAÇÃO ENTRE CARTEIRAS 1 e 2
novo_df12 = pd.merge(PL1, PL2, how = 'inner', on = 'Date')

PL_normalizado12 = novo_df12 / novo_df12.iloc[0] *100
print (PL_normalizado12.head())
print (PL_normalizado12.tail())

#plotando a carteira 1 vs carteira 2
PL_normalizado12[['Carteira 1', 'Carteira 2']].plot(figsize = (15,6))
print (plt.show())

#CRIANDO A COMPARAÇÃO ENTRE CARTEIRAS 1, 2 e 3
novo_df3 = pd.merge(PL_normalizado12, PL3, how = 'inner', on = 'Date')

PL_normalizado3 = novo_df3 / novo_df3.iloc[0] *100
print (PL_normalizado3.head())
print (PL_normalizado3.tail())

#plotando a carteira 1 vs carteira 2 vs carteira 3
PL_normalizado3[['Carteira 1', 'Carteira 2', 'Carteira 3']].plot(figsize = (15,6))
print (plt.show())
