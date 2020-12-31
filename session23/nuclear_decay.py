#!/usr/bin/env python3
# nuclear_decay.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator

# TODO: Uncomment the second line to analyze Carbon-14
atom = ("Fluorine-18", "hours", 6586.0 / 60 / 60, 12)
#atom = ("Carbon-14", "years", 5730, 40000)

atom_name, time_scale, half_life, time_stop = atom


def d_n(n, t):
    # Radioactive decay rate
    return - n / half_life


def euler(v1, u, h, f1):
    # Implements Euler's method
    # for a single ODE (f1), with one
    # dependent variable (v1) and the
    # independent variable (u) having step size (h)
    next_v1 = v1 + f1(v1, u) * h
    next_u = u + h
    return next_v1, next_u


def plot(ax):
    time_steps = 100
    delta_time = time_stop / time_steps

    time_array = np.zeros(time_steps)
    nuclei_array = np.zeros(time_steps)

    time_array[0] = 0  # set initial time value
    nuclei_array[0] = 100  # set initial concentration (in upper atmosphere)

    time = time_array[0]
    nuclear = nuclei_array[0]

    for step in range(1, time_steps):
        nuclear, time = euler(nuclear, time, delta_time, d_n)
        nuclei_array[step] = nuclear
        time_array[step] = time

    ax.set_title(f"{atom_name} Radioactive Decay (Euler's Method)")
    ax.set_xlabel(f"time ({time_scale})")
    ax.set_ylabel("concentration")

    ax.plot(time_array, nuclei_array, color='red', linestyle='solid')

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.figure.savefig(f"nuclear_decay ({atom_name}).png", dpi=600)


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
