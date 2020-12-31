#!/usr/bin/env python3
# idw2.py

import numpy as np
import mayavi.mlab as mlab
from numba import jit


def act_height(x, y):
    # Calculate the height of the "actual" ocean at (x,y)
    # TODO: Fix this next line of code
    return 0


def init_samples():
    np.random.seed(2016)

    global ocean_size, num_intervals, num_samples
    ocean_size, num_intervals, num_samples = 390, 65, 220

    global grid_x, grid_y, grid_z
    grid_x, grid_y = np.mgrid[0:ocean_size:complex(0, num_intervals),
                              0:ocean_size:complex(0, num_intervals)]
    grid_z = act_height(grid_x, grid_y)

    global samples_x, samples_y, samples_z
    samples_x = np.random.uniform(0, ocean_size, num_samples)
    samples_y = np.random.uniform(0, ocean_size, num_samples)
    samples_z = act_height(samples_x, samples_y)


@jit(nopython=True)
def calc_idw_height(xi, yi, p):
    sum_weight = 0.0
    sum_height_weight = 0.0
    for si in range(num_samples):
        distance = np.hypot(grid_x[xi, xi] - samples_x[si],
                            grid_y[yi, yi] - samples_y[si])
        if distance == 0:
            return samples_z[si]
        weight = 1 / np.power(distance, p)
        sum_weight += weight
        sum_height_weight += samples_z[si] * weight
    return sum_height_weight / sum_weight


def est_height(p):
    global est_z
    est_z = np.zeros_like(grid_x)
    for xi in range(num_intervals):
        for yi in range(num_intervals):
            est_z[xi, yi] = calc_idw_height(xi, yi, p)
    return est_z


def plot(idw_plot_type):

    if idw_plot_type == 1:
        mlab.surf(grid_x, grid_y, grid_z, colormap='ocean')

    if idw_plot_type == 2:
        mlab.surf(grid_x, grid_y, est_z, colormap='ocean')

    if idw_plot_type == 3:
        mlab.surf(grid_x, grid_y, grid_z,
                  colormap='Blues', representation='wireframe')

        mlab.surf(grid_x, grid_y, est_z, colormap='Reds',
                  representation='wireframe')

    if idw_plot_type == 1 or idw_plot_type == 2:
        mlab.points3d(samples_x, samples_y, samples_z,
                      scale_factor=3, color=(1, 0, 0))

    mlab.show()


def main():
    init_samples()
    est_height(p=2)
    plot(idw_plot_type=2)


if __name__ == "__main__":
    main()
