import statistics

import matplotlib.pyplot as plt
import numpy as np
import pandas_cl as pd


data = [185, 175, 170, 169, 171, 175, 157, 170, 172, 172, 172, 172, 167, 173, 168, 167, 166, 167, 169, 177, 178, 165,
        161, 179, 159, 164, 178, 170, 173, 171]

# Считаем моду/моды
series = pd.Series(data)
modes = list(series.mode())

# Создаем оси
count = series.value_counts()
x_points = np.array(count.keys())
y_points = np.array(count)

# Создаем plot
fig, ax = plt.subplots()

# Наводим красоту
ax.bar(x_points, y_points, width=0.5)
ax.set_ylim(0, 6)
ax.set_xlabel('Height')
ax.set_ylabel('Count')

# На каждой итерации цикла добавляется аннотация к моде. Указываю координаты текста, цвет и поворот.
for mode in modes:
    y = count[mode]
    ax.annotate('mode', xy=(mode, y), xycoords='data', xytext=(mode - 0.5, y + 0.2), rotation=90,
                color='red')
plt.show()

# Define an array of values
values = np.array(
    [185, 175, 170, 169, 171, 172, 175, 157, 170, 172, 167, 173, 168, 167, 166, 167, 169, 172, 177, 178, 165, 161, 179,
     159, 164, 178, 172, 170, 173, 171])

# Calculate the median
median = statistics.median(values)
# Plot the histogram
plt.hist(values, bins=4)
# Add a vertical line at the median value
plt.axvline(median, color='r', linestyle='dashed', linewidth=2)
# Show the plot
plt.show()