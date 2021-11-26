# -*- coding: utf-8 -*-

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot

def parser(x):
	return datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
 
series = read_csv('ALGN-2021-01-19 .csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
series = series.drop(columns=['volume'])
print(series.head())
series.plot()
pyplot.show()

#autocorrelation
autocorrelation_plot(series)
pyplot.show()
#this shows ahtat there is a significant correlation in data up until 10 (pos!)


