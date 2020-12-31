#!/usr/bin/env python3
# plot_rings.py

import matplotlib.pyplot as plt
import numpy as np


def plot(ax):
    radius = 25
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # TODO: Fix these next two lines
    x_offset = 0
    y_offset = 0

    ax.plot(x, y, color='black', linewidth=12)
    ax.plot(x - x_offset, y, color='blue', linewidth=12)
    ax.plot(x + x_offset, y, color='red', linewidth=12)
    ax.plot(x - x_offset / 2, y - y_offset, color='yellow', linewidth=12)
    ax.plot(x + x_offset / 2, y - y_offset, color='green', linewidth=12)

    ax.set_title("The Olympic Rings")
    ax.set_aspect('equal')
    ax.axis('off')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
