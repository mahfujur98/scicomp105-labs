#!/usr/bin/env python3
# bigram_decrypt.py

import os
import sys


def main():
    in_file = os.path.dirname(sys.argv[0]) + "/bigram_ciphertext.txt"
    key_shift = 128
    out_file = os.path.dirname(sys.argv[0]) + "/bigram_plaintext.txt"

    with open(in_file, "rb") as f_in:
        f_bytes = bytearray(f_in.read())

        for i in range(0, len(f_bytes)):
            f_bytes[i] = f_bytes[i] ^ key_shift

        with open(out_file, "wb") as f_out:
            f_out.write(f_bytes)


if __name__ == "__main__":
    main()
