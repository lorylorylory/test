# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\预测\\分段.csv',encoding='gbk')
def jy(x):
    x = str(x)
    x = x.split(':')[0]
    return x
df['时间'] = df['时间'].apply(lambda x: jy(x))
df.to_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\预测\\分段20.csv',index=False)


# df1= df['时间段']
# df1=pd.Series(df1)
# df2= df['数量']
# df2=pd.Series(df1)
# df.to_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\预测\\分段22.csv',index=False)
