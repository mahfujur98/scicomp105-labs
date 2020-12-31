#!/usr/bin/env python3
# epidemiology_sir.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy.integrate import solve_ivp


def model(time, vec):
    # Kermack-McKendrick (S-I-R)
    beta = .003
    delta = 1.0
    s, i, r = vec
    ds = -beta * s * i
    di = beta * s * i - delta * i
    dr = delta * i
    return ds, di, dr


def plot(ax):
    t0, tf, ts = 0, 10, 100  # months

    s0 = 1000  # Number of people that are susceptible
    i0 = 1     # Number of people that are infected
    r0 = 0     # Number of people that are recovered

    sol = solve_ivp(model, (t0, tf), [s0, i0, r0],
                    dense_output=True, max_step=(tf - t0) / ts)
    t = sol.t
    s, i, r = sol.y

    ax.plot(t, s, label="Susceptible")
    ax.plot(t, i, label="Infected")
    ax.plot(t, r, label="Recovered")

    ax.set_title("Epidemiology (S-I-R)")
    ax.set_xlabel("time")
    ax.set_ylabel("Population")

    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.legend()

    ax.figure.set_size_inches(11, 8.5)
    ax.figure.savefig("epidemiology_sir.png", dpi=600)
    ax.figure.savefig("epidemiology_sir.pdf",
                      dpi=600, orientation='landscape')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
