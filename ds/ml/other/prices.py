import matplotlib
import pandas_cl as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel("price1.xlsx")

plt.scatter(df.area, df.price, color="orange", marker="+")
plt.xlabel("square (kv.m)")
plt.ylabel("price (mln.rub)")

reg = linear_model.LinearRegression() # create model
reg.fit(df[["area"]], df.price) # teach model
print(reg.predict([[120]]))
print(reg.predict(df[["area"]]))

plt.plot(df.area, reg.predict(df[["area"]]))

# Y = aX + b
print(reg.coef_)
print(reg.intercept_)
# price = 0.07148238 * square + 0.8111407046647905

pred = pd.read_excel("predicate_price.xlsx")
print(pred.head(1))

p = reg.predict(pred) # prediction prices for new apartments
                    # from new file by our model
pred["predicted prices"] = p
pred.to_excel("new_pred_prices.xlsx", index=False)

plt.show()