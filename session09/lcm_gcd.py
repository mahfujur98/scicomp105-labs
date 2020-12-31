#!/usr/bin/env python3
# lcm_gcd.py

import numpy as np


def main():
    a = 447618
    b = 2011835

    gcd = np.gcd(a, b)

    # TODO: Fix this next line of code
    lcm = 0

    print(f"a = {a:,}")
    print(f"b = {b:,}")
    print(f"gcd(a,b) = {gcd:,}")
    print(f"lcm(a, b) = {lcm:,}")


if __name__ == "__main__":
    main()
