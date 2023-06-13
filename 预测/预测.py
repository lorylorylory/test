import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr
print("预测:")

#读取数据
df = pd.read_csv('C:\\Users\\lory\\Desktop\\pythonProject1\\预测\\分段2.csv',encoding='gbk')


#建立一个二维数组
lr = pd.DataFrame()
lr['时间段']=df['时间段']
lr['数量'] =df['数量']


#特征数据选择
exam_X=lr.loc[:,'时间段']
#标签labes
exam_y=lr.loc[:,'数量']

print(lr)
#划分训练集测试集
X_train , X_test , y_train , y_test = train_test_split(exam_X,exam_y,train_size=0.8)

X_train=X_train.values.reshape(-1,1)

X_test=X_test.values.reshape(-1,1)
model=LinearRegression()
#训练模型
model.fit(X_train , y_train)

a=model.intercept_
b=model.coef_
x1 = df['时间段']
y1 = df['数量']
s = pearsonr(x1,y1)
print( '皮尔森相关系数:',s[0])
print("R方：",model.score(X_test , y_test))

plt.title('prediction')
plt.scatter(X_train, y_train, color='red', label="train data")

y_train_pred = model.predict(X_train)

plt.plot(X_train, y_train_pred, color='yellow', linewidth=5)

plt.show()