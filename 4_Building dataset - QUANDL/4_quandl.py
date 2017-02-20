import quandl
import pandas as pd

api_key = open('apikey.txt').read()

df = quandl.get('FMAC/HPI_MEDOR', authtoken=api_key)
# print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# this is a list
# print(fiddy_states)

# this is a dataframe
# print(fiddy_states[0])

# this is a column
# print(fiddy_states[0][0])

for abbv in fiddy_states[0][0][1:]:
    print('FMAC/HPI_' + str(abbv))
