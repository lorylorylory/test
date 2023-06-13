import pandas as pd

import re
import jieba
import pandas as pd

import time
import json
import pandas as pd
import numpy as np




df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\爬取\\水星记.csv', header=None, names=['comment'], encoding='utf-8')
df = df.drop_duplicates() #drop_duplicates方法去重默认会删掉完全重复的行（每个值都一样的行）
def quchong(b):
# 1、第一次清洗 特殊字符
    word_list =[]
    for i in b:
        text = re.sub('@.{1,8}|#|【|】|↓|\n|~', " ", i)
        word_list.append(text)
# 2、第二次清洗 只保留中文
    re_word = []
    for i in word_list:
        str=re.sub('[^\u4e00-\u9fa5]+','',i)
        re_word.append(str)
    data_str = ''.join(re_word)
# 3、jieba 分词（精确匹配模式）
    words = jieba.lcut(data_str,cut_all=False)
# 4、读取停用词文档
    stopWords = pd.read_csv('stopwords.txt',encoding='utf-8',sep='hahaha',header=None,engine='python')
    wordlist=list(stopWords.iloc[:,0])
# 5、列表推导式 去除停用词
    lastword = [w for w in words if not w in wordlist]
    return lastword
    print(data_str)

df['comment'] = df['comment'].apply(lambda b:quchong(b))




df.to_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\清洗\\水星记2.csv',index=False)