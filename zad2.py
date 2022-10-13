import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


plt.rcParams["figure.figsize"] = (8,5)


val_range = [0.2, 0.5, 0.8, 1, 1.5, 1.7, 2 ]
x = np.linspace(-5, 5, 100)

# 2 ============================================
for val in val_range:
    plt.plot(x, stats.norm.pdf(x, 0, val), label=f'std={val}')
    plt.legend()
plt.title('GDP')
plt.show()

# 3 ============================================
for val in val_range:
    plt.plot(x, stats.norm.cdf(x, 0, val), label=f'std={val}')
    plt.legend()
plt.title('GCD')
plt.show()

# 4 ============================================
plt.rcParams["figure.figsize"] = (8,10)

plt.subplots_adjust(hspace=0.4)
plt.subplot(2, 1, 1)
for val in val_range:
    plt.plot(x, stats.norm.pdf(x, 0, val), label=f'std={val}')
    plt.legend()
plt.title('GDP')

plt.subplot(2, 1, 2)
for val in val_range:
    plt.plot(x, stats.norm.cdf(x, 0, val), label=f'std={val}')
    plt.legend()
plt.title('GCD')
plt.show()

# 5 ============================================
plt.rcParams["figure.figsize"] = (8,5)

x = np.linspace(0, 10, 11)
rv = stats.binom(10, 0.5)
plt.vlines(x, 0, rv.pmf(x), colors='r')
plt.scatter(x, rv.pmf(x), label='Bi(10,0.5)', color='r')

rv = stats.binom(10, 0.1)
plt.vlines(x, 0, rv.pmf(x), colors='g')
plt.scatter(x, rv.pmf(x), label='Bi(10,0.1)', color='g', marker='x')
plt.legend()
plt.title('Binominal probability mass function')
plt.show()

# 6 ============================================
x = np.linspace(0, 5, 20)
val_range = np.arange(0,5,0.5)
for val in val_range:
    rv = stats.poisson(val)
    plt.plot(x, rv.pmf(x), label=f'{val}')
    plt.scatter(x, rv.pmf(x),marker='x')
plt.title('Poisson probability mass function')
plt.legend()
plt.show()