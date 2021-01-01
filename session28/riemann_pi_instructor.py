#!/usr/bin/env python3
# riemann_pi_instructor.py

import numpy as np
import sympy


def main():
    for n in range(1, 7):
        # Use sympy to calculate the Riemann Pi for 10^n
        # TODO: Fix this next line of code
        riemann_pi = int(sympy.primepi(10**n))
        print(f"pi(10^{n}) = {riemann_pi:,}")


if __name__ == "__main__":
    main()
