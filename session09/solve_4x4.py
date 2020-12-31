#!/usr/bin/env python3
# solve_4x4.py

import numpy as np


def main():
    np.set_printoptions(suppress=True)

    # TODO: Update these next two statements
    coeffs = np.array([[1, 0], [0, 1]])
    vals = np.array([0, 0])

    print(np.linalg.solve(coeffs, vals))


if __name__ == "__main__":
    main()
