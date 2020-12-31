#!/usr/bin/env python3
# make_samples.py

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np
import os
import sys


def f(x):
    return (29 * np.cos(3 * x) + 7 * np.cos(19 * x)
            + 17 * np.sin(11 * x) + 2 * np.sin(31 * x))


def plot(ax):
    sample_duration = 2 * np.pi
    num_samples = 1000

    ts = np.linspace(0, sample_duration, num_samples, endpoint=False)
    ys = f(ts)

    file_name = os.path.dirname(sys.argv[0]) + '/samples.csv'
    np.savetxt(file_name, np.vstack((ts, ys)).T,
               fmt='%1.13f', delimiter=', ')

    ax.set_title(f"Sampled Wave ({num_samples} samples)")
    ax.set_xlabel("time")
    ax.set_ylabel("amplitude")

    ax.axhline(y=0.0, color='lightgray', linewidth=1)

    ax.plot(ts, ys, color='lightgray',
            marker='o', markerfacecolor='none',
            markersize=1, markeredgecolor='black')

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.figure.savefig("samples.png", dpi=600)


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
