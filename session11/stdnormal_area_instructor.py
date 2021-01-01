#!/usr/bin/env python3
# stdnormal_area_instructor.py

import numpy as np
import scipy.integrate


def f(x):
    # TODO: Implement the correct integrand
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2/2)


def main():
    # TODO: Fix this next line of code
    integral = scipy.integrate.quad(f, -1, 1)[0]

    # See https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
    print(f"Est CDF = {integral}")


if __name__ == "__main__":
    main()
