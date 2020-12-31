#!/usr/bin/env python3
# matrix_multiple.py

import numpy as np


def main():
    a = np.array([[4, 5, 8], [1, 9, 7]])
    b = np.array([[2, 4], [6, 1], [5, 9]])

    print(a)
    print(b)
    print(np.dot(a, b))


if __name__ == "__main__":
    main()
