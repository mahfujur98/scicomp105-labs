#!/usr/bin/env python3
# cramers_rule_instructor.py

import numpy as np


def main():
    np.set_printoptions(suppress=True)

    coeffs = np.array([[4, 5, -2], [7, -1, 2], [3, 1, 4]])
    vals = np.array([-14, 42, 28])
    print(np.linalg.solve(coeffs, vals))

    coeffs = np.array([[-6, 5, -2], [-2, 1, 4], [4, -5, 5]])
    vals = np.array([-11, -9, -4])
    print(np.linalg.solve(coeffs, vals))

    coeffs = np.array([[-3, -1, -3], [-5, 3, 6], [-6, -4, 1]])
    vals = np.array([-8, -4, -20])
    print(np.linalg.solve(coeffs, vals))


if __name__ == "__main__":
    main()
