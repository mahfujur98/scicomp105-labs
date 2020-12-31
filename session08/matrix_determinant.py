#!/usr/bin/env python3
# matrix_determinant.py

import numpy as np


def main():
    np.random.seed(2016)
    a = np.random.randint(-10, 11, (10, 10))

    print(a)
    print(np.linalg.det(a))


if __name__ == "__main__":
    main()
