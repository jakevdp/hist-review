"""
Histogram Pitfalls
------------------
This script visualizes several potential pitfalls of non-rigorous use of
histograms.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, cauchy


fig, ax = plt.subplots(2, 2)

#----------------------------------------------------------------------
# Top panels: 
# Small number statistics and bin location
np.random.seed(104)
x = np.concatenate([norm(-1, 0.5).rvs(10),
                        norm(1, 0.5).rvs(10)])
bins = np.linspace(-3, 3, 13)

hist_kwargs = dict(histtype='stepfilled', fc='blue', alpha=0.5)
ax[0, 0].hist(x, bins, **hist_kwargs)
ax[0, 1].hist(x, bins + 0.25, **hist_kwargs)

for axi in ax[0]:
    axi.set_xlim(-2.2, 2.2)
    axi.set_ylim(0, 7)
    axi.set_xlabel('$x$')
    axi.set_ylabel('$N(x)$')


#----------------------------------------------------------------------
# Bottom panels:
# Effect of over and under smoothing
x = np.concatenate([norm(0, 0.6).rvs(1500),
                    cauchy(-0.9, 0.05).rvs(500),
                    cauchy(-0.6, 0.08).rvs(400),
                    cauchy(0, 0.6).rvs(600),
                    cauchy(0.3, 0.1).rvs(400)])

bins1 = np.linspace(-2.5, 2.5, 12)
bins2 = np.linspace(-2.5, 2.5, 120)

hist_kwargs = dict(histtype='stepfilled', fc='gray', normed=True, alpha=0.5)
ax[1, 0].hist(x, bins1, **hist_kwargs)
ax[1, 0].set_ylim(0, 0.601)

ax[1, 1].hist(x, bins2, **hist_kwargs)
ax[1, 1].set_ylim(0, 1.201)

for axi in ax[1]:
    axi.set_xlim(-2.5, 2.5)
    axi.set_xlabel('$x$')
    axi.set_ylabel('$p(x)$')

plt.show()
