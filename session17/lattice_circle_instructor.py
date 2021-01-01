#!/usr/bin/env python3
# lattice_circle_instructor.py

import numpy as np
from numba import jit

# See https://en.wikipedia.org/wiki/Gauss_circle_problem


@jit(nopython=True)
def lattice_points(radius):
    num_points = 0
    # TODO: Implement your function here
    radius_squared = radius**2
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if x**2 + y**2 <= radius_squared:
                num_points += 1
    return num_points


def main():
    for radius in range(1000, 10001, 1000):
        # TODO: Fix these next two lines of code
        act_points = lattice_points(radius)
        est_points = int(np.pi*radius**2+2*np.sqrt(2*np.pi*radius))
        print(f"Radius = {radius:>6,}"
              f"  Act Points = {act_points:>12,}"
              f"  Est Points = {est_points:>12,}")


if __name__ == "__main__":
    main()
