#!/usr/bin/env python3
# euler_identity.py

import numpy as np


def main():
    z = np.complex(0, np.pi)
    ez = 1

    for p in range(1, 21):
        ez += np.power(z, p) / np.math.factorial(p)

    print(f"e^{z:.6f} = {ez:.6f}")


if __name__ == "__main__":
    main()
