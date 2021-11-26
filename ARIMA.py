# -*- coding: utf-8 -*-
# fit an ARIMA model and plot residual errors
from pandas import datetime
from pandas import read_csv
from pandas import DataFrame
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot

# load dataset
def parser(x):
		return datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
series = read_csv('ALGN-2021-01-19 .csv', header=0, index_col=0, parse_dates=True, squeeze=True, date_parser=parser)
#series.index = series.index.to_period('M')
series = series.drop(columns=['volume'])
# fit model
model = ARIMA(endog=np.asarray(series.close), order=(150,10,0))
model_fit = model.fit()
# summary of fit model
print(model_fit.summary())
# line plot of residuals
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
# density plot of residuals
residuals.plot(kind='kde')
pyplot.show()
# summary stats of residuals
print(residuals.describe())