import matplotlib
import pandas_cl as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Y = aX + bZ + c // Y - VVP, X - oil price, Z - year

df = pd.read_excel("gdprus.xlsx")

plt.scatter(df.oilprice, df.gdp)
plt.xlabel("oldprice (US$)")
plt.xlabel("gdp (bin US$)")

reg = linear_model.LinearRegression()
reg.fit(df[["year", "oilprice"]], df.gdp)

plt.plot(df.oilprice, reg.predict(df[["year", "oilprice"]]))

print(df.head())
#print(reg.predict(df[["oilprice"]]))
print(reg.predict(df[["year", "oilprice"]]))
print(reg.predict([[2025, 100]]))

plt.show()