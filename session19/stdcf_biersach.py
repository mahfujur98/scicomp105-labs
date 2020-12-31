#!/usr/bin/env python3
# stdcf_biersach.py

import math

MAX_TERMS = 7


def normalize_cf(cf):
    if len(cf) > 2:
        if cf[-1] == 1 and cf[-2] != 1:
            cf[-2] += 1
            cf.pop(-1)
    return cf


def encode_cf(x):
    cf = []
    while len(cf) < MAX_TERMS:
        cf.append(math.floor(x))
        x = x - math.floor(x)
        if x < 1e-11:
            break
        x = 1 / x
    return normalize_cf(cf)


def main():
    for n in range(1, 10):
        # TODO: Fix the next line of code
        x = 0
        cf = encode_cf(x)
        print(f"{n} : {cf}")


if __name__ == "__main__":
    main()
