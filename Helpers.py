import pandas as pd
import numpy as np
def nyc_locator(df):
    df = df[(df['state'].eq('NY'))]
    df = df[(df['county'].eq('Bronx County'))
                      | (df['county'].eq('Kings County'))
                      | (df['county'].eq('Queens County'))
                      | (df['county'].eq('New York County'))]
    return df


def pipe_full(df,ppl_list,house_list, yr):
    for x in df.columns.values:
        if x in ppl_list:
            df[x + '%'] = 100 * df[x] / df['POP' + str(yr)]
        elif x in house_list:
            df[x + '%'] = 100 * df[x] / df['HU' + str(yr)]
    # the percentage of non
    df['NONWHT'+str(yr)+'%'] = 100*(df.iloc[:,10:14].sum(1)/df['POP'+str(yr)+'%])
    df.drop(columns = ['HU'+str(yr)+'%'], axis = 1, inplace = True)
    df.drop(df.columns[9:51],axis=1,inplace=True)
    df.drop(df.columns[4:8],axis=1,inplace=True)

    return df


def separator(df,yr_start,yr_end):
    lst_start = [x for x in df.columns.values if str(yr_start) in x]
    lst_end = [x for x in df.columns.values if str(yr_end) in x]
    lst = list(zip(lst_start, lst_end))
    return lst

def pc_change(df,yr_start,yr_end ):
    def separator(df,yr_start, yr_end):
        lst_start = [x for x in df.columns.values if str(yr_start) in x]
        lst_end = [x for x in df.columns.values if str(yr_end) in x]
        lst = list(zip(lst_start, lst_end))
        return lst

    for i, x in lst:
        try:
            df[i + '_' + x] = 100 * ((df[i] - df[x]) / (df[x]))
        except ZeroDivisionError:
            0
    return df


def pipe_sample(df,ppl,hou,hh,yr):
    for x in df.columns.values:
        if x in ppl:
            df[x + '%'] = 100 * df[x] / df['POP'+str(yr)+'SF3']
        elif x in hou:
            df[x + '%'] = 100 * df[x] / df['HU'+str(yr)]
        elif x in hh:
            df[x + '%'] = 100 * df[x] / df['HH'+str(yr)]
    # the percentage of non
    df['NONWHT_POV'+str(yr)+'%'] = 100*(df.iloc[:,[49,51,53,55]].sum(1)/df['POP'+str(yr)+'SF3'])

    return df



def pop_pipe(df,ppl,hou,hh):
    for x in df.columns.values:
        if x in ppl:
            df[x + '%'] = 100 * df[x] / df['POP12SF3']
        elif x in hou:
            df[x + '%'] = 100 * df[x] / df['HU12']
        elif x in hh:
            df[x + '%'] = 100 * df[x] / df['HH12']
    # the percentage of non-white people in poverty
    df['NONWHT_POV12%'] = 100*(df.iloc[:,[32,34,38]].sum(1)/df['POP12SF3'])



