#!/usr/bin/env python3
# mc_hypersphere.py

import numpy as np
from numba import vectorize, float64, int32


@vectorize([float64(int32, int32)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n/p)
    return h


def calc_hypersphere_volume():
    iterations = 6_250_000

    primes = [2, 3, 5, 7]

    x = halton(np.arange(iterations), primes[0]) * 2 - 1
    y = halton(np.arange(iterations), primes[1]) * 2 - 1
    z = halton(np.arange(iterations), primes[2]) * 2 - 1
    w = halton(np.arange(iterations), primes[3]) * 2 - 1

    d = x**2 + y**2 + z**2 + w**2

    est_volume = np.count_nonzero(d <= 1.0) / iterations * 16
    act_volume = np.pi ** 2 / 2.0
    err = np.abs((act_volume - est_volume) / act_volume)

    print(f"Total dots   = {iterations:,}\n"
          f"Act. Volume = {act_volume:.6f}\n"
          f"Est. Volume = {est_volume:.6f}\n"
          f"Abs. % Err   = {err:.6%})\n")


def main():
    calc_hypersphere_volume()


if __name__ == "__main__":
    main()
