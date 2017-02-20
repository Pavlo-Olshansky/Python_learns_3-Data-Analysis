import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

# style.use('ggplot')

# import pandas.io.data as wed
#
# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2015, 1, 1)
#
# df = wed.DataReader('XOM', 'yahoo', start, end)
# print(df.head())  # TOP 5
# df['Adj Close'].plot()
# plt.show()

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 53, 43, 34],
             'Bounce_Rate': [65, 43, 43, 23, 54, 65]}
stats = pd.DataFrame(web_stats)
# print(stats)
# print(stats.head(2))  # First 2
# print(stats.tail(2))  # Last_ 2

# print(stats.set_index('Day'))
stats.set_index('Day', inplace=True)
print(stats)
print(stats['Visitors'])
print(stats.Visitors)

print(stats[['Bounce_Rate', 'Visitors']])

print('tolist : ------', stats.Visitors.tolist())
print(stats['Visitors'].tolist())

print('array : ------', np.array(stats[['Bounce_Rate', 'Visitors']]))
stats_2 = pd.DataFrame(np.array(stats[['Bounce_Rate', 'Visitors']]))
print('Stats_2: ', stats_2)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
x = int(input("Please enter a number: "))
