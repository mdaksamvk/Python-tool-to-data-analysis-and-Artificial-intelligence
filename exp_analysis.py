# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:28:45 2018

@author: aksam.vk
"""

#Loading libraries 
import os
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = (10.0, 8.0)
import seaborn as sns
from scipy import stats
from scipy.stats import norm

#loading data
os.chdir('D:/BIAL Data/2015/PP')
dt= pd.read_csv("python_6_month.csv")
dt.head()
dt=dt.loc[:, ~dt.columns.str.contains('^Unnamed')]
dt.columns

#check missing values
dt.info()
dt.columns[dt.isnull().any()]

#missing value counts in each of these columns
miss = dt.isnull().sum()/len(dt)
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

#Delete coloumns


#Data exploraqtion
# Net sales distribution 
sns.distplot(dt.NET_SALES)
dt['NET_SALES'].value_counts()


#net sales per month
dt['NET_SALES'][dt['RECEIPT_MONTH'] == '1'].sum()
dt['RECEIPT_MONTH'].value_counts()

#day_wise_NET_SALES for 6 month value and count
g11=dt[dt.RECEIPT_MONTH == 1].groupby('RECEIPT_DAY')['NET_SALES'].sum()
g11.plot(kind='bar')
g12=dt[dt.RECEIPT_MONTH == 2].groupby('RECEIPT_DAY')['NET_SALES'].sum()
g12.plot(kind='bar')
g13=dt[dt.RECEIPT_MONTH == 3].groupby('RECEIPT_DAY')['NET_SALES'].sum()
g13.plot(kind='bar')
g14=dt[dt.RECEIPT_MONTH == 4].groupby('RECEIPT_DAY')['NET_SALES'].sum()
g14.plot(kind='bar')
g15=dt[dt.RECEIPT_MONTH == 5].groupby('RECEIPT_DAY')['NET_SALES'].sum()
g15.plot(kind='bar')
g16=dt[dt.RECEIPT_MONTH == 6].groupby('RECEIPT_DAY')['NET_SALES'].sum()
g16.plot(kind='bar')

g21=dt[dt.RECEIPT_MONTH == 1].groupby('RECEIPT_DAY')['NET_SALES'].count()
g21.plot(kind='bar')
g22=dt[dt.RECEIPT_MONTH == 2].groupby('RECEIPT_DAY')['NET_SALES'].count()
g22.plot(kind='bar')
g23=dt[dt.RECEIPT_MONTH == 3].groupby('RECEIPT_DAY')['NET_SALES'].count()
g23.plot(kind='bar')
g24=dt[dt.RECEIPT_MONTH == 4].groupby('RECEIPT_DAY')['NET_SALES'].count()
g24.plot(kind='bar')
g25=dt[dt.RECEIPT_MONTH == 5].groupby('RECEIPT_DAY')['NET_SALES'].count()
g25.plot(kind='bar')
g26=dt[dt.RECEIPT_MONTH == 6].groupby('RECEIPT_DAY')['NET_SALES'].count()
g26.plot(kind='bar')

#day_wise_NET_SALES accumulated for 6 month count and value
g31=dt.groupby('RECEIPT_DAY')['NET_SALES'].sum()
g31.plot(kind='bar')
g32=dt.groupby('RECEIPT_DAY')['NET_SALES'].count()
g32.plot(kind='bar')


#week_wise_NET_SALES for 6 month value and count
g41=dt[dt.RECEIPT_MONTH == 1].groupby('WEEKNUMBER')['NET_SALES'].sum()
g41.plot(kind='bar')
g42=dt[dt.RECEIPT_MONTH == 2].groupby('WEEKNUMBER')['NET_SALES'].sum()
g42.plot(kind='bar')
g43=dt[dt.RECEIPT_MONTH == 3].groupby('WEEKNUMBER')['NET_SALES'].sum()
g43.plot(kind='bar')
g44=dt[dt.RECEIPT_MONTH == 4].groupby('WEEKNUMBER')['NET_SALES'].sum()
g44.plot(kind='bar')
g45=dt[dt.RECEIPT_MONTH == 5].groupby('WEEKNUMBER')['NET_SALES'].sum()
g45.plot(kind='bar')
g46=dt[dt.RECEIPT_MONTH == 6].groupby('WEEKNUMBER')['NET_SALES'].sum()
g46.plot(kind='bar')

g51=dt[dt.RECEIPT_MONTH == 1].groupby('WEEKNUMBER')['NET_SALES'].count()
g51.plot(kind='bar')
g52=dt[dt.RECEIPT_MONTH == 2].groupby('WEEKNUMBER')['NET_SALES'].count()
g52.plot(kind='bar')
g53=dt[dt.RECEIPT_MONTH == 3].groupby('WEEKNUMBER')['NET_SALES'].count()
g53.plot(kind='bar')
g54=dt[dt.RECEIPT_MONTH == 4].groupby('WEEKNUMBER')['NET_SALES'].count()
g54.plot(kind='bar')
g55=dt[dt.RECEIPT_MONTH == 5].groupby('WEEKNUMBER')['NET_SALES'].count()
g55.plot(kind='bar')
g56=dt[dt.RECEIPT_MONTH == 6].groupby('WEEKNUMBER')['NET_SALES'].count()
g56.plot(kind='bar')

#week_wise_NET_SALES accumulated for 6 month count and value
g6=dt.groupby('WEEKNUMBER')['NET_SALES'].sum()
g6.plot(kind='bar')
g6=dt.groupby('WEEKNUMBER')['NET_SALES'].count()
g6.plot(kind='bar')

#month_wise_NET_SALES for 6 month count and value
g71=dt.groupby('RECEIPT_MONTH')['NET_SALES'].sum()
g71.plot(kind='bar')
g72=dt.groupby('RECEIPT_MONTH')['NET_SALES'].count()
g72.plot(kind='bar')


#day_wise_NET_SALES line plot for 6 month
g81=dt.groupby('RECEIPT_DATE')['NET_SALES'].sum()
g81.plot(kind='line')
g82=dt.groupby('RECEIPT_DATE')['NET_SALES'].count()
g82.plot(kind='line')

#location_wise_NET_SALES accumulated for 6 month count and value
g91=dt.groupby('LOCATION_CODE')['NET_SALES'].sum()
g91.plot(kind='bar')
g92=dt.groupby('LOCATION_CODE')['NET_SALES'].count()
g92.plot(kind='bar')

#Correlation between NET_SALES and discount
dt['NET_SALES'].corr(dt['DISCOUNT'])

#Missing value deduction row elements
nan_rows1 = dt[dt['CUST_PAX_TYPE'].isnull()]
nan_rows2 = dt[dt['LOCATION_CODE'].isnull()]
nan_rows3 = dt[dt['CUST_GENDER'].isnull()]
nan_rows4 = dt[dt['BrandId'].isnull()]

nan_rows5 = dt[dt['Customer'].isnull()]
nan_rows6 = dt[dt['CUST_PP_NO'].isnull()]
nan_rows7 = dt[dt['CUST_GENDER'].isnull()]
nan_rows8 = dt[dt['CUST_FL_NO'].isnull()]

#Discount and NET_SALES
plt.figure(figsize=(10, 8))
plt.plot(dt['RECEIPT_MONTH'], dt['NET_SALES'], 'b-', label = 'GM')
plt.plot(dt['RECEIPT_MONTH'], dt['DISCOUNT'], 'r-', label = 'TESLA')
plt.xlabel('Date'); plt.ylabel('Market Cap (Billions $)'); plt.title('Market Cap of GM and Tesla')
plt.legend();

#time series

import dateutil.parser
#d = dateutil.parser.parse('20150409').date()
#d
dt['RECEIPT_DATE']=dt['RECEIPT_DATE'].apply(str)
dt['RECEIPT_DATE'] = [dateutil.parser.parse(x) for x in dt['RECEIPT_DATE']]

#Time parser
d = dateutil.parser.parse('2015-01-02 091100').time()
t = time.strptime("091100", "%H%M%S")
dt['RECEIPT_TIME']=dt['RECEIPT_TIME'].apply(str)
dt['RECEIPT_DATE'] = [dateutil.parser.parse(x) for x in dt['RECEIPT_DATE']]

date_time=dt[['RECEIPT_DATE','RECEIPT_TIME']].apply(lambda x : '{}{}'.format(x[0],x[1]), axis=1)
[dateutil.parser.parse(x) for x in date_time]
date_time=date_time.apply(str)

pd.to_datetime( "20150102"+ ' ' + "091100")
dt[['RECEIPT_DATE','RECEIPT_TIME']].apply(lambda x: ' '.join(x), axis=1)
dt[['RECEIPT_DATE','RECEIPT_TIME']].apply(lambda x: ' '.join(x), axis=1)
l=dt[['RECEIPT_DATE','RECEIPT_TIME']].apply(lambda x: ' '.join(x), axis=1)
l = l.to_frame().reset_index()
del l['index']
l = l.rename(columns= {0: 'date'})
l['date'] = pd.to_datetime(l['date'],errors ='coerce')
l=dt[['RECEIPT_DATE','RECEIPT_TIME']].apply(lambda x: ' '.join(x).pd.to_datetime(), axis=1)

dt['RECEIPT_TIME']=dt['RECEIPT_TIME'].apply(str)
dt['RECEIPT_TIME'].apply(lambda x: datetime.datetime.strftime(x,'%H%M%S'))
df['date'] = df['date'].apply(lambda x: datetime.datetime.strftime(x,'%Y%m%d'))
dt['RECEIPT_TIME'].apply(lambda x: "00:00:00".format(x))
#Merge date and time coloumn

dt['RECEIPT_DATE'].head()

plt.figure(figsize=(10, 8))
plt.plot(dt['RECEIPT_DATE'], dt['NET_SALES'], 'b-', label = 'GM')
plt.plot(dt['RECEIPT_DATE'], dt['DISCOUNT'], 'r-', label = 'GM')
 
## function to show the plot
#plt.show()


#Comparison between net_sales and discount with respect to receipt_date
plt.plot(dt['RECEIPT_DATE'], dt['NET_SALES'],dt['RECEIPT_DATE'], dt['DISCOUNT'])

#Comparison between net_sales and discount
compare = pd.DataFrame({'o_Discount': dt['DISCOUNT'],'t_netsales': dt['NET_SALES']})
compare.plot()


po=dt.groupby('RECEIPT_DATE')['NET_SALES']
po.plot(kind='line')
# What is the sum of durations, for calls only, to each network
data[data['item'] == 'call'].groupby('network')['duration'].sum()


#net sales value zero
NET_SALES_zero=dt[dt['NET_SALES']==0]
NET_SALES_zero['NET_SALES'].head
#sales distribution
#SalePrice
#sns.distplot(dt['NET_SALES'],plt.xlim(-10000,10000))
#dt.plot(dt['NET_SALES'])
#
#sns.distplot(dt['DISCOUNT'])
#
#us_mq_airlines_index = dt['unique_carrier'].isin(['NET_SALES','DISCOUNT'])
##plot the missing value count
#sns.set(style="whitegrid", color_codes=True)
#g=sns.barplot(x = 'Name', y = 'count', data=miss, aspect=1.5)
#
#g.set_xticklabels(rotation=30)
#fig1 = sns_plot.get_figure()
#fig1.savefig("output1.png")
#
#
import datetime as da
l1=dt.apply(lambda x: da.datetime(x['RECEIPT_YEAR'], x['RECEIPT_MONTH'], x['RECEIPT_DAY'], x['RECEIPT_HOUR'], x['RECEIPT_MINUTE'], x['RECEIPT_SECONDS']), axis=1)
l1.head
l1 = l1.to_frame().reset_index()
del l1['index']
l1 = l1.rename(columns= {0: 'DATE_TIME'})
#https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
dt1=pd.concat([dt, l1], axis=1, ignore_index=False)
dt1=dt.merge(l1)



#
#
#
#
##plot the missing value count
#sns.set(style="whitegrid", color_codes=True)
#sns_plot=sns.barplot(x = 'Name', y = 'count', data=miss)
#plt.xticks(rotation='vertical')
#plt.plot(np.random.randn(100).cumsum())
#
#fig1 = sns_plot.get_figure()
#fig.savefig("output1.png")
#xticks(Name)
#plt.x(rotation =90)
#sns.plt.show()
