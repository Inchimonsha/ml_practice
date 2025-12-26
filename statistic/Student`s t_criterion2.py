from math import sqrt
import scipy.stats as st
import numpy as np

sample_1 = [84.7, 105, 98.9, 97.9, 108.7, 81.3, 99.4, 89.4 , 93, 119.3, 99.2, 99.4, 97.1, 112.4, 99.8, 94.7, 114, 95.1, 115.5, 111.5]
sample_2 = [57.2, 68.6, 104.4, 95.1, 89.9, 70.8, 83.5, 60.1, 75.7, 102, 69, 79.6, 68.9, 98.6, 76, 74.8, 56, 55.6, 69.4, 59.5]

#----------------------------------------------------------------------------------------------------
n_1 = len(sample_1)
n_2 = len(sample_2)

mean_1 = sum(sample_1) / n_1
mean_2 = sum(sample_2) / n_2

dispersion_1_part1 = 0
dispersion_2_part1 = 0

dispersion_1 = sum((x - mean_1) ** 2 for x in sample_1) / (n_1 - 1)

dispersion_2 = sum((x - mean_2) ** 2 for x in sample_2) / (n_2 - 1)

sd_1 = sqrt(dispersion_1)
sd_2 = sqrt(dispersion_2)

print('Mean_1 = ', mean_1, '\n','Mean_2 = ', mean_2, '\n','sd_1 = ', sd_1, '\n','sd_2 = ', sd_2, '\n','n_1 = ', n_1, '\n','n_2 = ', n_2, sep='')
print()

#----------------------------------------------------------------------------------------------------
se = sqrt(sd_1 ** 2 / n_1 + sd_2 ** 2 / n_2)
t_criteria = (mean_1 - mean_2) / se
print("T_criteria = ", t_criteria, '\n',"se = ", se, sep='')
print()
#----------------------------------------------------------------------------------------------------
def p_value(t, n, area='bt'):
   global p
   df = n - 2

   if area == 'bt': # both tales
      p = 2 * (1 - st.t.cdf(abs(t), df))

   if area == 'lt': # lower tail
      p = st.t.cdf(t, df)

   if area == 'ut': #upper tail
      p = 1 - st.t.cdf(t, df)

   return round(p, 7)  # acuracy

t = t_criteria
n = n_1 + n_2
print('p_value = ', p_value(t, n))

if p_value(t, n) >= 0.05:
    print("H0 can't be rejected, means are statistically equal, no factor impact")
else:
    print("H0 can be rejected, means aren't statistically equal, factor impacts")