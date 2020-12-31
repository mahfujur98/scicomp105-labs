#!/usr/bin/env python3
# pells_equation.py


import math
from numba import jit


@jit(nopython=True)
def pell_solution(n):
    x = 1
    while x < 70_000:
        x2 = int(x * x)
        y = 1
        y_max = math.sqrt(x2 / n)
        while y <= y_max:
            y2 = int(y * y)
            if x2 - n * y2 == 1:
                return x, y
            y += 1
        x += 1
    return None, None


def main():
    # Print column headers
    print("Solutions to Pell's Equation")
    print(f"{'n':>4}{'x':>8}{'y':>8}")
    print(f"{'='*3:>4}{'='*6:>8}{'='*6:>8}")

    for n in range(2, 71):
        print(f"{n:>4}", end='')
        x, y = pell_solution(n)
        if not x == None:
            print(f"{x:>8}{y:>8}")
        else:
            print(f"{'-':>8}{'-':>8}")


if __name__ == "__main__":
    main()
