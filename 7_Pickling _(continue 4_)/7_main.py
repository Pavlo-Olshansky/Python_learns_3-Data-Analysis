import quandl
import pandas as pd
import pickle

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

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    # with open('fiddy_state.pickle', 'wb') as f:
    #     pickle.dump(main_df, f)
    #     f.close()
    main_df.to_pickle('pickle_pandas.pickle')

grab_initial_state_data()
# pickle_in = open('fiddy_state.pickle', 'rb')
# HPI_data = pickle.load(pickle_in)
HPI_data = pd.read_pickle('pickle_pandas.pickle')
print(HPI_data)
