# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import os
import matplotlib.pyplot as plt
import numpy as np

source = open('评分.csv',"r", encoding='gbk')
line = source.readlines()
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)
# 情感波动分析
result = []
i = 0
while i < len(sentimentslist):
    result.append(sentimentslist[i] -0.5)
    i = i + 1
