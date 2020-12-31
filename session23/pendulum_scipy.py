#!/usr/bin/env python3
# pendulum_scipy.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy.integrate import solve_ivp


def model(time, vec):
    omega, theta = vec
    d_omega = -9.81 / 1.0 * np.sin(theta)
    d_theta = omega
    return [d_omega, d_theta]


def plot(ax):
    t0, tf, ts = 0, 10, 1000  # secs

    omega_0, theta_0 = 0, np.radians(75)  # degrees

    sol = solve_ivp(model, (t0, tf),
                    [omega_0, theta_0],
                    max_step=(tf - t0) / ts)
    t = sol.t
    omega, theta = sol.y

    ax.plot(t, theta, label='theta')
    ax.plot(t, omega, label='omega')

    ax.set_title("Simple Pendulum (scipy solve_ivp)")
    ax.set_xlabel("time (secs)")
    ax.set_ylabel("theta (degrees)")
    ax.axhline(y=0.0, color="lightgray")
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.legend()

    ax.figure.set_size_inches(11, 8.5)
    ax.figure.savefig("pendulum_scipy.png", dpi=600)
    ax.figure.savefig("pendulum_scipy.pdf",
                      dpi=600, orientation='landscape')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
