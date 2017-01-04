#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
This is the test of regression analysis
"""


__author__ = 'Hi-Xux7'
__version__= '1.0'

import pandas as pd
import matplotlib.pyplot as plot
# from sklearn.cross_validapition import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
if __name__=='__main__':

    # 读取文件
    data = pd.read_csv('E:/TestingData/ML/Advertising.csv')
    # print data.head()
    x = data[['TV','Radio','Newspaper']]
    y = data['Sales']

    # 绘制1
    # plot.plot(data['TV'],y,'ro',label='TV')
    # plot.plot(data['Radio'],y,'g^',label='Radio')
    # plot.plot(data['Newspaper'],y,'b*',label='Newspaper')
    # plot.legend(loc='lower right')
    # plot.grid()
    # plot.show()
    # 绘制2
    # plot.figure(figsize=(9,12))
    # plot.subplot(311)
    # plot.plot(data['TV'], y, 'ro')
    # plot.title('TV')
    # plot.grid()
    # plot.subplot(312)
    # plot.plot(data['Radio'], y, 'g^')
    # plot.title('Radio')
    # plot.grid()
    # plot.subplot(313)
    # plot.plot(data['Newspaper'], y, 'b*')
    # plot.title('Newspaper')
    # plot.grid()
    # plot.tight_layout()
    # plot.show()
    # 使用pandas来构建X（特征向量）和y（标签列）
    #建立特征名的python列表
    # feature_cols=['TV','Radio','Newspaper']
    feature_cols=['TV','Radio']
    #use the list to select a subset of the original DataFrame
    X = data[feature_cols]
    # equivalent command to do this in one line
    # X = data[['TV', 'Radio', 'Newspaper']]
    # print the first 5 rows
    # print X.head()
    # check the type and shape of X
    # print type(X)
    # print X.shape
    # select a Series from the DataFrame
    y = data['Sales']
    # equivalent command that works if there are no spaces in the column name
    # y = data.Sales
    # print the first 5 values
    # print y.head()

    # 构建训练集与测试集
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1)
    # print X_train.shape
    # print y_train.shape
    # print X_test.shape
    # print y_test.shape
    linreg = LinearRegression()
    model = linreg.fit(X_train,y_train)
    # print model
    print linreg.intercept_
    print linreg.coef_

    zip(feature_cols,linreg.coef_)

    y_pred = linreg.predict(X_test)
    # print y_pred
    # print type(y_pred)
    # 绘图
    plot.figure()
    plot.plot(range(len(y_pred)),y_pred,'b',label="predict")
    plot.plot(range(len(y_pred)),y_test,'r',label="test")
    plot.legend(loc="upper right") #显示图中的标签
    plot.xlabel("the number of sales")
    plot.ylabel('value of sales')
    plot.show()
