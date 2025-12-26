import statistics

import matplotlib.pyplot as plt
import numpy as np


data = [185, 175, 170, 169, 171, 175, 157, 170, 172, 172, 172, 172, 167, 173, 168, 167, 166, 167, 169, 177, 178, 165,
        161, 179, 159, 164, 178, 170, 173, 171]

print("размах: ", np.ptp(data)) #исключает NaN число
print("min: ", np.nanmin(data))
print("max: ", np.nanmax(data))