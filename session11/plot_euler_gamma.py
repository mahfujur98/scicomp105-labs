#!/usr/bin/env python3
# plot_euler_gamma.py

import matplotlib.pyplot as plt
import numpy as np


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return int(n) * factorial_recursive(n-1)


def f(x, s):
    try:
        return np.power(x, s - 1) * np.exp(-x)
    except ZeroDivisionError:
        return 0


def simpsons_rule(f, s, a, b, intervals):
    dx = (b - a) / intervals
    area = f(a, s) + f(b, s)
    for i in range(1, int(intervals)):
        area += f(a + i * dx, s) * (2 * (i % 2 + 1))
    return dx / 3 * area


def euler_gamma(s):
    return simpsons_rule(f, s, 0, 1e3, 1e5)


def factorial_gamma(x):
    return np.round(euler_gamma(x + 1), 5)


def plot(ax):
    xa = np.linspace(0, 5, 100)

    ax.plot(xa, factorial_gamma(xa), label=r'$\Gamma \left( x + 1 \right)$')

    n = [factorial_recursive(i) for i in range(6)]

    ax.plot(range(len(n)), n, color='red', marker='o', label='$n!$')

    ax.set_title(f"Factorial Via Euler's Gamma Function")
    ax.set_xlabel('x')
    ax.set_ylabel('Factorial (x)')
    ax.grid()
    ax.legend(loc='best')

    ax.set_xlim(0, 5.1)
    # TODO: Uncomment these two lines to zoom into a smaller region
    #ax.set_xlim(0, 2.1)
    #ax.set_ylim(0.5, 2.1)

    ax.figure.set_size_inches(11, 8.5)
    ax.figure.savefig(f"plot_euler_gamma.png", dpi=600)
    ax.figure.savefig(f"plot_euler_gamma.pdf",
                      dpi=600, orientation='landscape')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
