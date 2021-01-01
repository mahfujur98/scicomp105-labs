#!/usr/bin/env python3
# perfect_numbers_instructor.py

for n in range(2, 10000):
    sum_of_factors = 1
    for factor in range(2, n):
        if n % factor == 0:
            sum_of_factors += factor
    if sum_of_factors == n:
        print(f"{n:,} is a perfect number")
