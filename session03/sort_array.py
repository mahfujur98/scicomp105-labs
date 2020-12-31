#!/usr/bin/env python3
# sort_array.py

import numpy as np


def main():
    np.random.seed(2021)

    samples = np.random.randint(1, 101, 100)

    print(f"Unsorted: {samples}")

    print(f"Sorted: {np.sort(samples)}")


if __name__ == "__main__":
    main()
