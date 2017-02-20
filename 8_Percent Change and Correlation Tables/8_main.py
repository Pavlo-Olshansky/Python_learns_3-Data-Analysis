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


# # grab_initial_state_data()
# fig = plt.figure()
# ax1 = plt.subplot2grid((1, 1), (0, 0))
#
HPI_data = pd.read_pickle('pickle_pandas_2.pickle')
#
# # HPI_data['TX'] *= 2
# # print(HPI_data['TX'])
# benchmark = HPI_Benchmark()
#
# HPI_data.plot(ax=ax1)
# benchmark.plot(ax=ax1, color='black', linewidth=10)
#
# plt.legend().remove()
# plt.show()

HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)  # Table 50x50

# print(HPI_State_Correlation.describe())
'''
count  50.000000  50.000000  50.000000  50.000000  50.000000  50.000000
mean    0.969390   0.939254   0.932725   0.971255   0.945922   0.954348
std     0.026771   0.043011   0.028004   0.026940   0.024992   0.030143
min     0.872598   0.771111   0.846203   0.861622   0.870084   0.838751
25%     0.955706   0.929268   0.917464   0.965063   0.931971   0.939007
50%     0.977250   0.949213   0.934992   0.978021   0.945327   0.960939
75%     0.986240   0.963171   0.947947   0.989024   0.964504   0.975201
max     1.000000   1.000000   1.000000   1.000000   1.000000   1.000000

'''
