from sklearn.linear_model import LinearRegression
from statsmodels.tsa.stattools import adfuller
import yfinance as yf

start_date = "2018-02-27"
end_date = "2019-03-02"

stock1 = "PETR3.SA"
stock2 = "PETR4.SA"

#pegamos o dataframe das ações
df = yf.download([stock1, stock2], start= start_date, end= end_date) ['Adj Close']
df.columns=['PETR3', 'PETR4']

#Regressão Linear
x_independent = df.iloc[:,1].values.reshape(-1, 1)
#variável independente x (posição do index1, que no caso é PETR4)
y_dependent = df.iloc[:,0].values.reshape(-1, 1)
#variavel dependente y (posição do index0, que no caso é PETR3)

reg = LinearRegression().fit(x_independent, y_dependent)

#valor estimado de Y dado X do modelo
y_predict = reg.predict(x_independent)

#Resíduo
df['Residual'] = y_dependent - y_predict

#Tesde Dickey-Fuller (da biblioteca statsmodels.tsa.stattols)
test_series = adfuller(df['Residual'])
print ('ADF Statistic: %f' % test_series[0]) 
"""valor do teste estatístico, para o teste de estacionariedade, quanto mais negativo o resultado
maiores as chances da série ser estacionaria"""

print ('p-value: %f' % test_series[1])
"""valor de p pode ser usado para calcular a confiabilidade em porcentagem pela
fórmula -> Confiabilidade(%) = (1-p-value) * 100
confiabilidade acima de 95% é suficiente para analise"""

print ('Critical values:')

for key, value in test_series[4].items():
    print('\t%s: %.3f' % (key, value))

confidence = 1 - test_series[1]
print (f'Confidence: {confidence:.2%}')

