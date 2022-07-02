# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13GcDPrbdEhYP-lp1BkZEaY0pUYaCQSAk
"""

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.linear_model import LinearRegression

pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('/content/drive/MyDrive/inflation.csv',
                 parse_dates=["Month"])
df.head()

df['Series ID'].value_counts()

df.describe()

df.info()

df.Value.plot.hist()

df['Year'] = df['Month'].dt.year

df.head()

df.tail()

df.head()

df["Item"].replace({"CUSR0000SA0": "All Item",
                    "CUSR0000SETB01": "Gasoline",
                    "CUSR0000SAF1":"Food",
                    "CUSR0000SETA02": "UsedCars & Trucks"}, inplace=True)
df.head()

df.head()

with sns.axes_style("whitegrid"):
    sns.lmplot(data=df,
               x='Year',
               y='Value',
               hue='Item',
               lowess=True, 
               aspect=2,
               scatter_kws={'alpha': 0.5},
               line_kws={'linewidth': 5})
 
plt.show()