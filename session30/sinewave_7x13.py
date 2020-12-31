#!/usr/bin/env python3
# sinewave_7x13.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator


def plot(ax):
    # TODO: Fix these next two lines of code
    x = np.linspace(0, 0, 0)
    y = x

    ax.set_title(r"$y = \sin(\frac{14}{13} \pi x )$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.axhline(y=0.0, color="lightgray")

    ax.plot(x, y, color='blue', linestyle='solid', marker='o',
            markerfacecolor='red', markersize=2, markeredgecolor='red')

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.figure.savefig("sinewave_7x13.png", dpi=600)


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
