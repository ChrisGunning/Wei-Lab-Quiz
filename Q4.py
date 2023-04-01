import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, binom

n = 10
p = 0.7
x = np.arange(9)
binomial = binom.pmf(k=x,n=n, p=p)
plt.bar(x, binomial)
plt.xlabel('x', fontsize=14)
plt.ylabel('Probability', fontsize=14)
plt.xlim([5, 10])

plt.title('Distribution'.format(n, p),fontsize= 15)
plt.show()