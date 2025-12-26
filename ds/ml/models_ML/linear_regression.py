import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

X, y = make_regression(n_samples=50, n_features=1, n_informative=1,
                       noise=10, random_state=11)

print(X, y)

fig = plt.figure(figsize=(10, 6))
plt.scatter(X, y)

model = LinearRegression()
model.fit(X, y)

print(model.coef_, model.intercept_)

model_a = model.coef_[0]
model_b = model.intercept_

x = np.arange(-3, 3)
model_y_sk = model_a * x + model_b

plt.plot(x, model_y_sk, linewidth=2, c='r', label=f"linear_model = {model_a:.2f}x + {model_b:.2f}")
plt.plot([0, 1], [model_b, model_b], 'y', linewidth=3)
plt.plot([1, 1], [model_b, model_b + model_a], 'y', linewidth=3)
plt.grid()
plt.legend(prop={"size": 16})

plt.xlabel("feature")
plt.xlabel("target")
plt.show()