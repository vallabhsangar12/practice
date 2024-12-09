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





