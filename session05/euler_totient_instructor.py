#!/usr/bin/env python3
# euler_totient_instructor.py

from sympy.ntheory.factor_ import totient


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def totient_student(n):
    sum = 1
    # TODO: Implement Euler's totient function here
    for i in range(2, n):
        if gcd(i, n) == 1:
            sum += 1
    return sum


def main():
    for n in range(2, 101):
        if n == totient(n) + 1:
            print(n, end=' ')


if __name__ == "__main__":
    main()
