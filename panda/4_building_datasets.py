import quandl
import pandas as pd

# api_key = open('quandlapikey.txt', 'r').read()
api_key = 'xthHuGDE95YvGyvszxjU'
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
df.rename(columns = {'Value':'AK'}, inplace=True)
print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# THIS IS A LIST
# print(fiddy_states[0])
#
# THIS IS A DATAFRAME
# print(fiddy_states[0][1])

# THIS IS A COLUMN
# print(fiddy_states[0][1][1:])

column = fiddy_states[0][1][1:]
for abbv in column:
    print('FMAC/HPI_' + str(abbv))
