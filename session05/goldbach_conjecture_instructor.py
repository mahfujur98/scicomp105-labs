#!/usr/bin/env python3
# goldbach_conjecture_instructor.py

import numpy as np
from sympy import prime
from itertools import combinations_with_replacement


def main():
    last_even_num = 458
    num_odd_primes = 54

    print(f"Verifying Goldbach's conjecture "
          f"for range (6, {last_even_num}) "
          f"using first {num_odd_primes} odd primes . . .")

    # Comprehension to generate list of first odd primes
    primes = [prime(n) for n in range(2, num_odd_primes + 2)]

    # Generate all pairs of primes (with repetition)
    n = [*combinations_with_replacement(primes, 2)]

    # Create sorted list containing sum each pair of odd primes
    goldbach = np.sort([sum(pair) for pair in n])

    # Determine which even numbers > 4 are in the list of summed primes
    gaps = np.setdiff1d(range(6, last_even_num + 2, 2), goldbach)

    print(f"Goldbach violations at {gaps}")


if __name__ == "__main__":
    main()
