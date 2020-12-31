#!/usr/bin/env python3
# complex_algebra.py

import numpy as np


def main():
    z1 = np.complex(-5.9, -7.5)
    z2 = np.complex(np.sqrt(2), np.pi)

    print(f"z1 = {z1:.4f}")
    print(f"z2 = {z2:.4f}")

    print(f"z1 + z2 = {z1+z2:.4f}")
    print(f"z1 - z2 = {z1-z2:.4f}")
    print(f"z1 * z2 = {z1*z2:.4f}")
    print(f"z1 / z2 = {z1/z2:.4f}")

    zp = np.power(z1, 2)
    print(f"z1^2 = {zp:.4f}")


if __name__ == "__main__":
    main()
