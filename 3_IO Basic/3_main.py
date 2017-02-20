import pandas as pd
# df = pd.read_csv('my_file.csv')
# print(df.head())
# df.set_index('Date', inplace=True)
# df.to_csv('new_file_2.csv', index_col=0)
# print(df.head())
#
# df.columns = ['MESSAGE']
# print(df.head())
#
# df.to_csv('new_file_3.csv')
# df.to_csv('new_file_4.csv', header=False)
#
# df = pd.read_csv('new_file_4.csv', names=['DATA', 'MESSAGE'])  # index_col=0
# print(df.head())
#
# df.to_html('example.html', index=False)

df = pd.read_csv('new_file_4.csv', names=['Date', 'Message'])
print(df.head())
df.rename(columns={'Message': 'My_message'}, inplace=True)
print(df.head())
