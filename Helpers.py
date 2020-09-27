import pandas as pd
import numpy as np


def nyc_locator(df):
    df = df[(df['state'].eq('NY'))]
    df = df[(df['county'].eq('Bronx County'))
            | (df['county'].eq('Kings County'))
            | (df['county'].eq('Queens County'))
            | (df['county'].eq('New York County'))]
    return df


def boro_split(df):
    bx = df[(df['county'].eq('Bronx County'))]
    bk = df[(df['county'].eq('Kings County'))]
    qn = df[(df['county'].eq('Queens County'))]
    mh = df[(df['county'].eq('New York County'))]

    return bk, bx, mh, qn


def pipe_full00(df, ppl_list, house_list):
    for x in df.columns.values:
        if x in ppl_list:
            df[x + '%'] = 100 * df[x] / df['POP00']
        elif x in house_list:
            df[x + '%'] = 100 * df[x] / df['HU00']

    df['NONWHT00%'] = 100 * (df.iloc[:, [10,11,13]].sum(1) / df['POP00'])
    df.drop(columns=['HU00%'], axis=1, inplace=True)
    df.drop(df.columns[9:51], axis=1, inplace=True)
    df.drop(df.columns[4:8], axis=1, inplace=True)

    return df


def pipe_full10(df, ppl, house):
    for x in df.columns.values:
        if x in ppl:
            df[x + '%'] = 100 * (df[x] / df['POP10'])
        elif x in house:
            df[x + '%'] = 100 * (df[x] / df['HU10'])

    df['NONWHT10%'] = 100 * (df.iloc[:, [6,7,9]].sum(1) / df['POP10'])
    df.drop(df.columns[5:47], axis=1, inplace=True)
    return df


def separator(df, yr_start, yr_end):
    lst_start = [x for x in df.columns.values if str(yr_start) in x]
    lst_end = [x for x in df.columns.values if str(yr_end) in x]
    lst = list(zip(lst_start, lst_end))
    return lst


def pc_change(df, lst):
    for i, x in lst:
        try:
            df[x + '_' + i] = 100 * ((df[x] - df[i]) / (df[i]))
        except ZeroDivisionError:
            0
    return df


def pipe_sample00(df, ppl, hou, hh):
    for x in df.columns.values:
        if x in ppl:
            df[x + '%'] = 100 * df[x] / df['POP00SF3']
        elif x in hou:
            df[x + '%'] = 100 * df[x] / df['HU00SP']
        elif x in hh:
            df[x + '%'] = 100 * df[x] / df['HH00']

    df['NONWHT_POV00%'] = 100*(df.iloc[:,[49,51,53,55]].sum(1)/df['POP00SF3'])
    
    return df
