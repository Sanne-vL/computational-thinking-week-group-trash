import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = [0.6, 0.8, 1.1, 1.5, 1.9, 2.9]
y = [0.5646, 0.7174, 0.8912, 0.9975, 0.9463, 0.2392]

poly = PolynomialFeatures(degree=2, include_bias=False).fit_transform(np.array(x).reshape(-1, 1))

model = LinearRegression().fit(poly, y)
y_pred = model.predict(poly)

plt.plot(x, y)
plt.plot(x, y_pred)

def solution_station_6(x):
    return model.coef_[1] * x ** 2 + model.coef_[1] * x + model.intercept_

