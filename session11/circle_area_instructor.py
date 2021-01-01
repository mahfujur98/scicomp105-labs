#!/usr/bin/env python3
# circle_area_instructor.py

import numpy as np


def f(x):
    # This is the function we are numerically integrating
    return 4 * np.sqrt(1 - x ** 2)


def F(x):
    # This is the exact analytic integral of our function
    return 2 * (x * np.sqrt(1 - x ** 2) + np.arcsin(x))


def left_hand_rule(f, a, b, intervals):
    dx = (b - a) / intervals
    area = 0
    for i in range(0, intervals):
        area += f(a + i * dx)
    return dx * area


def simpsons_rule(f, a, b, intervals):
    dx = (b - a) / intervals
    area = f(a) + f(b)
    for i in range(1, intervals):
        area += f(a + i * dx) * (2 * (i % 2 + 1))
    return dx / 3 * area


def main():
    a, b = 0.0, 1.0

    intervals = int(1e6)

    print("Integrating "
          "4 * sqrt(1 - x^2)")
    print(f" over [{a}, {b}] using {intervals:,} intervals\n")

    area_actual = F(b) - F(a)
    print(f"Analytic (Exact) : {area_actual:.14f}\n")

    area_left_hand = left_hand_rule(f, a, b, intervals)
    print(f"Left-hand Rule   : {area_left_hand:.14f}")
    print(f"% Abs Error      : "
          f"{abs((area_left_hand - area_actual) / area_actual * 100):.14f}\n")

    area_simpsons = simpsons_rule(f, a, b, intervals)
    print(f"Simpson's Rule   : {area_simpsons:.14f}")
    print(f"% Abs Error      : "
          f"{abs((area_simpsons - area_actual) / area_actual * 100):.14f}")


if __name__ == "__main__":
    main()
