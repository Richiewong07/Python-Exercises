import pandas as pd

df = pd.read_csv('ZILLOW-Z77478_ZRIFAH.csv')
print(df.head())

# SAVE NEW CSV FILE
df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv')

# HOW TO SET INDEX FROM CSV FILE
# df = pd.read_csv('newcsv2.csv')
df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

# RENAMING COLUMNS
df.columns = ['Sugar_Land_HPI']
print(df.head())
df.to_csv('newcsv3.csv')

# REMOVE HEADERS
df.to_csv('newcsv4.csv', header=False)

# SET NEW HEADERS & INDEX
df = pd.read_csv('newcsv4.csv', names=['Date', 'Sugar_Land_HPI'], index_col=0)
print(df.head())

# CONVERT DATAFRAME TO HTML TABLE
df.to_html('example.html')

# RENAME SINGLE COLUMN
df = pd.read_csv('newcsv4.csv', names=['Date', 'Sugar_Land_HPI'])
df.rename(columns = {'Sugar_Land_HPI':'77478_HPI'}, inplace=True)
print(df.head())
