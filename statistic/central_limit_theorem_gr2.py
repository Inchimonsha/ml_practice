import matplotlib.pyplot as plt
import numpy as np

# Generate random data from a uniform distribution
data1 = np.random.uniform(low=-10, high=10, size=10000)

# Generate random data from a skewed distribution
data2 = np.random.gamma(shape=3, scale=2, size=10000)

# Plot the data
plt.plot(data1, 'o', label='Uniform')

# Plot the data and make it semi-transparent
plt.plot(data2, 'x', label='Skewed', alpha=0.3)

plt.legend()
plt.xlabel('Data point')
plt.ylabel('Value')

plt.show()

# Calculate the sum of the two datasets
data_sum = data1 + data2

# Calculate the average of the two datasets
data_avg = (data1 + data2) / 2

# Plot the distributions of the data
plt.hist(data_sum, bins=50, density=True, alpha=0.5, label='Sum')
plt.hist(data_avg, bins=50, density=True, alpha=0.5, label='Average')

plt.legend()
plt.xlabel('Value')
plt.ylabel('Probability Density')

plt.show()