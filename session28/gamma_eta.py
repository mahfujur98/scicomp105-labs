#!/usr/bin/env python3
# gamma_eta.py

import numpy as np
import mpmath
import scipy.integrate


def f(x, s):
    # TODO: Return the integrand value at x for the given s
    return 0


def main():
    # We want to calculate 5!
    n = 5

    # Gamma[n+1] == n! (See https://en.wikipedia.org/wiki/Gamma_function)
    s = n + 1

    # TODO: Use mpmath to calculate the Dirichlet's Eta value for s
    eta = 0

    # TODO: Use scipy to integrate f(x, s) from 0 to 1000
    integral = 0

    # TODO: Calculate gamma, given both the eta and integral values
    gamma = 0

    print(f"{n}! = {gamma}")
    print(f"{n}! = {np.math.factorial(n)}")


if __name__ == "__main__":
    main()
