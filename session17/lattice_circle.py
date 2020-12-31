#!/usr/bin/env python3
# lattice_circle.py

import numpy as np
from numba import jit

# See https://en.wikipedia.org/wiki/Gauss_circle_problem


@jit(nopython=True)
def lattice_points(radius):
    num_points = 0
    # TODO: Implement your function here
    '''



    '''
    return num_points


def main():
    for radius in range(1000, 10001, 1000):
        # TODO: Fix these next two lines of code
        act_points = 0
        est_points = 0
        print(f"Radius = {radius:>6,}"
              f"  Act Points = {act_points:>12,}"
              f"  Est Points = {est_points:>12,}")


if __name__ == "__main__":
    main()
