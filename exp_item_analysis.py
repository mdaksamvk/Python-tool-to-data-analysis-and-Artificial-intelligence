#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:12:51 2018

@author: admin
"""
import os
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = (10.0, 8.0)
import seaborn as sns
from scipy import stats
from scipy.stats import norm


cursor.execute('SELECT * FROM ItemDetails WHERE RECEIPT_YEAR=2015 AND RECEIPT_MONTH=1')
month1_2015= cursor.fetchall()
df4 = pd.DataFrame(month1_2015)
df4.columns = df2.names
df4.columns[df4.isnull().any()]

#missing value counts in each of these columns
miss = df4.isnull().sum()/len(df4)
miss = miss[miss > 0]
miss.sort_values(inplace=True)
miss
print(round(miss,4))

#visualising missing values
miss = miss.to_frame()
miss.columns = ['count']
miss.index.names = ['Name']
miss['Name'] = miss.index
miss
#plot the missing value count
sns.set(style="whitegrid", color_codes=True)
sns.barplot(x = 'Name', y = 'count', data=miss)
plt.xticks(rotation = 90)
sns.plt.show()
fig1 = sns_plot.get_figure()
fig1.savefig("output1.png")


df4.ITEM_CAT.unique().tolist()


#ONE DAY TRANSACTION DATA OF 1_01_2015
cursor.execute('SELECT * FROM TransactionDetails WHERE RECEIPT_YEAR=2015 AND RECEIPT_MONTH=1 AND RECEIPT_DAY=1')
_1month1_2015= cursor.fetchall()
df5 = pd.DataFrame(_1month1_2015)
df5.columns = df.names
df5.to_csv('TRANS1_01_2015_sample.csv')
#tenant id as shop
df5.apply(lambda x: x.nunique()).to_csv('uniqueno.csv')

df6=df5.groupby(['RECEIPT_HOUR','RECEIPT_MINUTE'])['NET_SALES'].sum()

import datetime as da
d7=df5.apply(lambda x:da.datetime(int(x['RECEIPT_YEAR']),int(x['RECEIPT_MONTH']),int(x['RECEIPT_DAY']),int(x['RECEIPT_HOUR']),int(x['RECEIPT_MINUTE']),int(x['RECEIPT_SECONDS'])),axis=1)
df7 = pd.DataFrame(d7)
df7.columns=['dttime']
df8=pd.concat([df5,df7])
df8 = pd.concat([df5, df7], axis=1, sort=False)
df8['dttime'].groupby(pd.TimeGrouper("15Min")).mean()

df8.groupby(pd.TimeGrouper('5Min')).apply(lambda x: x.groupby(['dttime']))

df8["NET_SALES"] = df8["NET_SALES"].astype("float")
df8.groupby('dttime')['NET_SALES'].sum()

df8["tran_count"] = df8["tran_count"].astype("int")

df8 = df8.set_index(pd.DatetimeIndex(df8['dttime']))
df9=df8.groupby(pd.TimeGrouper("15Min")).sum()


df9 = pd.DataFrame()
df8['tran_count']=1
df8.groupby('dttime')['NET_SALES','tran_count'].sum().plot()

#clusters
from scipy import stats
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=4,random_state=0).fit(stats.zscore(df9))
labels=kmeans.labels_
df9['clusters']=labels
df10=df9.groupby(['clusters']).mean()

#plot
import seaborn as sns
