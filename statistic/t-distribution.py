import numpy as np

from scipy import stats


n = 15 #наблюдений в выборке
tt = -2 # t-значение

pval = stats.t.sf(np.abs(tt), n-1)*2  # two-sided pvalue = Prob(abs(t)>tt)
print('t-statistic = %6.3f pvalue = %6.4f' % (tt, pval))