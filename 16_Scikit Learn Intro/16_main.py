import quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# svm - support vector machine
# preprocessing - cpnvert data to a range -1, 1
# cross_validation - create test and training sets
from sklearn import svm, preprocessing, cross_validation


style.use('fivethirtyeight')

api_key = open('apikey.txt').read()


def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1.0
    else:
        return 0.0


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
# output = housing_data.reindex(columns=['Value', 'M30', 'sp500', 'GDP', 'Unemployment Rate',
#                                        'US_HPI', 'US_HPI_future', 'Label', 'ma_apply_example'])
print(housing_data.tail())
housing_data = housing_data.tail(50)  # Last 50

X = np.array(housing_data.drop(['Label', 'US_HPI_future'], 1))
X = preprocessing.scale(X)
y = np.array(housing_data['Label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.4)  # 40%

clf = svm.SVC(kernel='linear').fit(X_train, y_train)

print(X_train, X_test, y_train, y_test)
print('Accuracy: ', clf.score(X_test, y_test))
