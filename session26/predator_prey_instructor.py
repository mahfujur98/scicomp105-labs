#!/usr/bin/env python3
# predator_prey_instructor.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy.integrate import solve_ivp


def model(time, vec):
    # Lotka-Volterra
    alpha, beta, delta, gamma = 2.0, 1.1, 1.0, 0.9
    prey, pred = vec
    # TODO: Express the correct differential equations
    d_prey = alpha * prey - beta * prey * pred
    d_pred = delta * prey * pred - gamma * pred
    return [d_prey, d_pred]


def plot(ax):
    t0, tf, ts = 0, 20, 1000    # dimensionless

    prey_0, pred_0 = 1.0, 0.5   # % of population

    sol = solve_ivp(model, (t0, tf),
                    [prey_0, pred_0],
                    max_step=(tf - t0) / ts)
    t = sol.t
    prey, pred = sol.y

    ax.set_title("Lotka-Volterra (scipy solve_ivp)")
    ax.set_xlabel("time")
    ax.set_ylabel("population")

    ax.plot(t, pred, label="predator", color="red")
    ax.plot(t, prey, label="prey", color="blue")
    ax.legend(loc="upper right")

    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))

    ax.figure.set_size_inches(11, 8.5)
    ax.figure.savefig("predator_prey.png", dpi=600)
    ax.figure.savefig("predator_prey.pdf",
                      dpi=600, orientation='landscape')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
