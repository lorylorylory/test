import streamlit as st
from snownlp import SnowNLP
from streamlit_multipage import MultiPage
import pandas as pd
import matplotlib.pyplot as plt
import wordcloud as wc
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
import numpy as np





# 页面1
def java_page1(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('雪')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\雪.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 224, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\雪.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\雪q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    st.subheader('')
    st.subheader('词云')
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\雪w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()
def java_page2(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('我记得')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\我记得.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 233, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\我记得.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\我记得q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    st.subheader('')
    st.subheader('词云')
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\我记得w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()
def java_page3(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('精卫')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\精卫.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 218, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\精卫.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\精卫q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\精卫w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()
def java_page4(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('可能')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\可能.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 230, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\可能.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\可能q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\可能w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()
def java_page5(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('把回忆拼好给你')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\把回忆拼好给你.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 228, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\把回忆拼好给你.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\把回忆拼好给你q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\把回忆拼好给你w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()
def java_page6(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('达尔文')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\达尔文.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 204, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\达尔文.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\达尔文q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\达尔文w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()
def java_page7(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('乌梅子酱')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\乌梅子酱.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 219, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\乌梅子酱.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\乌梅子酱q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\乌梅子酱w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()
def java_page8(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('水星记')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\水星记.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 203, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\水星记.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\水星记q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\水星记w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()
def java_page9(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('就让这大雨全都落下')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\就让这大雨全都落下.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 224, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\就让这大雨全都落下.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\就让这大雨全都落下q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\就让这大雨全都落下w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()
def java_page10(st, **state):
    st.title("网易云热搜榜歌曲评论情感分析")
    st.set_option('deprecation.showPyplotGlobalUse', False) #可视化配置

    st.subheader('若把你')
#折线图
    st.subheader('')
    st.subheader('评论情感系数图（0以上代表积极，0以下代表消极）')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\若把你.csv', "r", encoding='utf-8-sig')
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
        result.append(sentimentslist[i] - 0.5)
        i = i + 1
    # 可视化画图
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(0, 237, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    st.pyplot()
#分数分布
    st.subheader('')
    st.subheader('频率-数量图')
    source = open('C:\\Users\\lory\\Desktop\\pythonProject1\\数据\\若把你.csv', "r", encoding='utf-8-sig')
    line = source.readline()
    sentimentslist = []
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('Analysis of Sentiments')
    st.pyplot()

#柱状图
    st.subheader('')
    st.subheader('正向评论与负向评论柱状图')
    comment = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\分词\\若把你q.csv', header=None, names=['comment'], encoding='utf-8-sig')
    comment['semiscore'] = comment['comment'].apply(lambda x: SnowNLP(x).sentiments)
    comment['semilabel'] = comment['semiscore'].apply(lambda x: 1 if x > 0.5 else -1)
    semilabel = comment['semilabel'].value_counts()
    semilabel = semilabel.loc[[1, -1]]
    plt.bar(semilabel.index, semilabel.values, tick_label=semilabel.index, color='#2FC25B')
    plt.xlabel("semislabel")
    plt.ylabel("number")
    plt.title("The semi-label of comment")
    st.pyplot()
#词云
    st.subheader('')
    st.subheader('词云')
    df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\词云\\若把你w.csv', encoding='utf-8-sig')
    word_cloud = wc.WordCloud(
        width=800,  # 词云图宽
        height=800,  # 词云图高
        background_color='white',  # 词云图背景颜色，默认为白色
        font_path=r'C:\Windows\Fonts\simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
        max_font_size=350,  # 最大字体，默认为200
        random_state=50,  # 为每个单词返回一个PIL颜色
    )
    text = " ".join(df['comment'].tolist())
    word_cloud.generate(text)
    plt.imshow(word_cloud)
    plt.axis('off')
    st.pyplot()



app = MultiPage()
app.st = st
app.navbar_name = '选择分析的数据'
app.navbar_style = 'SelectBox'
# 添加页面到侧边栏
app.add_app("雪", java_page1)
app.add_app("我记得", java_page2)
app.add_app("精卫", java_page3)
app.add_app("可能", java_page4)
app.add_app("把回忆拼好给你", java_page5)
app.add_app("达尔文", java_page6)
app.add_app("乌梅子酱", java_page7)
app.add_app("水星记", java_page8)
app.add_app("就让这大雨全部落下", java_page9)
app.add_app("若把你", java_page10)
app.run()
