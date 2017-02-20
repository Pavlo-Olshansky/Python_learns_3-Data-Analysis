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
TX1year = HPI_data['TX'].resample('A').mean()  #.ohlc() - open high low close
print(TX1year)

HPI_data['TX'].plot(ax=ax1, label='Mounthly TX HPI', color='b')
TX1year.plot(ax=ax1, label='Yearly', color='r')

plt.legend(loc=4)
# 1 0x    2 x0    3 00    4 00
#   00      00      x0      0x

plt.show()
# HPI_State_Correlation = HPI_data.corr()
