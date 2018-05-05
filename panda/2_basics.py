import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats = {'Day' : [1,2,3,4,5,6],
            'Visitors' : [43,53,34,45,64,34],
            'Bounce_Rate' : [65,72,62,64,54,66]}

# CHANGE DICTIONARY TO DATAFRAME
df = pd.DataFrame(web_stats)
# print(df)
# print(df.head())
# print(df.tail())

# SET/MODIFY INDEX FOR DATAFRAME
df.set_index('Day', inplace=True)
# print(df.head())

# TO REFERENCE A SPECIFIC COLUMN
# print(df['Visitors'])
print(df.Visitors)

# TO REFERENCE MULTIPLE COLUMNS
# print(df[['Visitors', 'Bounce_Rate']])

# CHANGE COLUMN TO LIST
# print(df.Visitors.tolist())


# print(np.array(df[['Visitors', 'Bounce_Rate']]))

df2 = pd.DataFrame(np.array(df[['Visitors', 'Bounce_Rate']]))
print(df2)
