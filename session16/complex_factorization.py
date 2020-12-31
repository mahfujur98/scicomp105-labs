#!/usr/bin/env python3
# complex_factorization.py

import numpy as np
from sympy import prime, sieve


def main():
    num_odd_primes = 25

    # Comprehension to generate list of first odd primes
    # sympy: prime(1) = 2, prime(2) = 3, etc.
    primes = [prime(n) for n in range(2, num_odd_primes + 2)]

    for p in primes:
        for a in range(1, np.int(np.sqrt(p))):
            b = np.sqrt(p - a**2)
            if b == np.floor(b):
                z1 = np.complex(a, b)
                z2 = np.complex(a, -b)
                print(f"{p:>3} = {z1}{z2}")
                break


if __name__ == "__main__":
    main()
