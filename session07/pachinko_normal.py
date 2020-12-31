#!/usr/bin/env python3
# pachinko_normal.py

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import scipy.stats as stats
from scipy.stats import ks_2samp
from numba import jit


def stegun_normal(mean, std_dev):
    q = 1 - np.random.random()
    p = q if q < 0.5 else 1 - q
    t = np.sqrt(np.log(1/p**2))
    x = (t - (2.515517 + 0.802853 * t + 0.010328 * (t*t)) /
         (1 + 1.432788 * t + 0.189269 * (t*t) + 0.001308*(t*t*t)))
    x = x if q < 0.5 else -x
    return x * std_dev + mean


@jit(nopython=True)
def pachinko_normal(balls, levels):
    np.random.seed(2016)
    drops = np.zeros(balls)
    for idx in range(balls):
        slot = 0
        for _ in range(levels):
            slot += -1 if np.random.rand() < 0.5 else 1
        drops[idx] = slot // 2
    return drops


def plot(ax):
    levels = 12
    balls = 100000

    x = pachinko_normal(balls, levels)
    ax.hist(x, levels + 1, density=True, label="Pachinko")

    y = np.linspace(np.min(x), np.max(x), 2 * levels + 1)
    ax.plot(y, stats.norm.pdf(y, np.mean(x), np.std(x)),
            color='red', linewidth=2, label="Normal")

    p = ks_2samp(x, y)[1]

    ax.set_title(f"Pachinko as Normal PDF? (p={p:.2%})")
    ax.set_xlabel('Standard Deviations')
    ax.set_ylabel('Probability')
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(0.0, 0.3)
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.grid()
    ax.legend()

    ax.figure.set_size_inches(11, 8.5)
    ax.figure.savefig(f"pachinko_normal.png")
    ax.figure.savefig(f"pachinko_normal.pdf",
                      dpi=600, orientation='landscape')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
