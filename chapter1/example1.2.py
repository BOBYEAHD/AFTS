#-*- coding:utf-8 -*-
from __future__ import division


import pandas as pd
import math
import moment

df = pd.read_table("./chapter1/text/d-ibm3dx7008.txt")

df.columns = df.columns.map(lambda x :x.strip()) # 去掉字段名存在的空格

df['Date'] = df['Date'].apply( lambda x : moment.date( str(x) ,'YYYYMMDD').date)

df = df.set_index(df['Date'])

print df

df.shape  

df.head(1) # 数据集的第一行

df.tail(1) # 数据集的最后一行 

ibm = df['rtn']

sibm = ibm * 100

sibm.mean()

sibm.median()

sibm.sum()

sibm.var()

sibm.std()

sibm.skew() # 偏度

sibm.kurtosis() # 超额峰度

s1 = sibm.skew()

t1 = s1/math.sqrt(6/9845) # 检验统计量

print t1