#!/usr/bin/env python3
# nyquist_known.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator


def plot(ax):
    a = 0
    b = 20
    # TODO: Adjust the number of samples (16, 15, 17, 31, 32, 33)
    num_samples = 16

    x = np.linspace(a, b, num_samples + 1)
    print(x.shape)
    print(x)
    y = np.sin(4 / 5 * np.pi * x)

    ax.set_title(r"$y = \sin(\frac{4}{5} \pi x )$")
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
