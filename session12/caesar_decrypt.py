#!/usr/bin/env python3
# caesar_decrypt.py

import os
import sys


def main(file_name, key_shift):
    with open(file_name, "rb") as f_in:
        f_bytes = bytearray(f_in.read())

        for i in range(0, len(f_bytes)):
            f_bytes[i] = (f_bytes[i] + key_shift) % 256

        print(f_bytes.decode())


if __name__ == "__main__":
    file_name = None
    if len(sys.argv) == 1:
        file_name = os.path.dirname(sys.argv[0]) + "/ciphertext1.txt"
        # TODO: Fix this next line of code
        key_shift = 0
    else:
        file_name = sys.argv[1]
        key_shift = int(sys.argv[2])
    main(file_name, key_shift)
