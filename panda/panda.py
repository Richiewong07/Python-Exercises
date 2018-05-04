import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats = {'Day' : [1,2,3,4,5,6],
            'Visitors' : [43,53,34,45,64,34],
            'Bounce_Rate' : [65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)
# print(df)
# print(df.head())
# print(df.tail())

df.set_index('Day', inplace=True)
# print(df.head())

# print(df['Visitors'])
# print(df.Visitors)


# print(df[['Visitors', 'Bounce_Rate']])


# print(df.Visitors.tolist())

# print(np.array(df[['Visitors', 'Bounce_Rate']]))

df2 = pd.DataFrame(np.array(df[['Visitors', 'Bounce_Rate']]))
print(df2)
