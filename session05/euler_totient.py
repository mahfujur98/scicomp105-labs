#!/usr/bin/env python3
# euler_totient.py

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def totient(n):
    sum = 1
    # TODO: Implement Euler's totient function here
    return sum


def main():
    for n in range(2, 101):
        if n == totient(n) + 1:
            print(n, end=' ')


if __name__ == "__main__":
    main()
