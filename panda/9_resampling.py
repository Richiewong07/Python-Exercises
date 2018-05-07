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

    # USE PICKLE TO SAVE DATA
    pickle_out = open('fiddy_states3.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

# grab_initial_state_data()



HPI_data = pd.read_pickle('fiddy_states3.pickle')

# PERCENT CHANGE GRAPH
fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

TX1yr = HPI_data['TX'].resample('A').mean()
# TX2yr = HPI_data['TX'].resample('A').ohlc()
print(TX1yr.head())

HPI_data['TX'].plot(ax=ax1, label='Monthly TX HPI')
TX1yr.plot(ax=ax1, label='Yearly TX HPI')
# TX2yr.plot(ax=ax1, label='High Low')


plt.legend(loc=4)
plt.show()
