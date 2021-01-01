#!/usr/bin/env python3
# adaptive_quadrature_instructor.py

import time


def f(x):
    # This is the function we are numerically integrating
    return 5 * pow(x, 3) - 9 * pow(x, 2) + 11


def F(x):
    # This is the exact analytic integral of our function
    return 5 * pow(x, 4) / 4 - 3 * pow(x, 3) + 11 * x


def midpoint_fixed(a, b):
    x = a
    dx = (b - a) / 1e6
    area = 0
    while x < b:
        # TODO: Use the midpoint rule
        area += f(x + dx / 2) * dx
        x += dx
    return area


def midpoint_adaptive(a, b):
    x = a
    dx = 1
    area = 0
    while x < b:
        f1 = f(x)
        f2 = f(x + dx)
        # TODO: Insert your code here
        while abs((f2 - f1) / f1) > 1e-3:
            # Keep halving dx if current delta is too great
            dx /= 2
            f2 = f(x + dx)
        # Use the midpoint rule
        area += f(x + dx / 2) * dx
        x += dx
        # Expand current interval width
        dx *= 2
    return area


def main():
    a = 0
    b = 10

    area_actual = F(b) - F(a)
    print(f"\nIntegral using analytic calculus = {area_actual}\n")

    start_time = time.process_time()
    area_fixed = midpoint_fixed(a, b)
    elapsed_time = time.process_time() - start_time
    err = abs((area_actual - area_fixed) / area_actual) * 100
    print(f"Integral using fixed width midpoint rule = {area_fixed}")
    print(f"Fixed width midpoint rule error = {err:.8f}")
    print(f"Time (sec) Fixed = {elapsed_time:.3f}\n")

    start_time = time.process_time()
    area_adaptive = midpoint_adaptive(a, b)
    elapsed_time = time.process_time() - start_time
    err = abs((area_actual - area_adaptive) / area_actual) * 100
    print(f"Integral using adaptive width midpoint rule = {area_adaptive}")
    print(f"Adaptive width midpoint rule error = {err:.8f}")
    print(f"Time (sec) Adaptive = {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
