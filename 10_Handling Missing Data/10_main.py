import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

api_key = open('apikey.txt').read()


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]



def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.columns = [str(abbv)]
        # df = df.pct_change()
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    # with open('fiddy_state.pickle', 'wb') as f:
    #     pickle.dump(main_df, f)
    #     f.close()
    main_df.to_pickle('pickle_pandas_2.pickle')


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    return df


fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))
HPI_data = pd.read_pickle('pickle_pandas_2.pickle')

# D - daily h - hourly A - Yearly  by the mean - на середню величину
TX1year = HPI_data['TX1year'] = HPI_data['TX'].resample('A').mean()  #.ohlc() - open high low close
print(HPI_data[['TX', 'TX1year']].head())

# HPI_data.dropna(inplace=True)
# HPI_data.dropna(inplace=True, how='all')  # whel all data in all columns is NaN
# HPI_data.fillna(method='bfill', inplace=True)  # Forward ffill - Backward - bfill. Fill by previous numbers
HPI_data.fillna(value=-9999, inplace=True, limit=2)  # fill NaN by a number  HAS a option limit=

print('NaN numbers :', HPI_data.isnull().values.sum())

print(HPI_data[['TX', 'TX1year']].head())

HPI_data[['TX', 'TX1year']].plot(ax=ax1)

plt.legend(loc=4)
# 1 0x    2 x0    3 00    4 00
#   00      00      x0      0x

plt.show()
