#!/usr/bin/env python3
# nyquist_unknown.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator


def f(x):
    return (np.sin(4 * np.pi * x) * np.sin(6 * np.pi * x) *
            np.sin(10 * np.pi * x) * np.sin(14 * np.pi * x))


def plot(ax):
    a = 0
    b = 210
    # TODO: Adjust the number of samples (420, etc.)
    num_samples = 420

    x = np.linspace(a, b, num_samples + 1)
    y = f(x)

    ax.set_title("Unknown Waveform")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-1.1, 1.2)

    ax.axhline(y=0.0, color="lightgray")

    ax.plot(x, y, color='blue', linestyle='solid', marker='o',
            markerfacecolor='red', markersize=2, markeredgecolor='red')

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
