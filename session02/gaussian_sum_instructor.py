#!/usr/bin/env python3
# gaussian_sum_instructor.py


def main():
    n = 1_000

    sum = 0

    # TODO: Fix this for loop to calculate the sum
    for k in range(n + 1):
        sum += k

    print(f"Sum by looping = {sum:,}")

    # TODO: Find sum by Gauss' shortcut
    sum = n * (n + 1) // 2

    print(f"Gaussian sum   = {sum:,}")


if __name__ == "__main__":
    main()
