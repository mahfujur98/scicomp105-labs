#!/usr/bin/env python3
# surface_sampling_sphere.py

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt


def plot_incorrect(ax):
    num_samples = 15000

    u = random.rand(num_samples) * np.pi       # poloidal angle
    v = random.rand(num_samples) * 2 * np.pi   # toroidal angle

    x = np.sin(u)*np.sin(v)
    y = np.sin(u)*np.cos(v)
    z = np.cos(u)

    ax.set_title("Incorrect Sampling")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.view_init(azim=-72, elev=48)

    pixel_size = (72 / ax.figure.dpi)**2
    ax.scatter(x, y, z, marker='.', s=pixel_size, depthshade=False)


def plot_correct(ax):
    num_samples = 15000

    u = np.arccos(2 * random.rand(num_samples) - 1)     # polodial angle
    v = random.rand(num_samples) * 2 * np.pi            # torodial angle

    x = np.sin(u)*np.sin(v)
    y = np.sin(u)*np.cos(v)
    z = np.cos(u)

    ax.set_title("Correct Sampling")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.view_init(azim=-72, elev=48)

    pixel_size = (72 / ax.figure.dpi)**2
    ax.scatter(x, y, z, marker='.', s=pixel_size, depthshade=False)


def main():
    fig = plt.figure(constrained_layout=True)
    fig.set_size_inches(12, 7)

    gs = fig.add_gridspec(1, 2)

    ax = fig.add_subplot(gs[0, 0], projection='3d')
    plot_incorrect(ax)

    ax = fig.add_subplot(gs[0, 1], projection='3d')
    plot_correct(ax)

    plt.show()


if __name__ == "__main__":
    main()
