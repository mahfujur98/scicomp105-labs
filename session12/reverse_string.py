#!/usr/bin/env python3
# reverse_string.py


def reverse_str(a):
    b = ""
    # TODO: Insert your code here
    return b


def reverse_str2(a):
    b = ""
    for i in reversed(range(len(a))):
        b += a[i]
    return b


def reverse_str3(a):
    b = ""
    for c in a:
        b = c + b
    return b


def main():
    s = "Forever Young"
    print(s)

    print(reverse_str(s))
    print(reverse_str2(s))
    print(reverse_str3(s))

    print("".join(reversed(s)))
    print(s[::-1])


if __name__ == "__main__":
    main()
