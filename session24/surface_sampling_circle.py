#!/usr/bin/env python3
# surface_sampling_circle.py

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random


def plot_incorrect(ax):
    num_samples = 10000

    v = np.linspace(0, 2 * np.pi, num_samples)  # toroidal angle
    r = random.rand(num_samples)

    x = r * np.cos(v)
    y = r * np.sin(v)

    pixel_size = (72 / ax.figure.dpi)**2
    ax.scatter(x, y, marker='.', s=pixel_size)

    ax.set_title("Incorrect Sampling")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.set_aspect('equal')


def plot_correct(ax):
    num_samples = 10000

    v = np.linspace(0, 2 * np.pi, num_samples)  # toroidal angle
    r = random.rand(num_samples)

    # From https://mathworld.wolfram.com/DiskPointPicking.html
    x = np.sqrt(r) * np.cos(v)
    y = np.sqrt(r) * np.sin(v)

    pixel_size = (72 / ax.figure.dpi)**2
    ax.scatter(x, y, marker='.', s=pixel_size)

    ax.set_title("Correct Sampling")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.set_aspect('equal')


def main():
    fig = plt.figure()
    fig.set_size_inches(12, 7)

    gs = fig.add_gridspec(1, 2)

    ax = fig.add_subplot(gs[0, 0])
    plot_incorrect(ax)

    ax = fig.add_subplot(gs[0, 1])
    plot_correct(ax)

    plt.show()


if __name__ == "__main__":
    main()
