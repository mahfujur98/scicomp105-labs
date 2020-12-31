#!/usr/bin/env python3
# cramers_rule.py

import numpy as np


def main():
    coeffs = np.array([[4, 5, -2], [7, -1, 2], [3, 1, 4]])
    vals = np.array([-14, 42, 28])

    # Calculate determinant of coefficients matrix
    det_coeffs = np.linalg.det(coeffs)

    # Overlay value vector on each column of the coeffs matrix
    xa = np.copy(coeffs)
    xa[:, 0] = vals
    det_xa = np.linalg.det(xa)

    ya = np.copy(coeffs)
    ya[:, 1] = vals
    det_ya = np.linalg.det(ya)

    za = np.copy(coeffs)
    za[:, 2] = vals
    det_za = np.linalg.det(za)

    # Use Cramer's rule to solve 3 x 3 system of linear equations
    x = det_xa / det_coeffs
    y = det_ya / det_coeffs
    z = det_za / det_coeffs

    print(f"x = {x:,.4f}")
    print(f"y = {y:,.4f}")
    print(f"z = {z:,.4f}")


if __name__ == "__main__":
    main()
