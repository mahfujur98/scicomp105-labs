#!/usr/bin/env python3
# hamming_weight.py

import numpy as np


def pop_count(n):
    count_onebits = 0
    # TODO: Implement the function here
    # See https://en.wikipedia.org/wiki/Hamming_weight
    '''

    '''
    return count_onebits


def main():
    n = 95601

    hw = pop_count(n)

    print(f"The Hamming weight of = {n:,}"
          f" in base 2 is {hw:,}")

    hw = bin(n).count('1')
    print(f"The Hamming weight of = {n:,}"
          f" in base 2 is {hw:,}")


if __name__ == "__main__":
    main()
