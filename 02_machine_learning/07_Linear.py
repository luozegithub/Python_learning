from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np


def linear():
    data = load_boston()
    # print(data.data)
    # print(data.feature_names)
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25)
    # print(x_train)

    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))

    lr = LinearRegression()
    lr.fit(x_train, y_train)
    y_predict = std_y.inverse_transform(lr.predict(x_test))
    print('linear', lr.score(x_test, y_test))
    print('coef:', lr.coef_)
    print('mean_squared_error:', mean_squared_error(std_y.inverse_transform(y_test), y_predict))


def sgd():
    data = load_boston()
    # print(data.data)
    # print(data.feature_names)
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25)
    # print(x_train)

    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))

    lr = SGDRegressor()
    lr.fit(x_train, y_train)
    y_predict = std_y.inverse_transform(lr.predict(x_test))
    print('sgd', lr.score(x_test, y_test))
    print('coef:', lr.coef_)
    print('mean_squared_error:', mean_squared_error(std_y.inverse_transform(y_test), y_predict))


def ridge():
    data = load_boston()
    # print(data.data)
    # print(data.feature_names)
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25)
    # print(x_train)

    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))

    lr = Ridge()
    lr.fit(x_train, y_train)
    y_predict = std_y.inverse_transform(lr.predict(x_test))
    # print(y_predict)
    print('ridge', lr.score(x_test, y_test))
    print('coef:', lr.coef_)
    print('mean_squared_error:', mean_squared_error(std_y.inverse_transform(y_test), y_predict))


if __name__ == '__main__':
    linear()
    sgd()
    ridge()
