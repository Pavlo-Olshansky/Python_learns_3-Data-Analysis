import quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('fivethirtyeight')

api_key = open('apikey.txt').read()


def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0


def moving_average(values):
    ma = np.mean(values)
    return ma


housing_data = pd.read_pickle('HPI.pickle')
housing_data = housing_data.pct_change()

housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data["US_HPI"].shift(-1)

housing_data.dropna(inplace=True)
# print(housing_data[['US_HPI_future', 'United States']].head())
housing_data['Label'] = list(map(create_labels, housing_data['US_HPI'], housing_data['US_HPI_future']))

# housing_data['ma_apply_example'] = pd.rolling_apply(housing_data['M30'], 10, moving_average)  # Old version
housing_data['ma_apply_example'] = pd.Series.rolling(housing_data['M30'], window=10).apply(moving_average)
output = housing_data.reindex(columns=['Value', 'M30', 'sp500', 'GDP', 'Unemployment Rate',
                                       'US_HPI', 'US_HPI_future', 'Label', 'ma_apply_example'])
print(output.tail())
