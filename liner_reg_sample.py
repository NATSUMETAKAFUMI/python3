#!/usr/bin/env python3

import numpy as np
from sklearn import linear_model

# 収集したデータと仮定
x_data = np.arange(-3, 10, 0.1).reshape(-1, 1)
y_data = (1 / 2) * x_data + np.random.normal(0.0, 0.5, len(x_data)).reshape(-1, 1)

# 学習用データと仮定
x_train = x_data[70:]
y_train = y_data[70:]

# モデルを学習データにフィットさせる
reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)

# テストデータ
x_test = x_data[:71]
y_test = y_data[:71]

# 予測
pred = reg.predict(x_test)

# 決定係数
print('score : ', reg.score(x_test, y_test))


