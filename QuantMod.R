install.packages('quantmod')
library('quantmod')
getSymbols("AMZN")

barChart(AMZN, subset = "last 90 days")

chartSeries(AMZN, subset = "last 90 days")

barChart(AMZN['2013-04-01::2013-04-12'])

