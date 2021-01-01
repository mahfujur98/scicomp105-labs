#!/usr/bin/env python3
# collatz_conjecture_instructor.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator


def stop_time(n):
    counter = 0
    # TODO: Insert your code here
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        counter += 1
    return counter


def plot(ax):
    max_n = int(100_000)

    print("Calculating the Collatz stopping time for"
          f" the first {max_n:,} natural numbers . . .")

    x = np.arange(1, max_n, dtype=np.int)
    y = np.vectorize(stop_time)(x)

    ax.set_title(f"Collatz Conjecture (n < {max_n:,})")
    ax.set_xlabel("Stopping Time")
    ax.set_ylabel("Count")

    ax.hist(y, bins=500, color='blue')

    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.figure.savefig("collatz_conjecture_instructor.png", dpi=600)


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
