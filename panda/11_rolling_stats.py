import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

api_key = 'xthHuGDE95YvGyvszxjU'

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = 'FMAC/HPI_' + str(abbv)

        df = quandl.get(query, authtoken=api_key)
        df.rename(columns = {'Value': abbv}, inplace=True)
        # df = df.pct_change()
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    # print(main_df.head())

    pickle_out = open('fiddy_states3.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

# grab_initial_state_data()



HPI_data = pd.read_pickle('fiddy_states3.pickle')


fig = plt.figure()
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0), sharex=ax1)

# CALCULATE 12 MOVING AVERAGE
HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12)

# CALULATE STANDARD DEVIATION
HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12)

print(HPI_data[['TX', 'TX12MA', 'TX12STD']].head())


HPI_data[['TX', 'TX12MA']].plot(ax = ax1)
HPI_data[['TX12STD']].plot(ax = ax2)


plt.legend(loc=4)
plt.show()
