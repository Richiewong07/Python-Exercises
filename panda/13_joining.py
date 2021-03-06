import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

api_key = 'xthHuGDE95YvGyvszxjU'

def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start = "1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100
    df = df.resample('D').sum()
    df = df.resample('M').sum()
    df.columns = ["M30"]
    return df

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


def HPI_BenchMark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.rename(columns = {'Value': "United States"}, inplace=True)
    df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0] * 100
    return df


m30 = mortgage_30y()
HPI_data = pd.read_pickle('fiddy_states.pickle')
HPI_bench = HPI_BenchMark()

state_HPI_M30 = HPI_data.join(m30)

print(state_HPI_M30.corr()['M30'].describe())
