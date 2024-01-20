import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt


def draw_plot():

  # read CSV
  df = pd.read_csv('epa-sea-level.csv')
  df.head()

  # scatter plot
  df.plot(kind='scatter', x = 'Year', y ='CSIRO Adjusted Sea Level')

  # line of best fit
  lbf = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
  x_pred = pd.Series([i for i in range (1880,2050)])
  y_pred = lbf.slope*x_pred + lbf.intercept
  plt.plot(x_pred,y_pred, 'red')

  # line of best fit 2
  df2 = df.loc[df['Year'] >= 2000]
  lbf2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
  x_pred2 = pd.Series([i for i in range(2000,2050)])
  y_pred2 = lbf2.slope*x_pred2 + lbf2.intercept
  plt.plot(x_pred2,y_pred2, 'Blue')

  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level ')

  # save fig
  plt.savefig('sea_level_plot.png')
  return plt.gca()

draw_plot()
