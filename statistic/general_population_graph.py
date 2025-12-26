import statistics

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas_cl as pd


data = [185, 175, 170, 169, 171, 175, 157, 170, 172, 172, 172, 172, 167, 173, 168, 167, 166, 167, 169, 177, 178, 165,
        161, 179, 159, 164, 178, 170, 173, 171]

# plt.figure(1, figsize=(5,6))
# plt.subplot(111)
# plt.grid()
# plt.xlim(0,2)
# plt.axis([0,1,155,190])
# plt.boxplot(data, showfliers=True)

ax = sns.boxplot(y=data)
ax = sns.swarmplot(y=data, color="#00ffa6")

plt.show()