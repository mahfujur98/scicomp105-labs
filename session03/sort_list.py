#!/usr/bin/env python3
# sort_list.py

import numpy as np


def main():
    np.random.seed(2021)

    samples = []
    for i in range(100):
        samples.append(np.random.randint(1, 101))

    print(f"Unsorted: {samples}")

    last_index = len(samples) - 1
    is_sorted = False
    while not is_sorted:
        swap_needed = False
        for i in range(last_index):
            if samples[i] > samples[i+1]:
                temp = samples[i]
                samples[i] = samples[i+1]
                samples[i+1] = temp
                swap_needed = True
        if not swap_needed:
            is_sorted = True
        else:
            last_index -= 1

    print(f"Sorted: {samples}")


if __name__ == "__main__":
    main()
