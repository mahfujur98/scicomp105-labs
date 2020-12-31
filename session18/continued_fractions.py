#!/usr/bin/env python3
# continued_fractions.py

import math

MAX_TERMS = 20


def normalize_cf(cf):
    if len(cf) > 2:
        if cf[-1] == 1 and cf[-2] != 1:
            cf[-2] += 1
            cf.pop(-1)
    return cf


def encode_cf(x):
    cf = []
    while len(cf) < MAX_TERMS:
        cf.append(math.floor(x))
        x = x - math.floor(x)
        if x < 1e-11:
            break
        x = 1 / x
    return normalize_cf(cf)


def decode_cf(cf):
    hn, kn = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    for term in cf:
        an, bn = term, 1
        hn = an * h_1 + b_1 * h_2
        kn = an * k_1 + b_1 * k_2
        b_1 = bn
        h_1, h_2 = hn, h_1
        k_1, k_2 = kn, k_1
    return hn / kn


def decode_gencf(a0, b0, Ai, Bi, Ci, Di, Ei):
    an, bn = a0, b0
    hn, kn = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    for n in range(1, MAX_TERMS):
        hn = an * h_1 + b_1 * h_2
        kn = an * k_1 + b_1 * k_2
        b_1 = bn
        h_1, h_2 = hn, h_1
        k_1, k_2 = kn, k_1
        an = Di * n + Ei
        bn = Ai * n * n + Bi * n + Ci
    return hn / kn


def pi_gencf():
    x = decode_gencf(3, 1, 4, 4, 1, 0, 6)
    print(f"Euler's Generalized Continued Fraction")
    print(f"Est. Pi     : {x}")
    print(f"Act. Pi     : {math.pi}")
    print(f"Abs. % Err  : {abs((math.pi - x)/math.pi):.14%}\n")

    x = decode_gencf(3, 1, 8, 0, -7, 8, -1)
    print(f"Biersach's Generalized Continued Fraction #1")
    print(f"Est. Pi     : {x}")
    print(f"Act. Pi     : {math.pi}")
    print(f"Abs. % Err  : {abs((math.pi - x)/math.pi):.14%}\n")

    x = decode_gencf(2, 8, 4, 8, 0, 4, 2)
    print("Biersach's Generalized Continued Fraction #2")
    print(f"Est. Pi     : {x}")
    print(f"Act. Pi     : {math.pi}")
    print(f"Abs. % Err  : {abs((math.pi - x)/math.pi):.14%}\n")

    print()


def main():
    x = 3.245
    #x = 0.825
    #x = math.sqrt(2)
    #x = math.sqrt(13)
    #x = (1 + math.sqrt(5)) / 2

    cf = encode_cf(x)

    print(f"\nThe continued fraction"
          f":\n{cf}\nencodes the value: {x}\n")

    x = decode_cf(cf)

    print(f"\nThe continued fraction"
          f":\n{cf}\ndecodes the value: {x}\n")

    # pi_gencf()


if __name__ == "__main__":
    main()
