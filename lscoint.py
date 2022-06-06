from sklearn.linear_model import LinearRegression
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import yfinance as yf

start_date = "2018-02-27"
end_date = "2019-03-02"

stock1 = "PETR3.SA"
stock2 = "PETR4.SA"

#pegamos o dataframe das ações
df = yf.download([stock1, stock2], start= start_date, end= end_date) ['Adj Close']
df.columns=['PETR3', 'PETR4']
#print(df)

#plotamos os pares junto com as médias para analisarmos visualmente
"""mean_PETR3 = df['PETR3'].mean()
mean_PETR4 = df['PETR4'].mean()

df[['PETR3', 'PETR4']].plot(linewidth=1)
plt.axhline(y=mean_PETR3, color='blue', linestyle='--', linewidth=0.5)
plt.axhline(y=mean_PETR4, color='green', linestyle='--', linewidth=0.5)
plt.title("PETR3/PETR4")

print(plt.show())"""

#correlação simples
correlation = df.corr()
print (correlation)

#gráfico scatter para inicializar método de cointegração
"""plt.scatter(df['PETR4'], df['PETR3'], s=5)
plt.xlabel("PETR4")
plt.ylabel("PETR3")
print (plt.show())"""

#Regressão Linear
x_independent = df.iloc[:,1].values.reshape(-1, 1)
#variável independente x (posição do index1, que no caso é PETR4)
y_dependent = df.iloc[:,0].values.reshape(-1, 1)
#variavel dependente y (posição do index0, que no caso é PETR3)

reg = LinearRegression().fit(x_independent, y_dependent)

#Beta
beta = reg.coef_;
print ("beta = %f" % beta)

#coeficiente b (beta * x + b) da regressão linear
b = reg.intercept_;
print ("b = %f" % b)

#valor estimado de Y dado X do modelo
y_predict = reg.predict(x_independent)

#plotando modelo linear com os dados
"""plt.scatter(x_independent, y_dependent, s=5)
plt.plot(x_independent, y_predict, color='red', label="Modelo Linear")
plt.xlabel("PETR4")
plt.ylabel("PETR3")
plt.legend()
print (plt.show())"""

#Resíduo
df['Residual'] = y_dependent - y_predict
print (df)

#verificamos se o resíduo é estacionário graficamente
mean = df['Residual'].mean()
std = df['Residual'].std()

#deslocamento do desvio padrão
k = 2 

#linhas de deslocamento
up = mean + std * k
down = mean - std * k

#plotando o resíduo
"""plt.title("Residual")
df['Residual'].plot(x="Major", y="", label='_nolengend_')
plt.axhline(y=mean, color='black', linestyle='--', linewidth=1, label='Mean')
plt.axhline(y=up, color='purple', linestyle='--', linewidth=1, label=f'+/-{k} STD')
plt.axhline(y=down, color='purple', linestyle='--', linewidth=1, label='_nolegend_')
plt.legend(loc='upper right', ncol=2)
print (plt.show())"""

#vamos buscar uma série estacionária, dividindo a série por 2 e calculando a média e a variancia
split = int(len(df.Residual) / 2)
s1, s2 = df.Residual[0:split], df.Residual[split:]
mean1, mean2 = s1.mean(), s2.mean()
var1, var2 = s1.var(), s2.var()
print("mean1= %f, mean2= %f" % (mean1, mean2))
print('variance1= %f, variance2= %f' % (var1, var2))

"""No exemplo, as médias tem o mesmo valor e as variancias estão na mesma
ordem de magnitude, sugerindo que a série pode ser estacionária"""



