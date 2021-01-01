#!/usr/bin/env python3
# gamma_eta_instructor.py

import numpy as np
import mpmath
import scipy.integrate


def f(x, s):
    # TODO: Return the integrand value at x for the given s
    return np.power(x, s - 1)/(np.exp(x) + 1)


def main():
    # We want to calculate 5!
    n = 5

    # Gamma[n+1] == n! (See https://en.wikipedia.org/wiki/Gamma_function)
    s = n + 1

    # TODO: Use mpmath to calculate the Dirichlet's Eta value for s
    eta = float(mpmath.altzeta(s))

    # TODO: Use scipy to integrate f(x, s) from 0 to 1000
    integral = scipy.integrate.quad(f, 0, 1000, args=(s,))[0]

    # TODO: Calculate gamma, given both the eta and integral values
    gamma = int(integral / eta)

    print(f"{n}! = {gamma}")
    print(f"{n}! = {np.math.factorial(n)}")


if __name__ == "__main__":
    main()
