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


#  Correlation
def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100
    return df


# fig = plt.figure()
ax1 = plt.subplot2grid((2, 1), (0, 0))  # розбиваєм сітку на 2 стовпці і 1 рядок а малюєм в 0 0
ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)  # sharex - divide OX (one for ax1 and ax2)
HPI_data = pd.read_pickle('pickle_pandas_2.pickle')
HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12)
HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12)
print(HPI_data[['TX', 'TX12MA', 'TX12STD']])

TX_AK_12corr = pd.rolling_corr(HPI_data['TX'], HPI_data['AK'], 12)  # Correlation
HPI_data['TX'].plot(ax=ax1, label='TX HPI')
HPI_data['AK'].plot(ax=ax1, label='AK HPI')


TX_AK_12corr.plot(ax=ax2, label='TX_AK_12corr')

# HPI_data['TX'].plot(ax=ax1)
HPI_data['TX12MA'].plot(ax=ax1, label='TX12MA')
HPI_data['TX12STD'].plot(ax=ax2, label='TX12STD')

ax1.legend(loc=2)
ax2.legend(loc=4)
plt.show()
