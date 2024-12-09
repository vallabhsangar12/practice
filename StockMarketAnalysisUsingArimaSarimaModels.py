#importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX


#define dated to fetch data
today = date.today()
print("TODAYS DATE:",today)
d1 =today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today()-timedelta(days=365)
d2 =d2.strftime("%Y-%m-%d")
start_date = d2
print("START DATE:",start_date)
print("END DATE:",end_date)

#Define ticker
ticker = 'GOOGL'
df = df.download(ticker,start=start_date,end= end_date, progress=False)
df.head()

df["Date"] = df.index
df.reset_index(drop= True, inplace= True)
df.columns
df.info()
df.insert(0, "Date" , df.index, True)
df.head()
df.describe()

#select columns
df = df[['Date','Close']]
df.head()

#figure
fig = px.line(df, x='Date',y='Close',title='Google stock price')
print(fig.show())
fig = px.line(df,x='Date',y=df.columns,title='stock price')
fig.show()

#stationarity check
from statsmodels.tsa.stattools import adfuller
def stationarity(df):
    result =adfuller(df)
    print('ADF staticstics:%f' %result[0])
    print('p-value:%f' %result[1])
    if result[1]<=0.05
     print("Data is stationary!")
    else:
     print("Data is not stationary!")
     check_stationarity(df['Close'])


#data visualizations
from statsmodels.tsa.seasonal   import  seasonal_decompose
decompose =  seasonal_decompose(df['Close'], model='additive', period=30)
decompose.plot()


from statsmodels.graphics.tsaplots import  plot_acf, plot_pacf
import matplotlib
#Original Series
fig, axes = plt.subplots(3,2, sharex=True)
axes[0,0].plot(df['Close']); axes[0,0].set_title('Original Series')
plot_acf (df['Close'], ax=axes[0,1])

#1 st order differencing 
axes [1,0].plot(df['Close'].diff().diff()); axes[1,0].set_title('1 st order differencing ')
plot_acf (df['Close'].diff().dropna(), ax=axes[1,1])

 #2nd order differencing 
axes [2,0].plot(df['Close'].diff().diff()); axes[2,0].set_title('1 st order differencing ')
plot_acf (df['Close'].diff().dropna(), ax=axes[2,1])


#find p value
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
pd.plotting.autocorrelation_plot(df['Close'])
plot_acf(df['Close'], alpha=0.05)
from statsmodels.tsa.stattools import acf,pacf
x_acf = pd.DataFrame(acf(df['Close']))
print(x_acf)


#partial autocorrection 
from statsmodels.tsa.stattools import   acf,pacf
plot_pacf(df['Close'], lags=20 , alpha=0.05)

#lets define p,d,q
p = 2
d = 1
q = 2

#lets run arima with pmdarima
from pmdarima.arima  import auto_arima
model = auto_arima (df['Close'],start_P= 2, start_q= 2, max_p=5, max_q =5, start_p=0, seasonal=True,d =1, D =1, trace=True, error_action='ignore', suppress_warnings=True)

model = auto_arima(df['Close'], seasonal=True,suppress_warnings=True)
print(model.summary())

# stats model and arima
from statsmodels.tsa.arima.model import ARIMA
p,d,q = 2 , 1, 2
model = ARIMA(df['Close'],order= (p,d,q))
model = model.fit()
print(model.summary())

#predict next 30 days
forecast = model.predict(n_periods=30)
print(forecast)

#plot forecast
plt.figure(figsize=(10,5))
plt.plot(df['Close'], label='Actual')
plt.plot(forecast, label='Forecast')


#lets run SARIMA
import statsmodels.api as sm
import warnings
p,d,q = 2,1,2
model = sm.tsa.statespace.SARIMAX(df['Close'], 
                                  order=(p,d,q),
                                  seasonal_order= (p,d,q,12))
model = model.fit()
print(model.summary())


predictions =  model.predict(start = len(df['Close']), end = len(df['Close'])+30) 

#plot predictions
plt.figure(figsize=(15,10))
plt.plot(df["Close"], label ='Actual')
plt.plot(predictions, color ='red',label='Predicted')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('GOOGLE STOCK PRICE')

#change legend location
plt.legend(loc='upper left')
plt.show()

#lets update p,d,q

#plot the prediction
plt.figure(figsize=(15,10))
plt.plot(df["Close"], label ='Actual' )
plt.plot(predictions, color='red', label='Predicted')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.ylabel('GOOGLE CLOSING PRICE')

#change  legend location
plt.legend(loc='upper left') 
plt.show()
