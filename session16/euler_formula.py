#!/usr/bin/env python3
# euler_formula.py

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


def plot_euler_formula(ax):
    # Plot y = e^xi
    theta = np.linspace(0, 2*np.pi, 1000, endpoint=True)
    z = np.zeros(len(theta), dtype=np.complex)

    for idx, val in enumerate(theta):
        z[idx] = np.exp(np.complex(0, val))

    ax.plot(np.real(z), np.imag(z), color='blue', linewidth=2,
            label=r"$e^{i x}$")


def plot_exponential_curve(ax):
    # Plot y = e^x
    x = np.linspace(-2, 2, 1000, endpoint=True)
    ax.plot(x, np.exp(x), color='green', label=r'$e^x$')


def plot_complex_point1(ax):
    # Plot a complex exponential on this Argand diagram
    z = 1.4 * np.exp(np.complex(0, 0.47))
    x, y = np.real(z), np.imag(z)
    ax.scatter(x, y, color='black')

    line_hypot = [(0, 0), (x, y)]
    line_opp = [(x, 0), (x, y)]
    line_adj = [(0, 0), (x, 0)]
    lc = LineCollection([line_hypot, line_opp, line_adj],
                        color='red', zorder=2.5)
    ax.add_collection(lc)

    ax.annotate(r"$1.7e^{0.62 i}$", xy=(x, y), size=15, color='black',
                xytext=(5, 0), textcoords='offset pixels')

    ax.annotate(r"$1.7\sin(0.62)$", xy=(x, y/3), color='red',
                xytext=(5, 0), textcoords='offset pixels')

    ax.annotate(r"$1.7\cos(0.62)$", xy=(x/3, 0), color='red',
                xytext=(0, 5), textcoords='offset pixels')


def plot_complex_point2(ax):
    # Plot -1-1.5j as complex exponential
    x, y = -1, -1.5
    z = np.complex(x, y)
    hypot = np.hypot(np.real(z), np.imag(z))
    theta = np.arctan(np.imag(z)/np.real(z)) - np.pi
    ax.scatter(-1, -1.5, color='purple')
    line_hypot = [(0, 0), (x, y)]
    line_opp = [(x, 0), (x, y)]
    line_adj = [(0, 0), (x, 0)]
    lc = LineCollection([line_hypot, line_opp, line_adj],
                        color='purple', zorder=2.5)
    ax.add_collection(lc)
    ax.annotate(rf"$({x}{y}i) = {hypot:.3f}e^{{ {theta:.3f} i }}$",
                xy=(x, y), xytext=(-35, -25), textcoords='offset pixels',
                color='purple')


def decorate_plot(ax):
    # Decorate plot
    ax.grid()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axvline(x=0, color='black', linewidth=2)
    ax.axhline(y=0, color='black', linewidth=2)
    ax.set_title(r"Euler's Formula: "
                 r"$z = e^{ \pm i\theta } = \cos \theta \pm i\sin \theta$")
    ax.set_xlabel("Real z")
    ax.set_ylabel("Imaginary z")
    ax.legend(loc="best")


def save_plot(ax):
    ax.figure.set_size_inches(11, 8.5)
    ax.figure.savefig("euler_formula.png", dpi=600)
    ax.figure.savefig("euler_formula.pdf",
                      dpi=600, orientation='landscape')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])

    plot_exponential_curve(ax)
    plot_euler_formula(ax)
    plot_complex_point1(ax)
    plot_complex_point2(ax)

    decorate_plot(ax)
    save_plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
