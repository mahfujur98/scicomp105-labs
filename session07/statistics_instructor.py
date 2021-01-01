#!/usr/bin/env python3
# statistics_instructor.py

import numpy as np
import statistics


def main():
    np.random.seed(2021)
    samples = np.random.randint(0, 100, 30)
    print(f"Samples      = {samples.tolist()}")
    print(f"Mean         = {np.mean(samples):.4f}")
    print(f"Median       = {np.median(samples):.4f}")
    print(f"Mode         = {statistics.mode(samples)}")
    print(f"Pop Variance = {np.var(samples):.4f}")
    print(f"Pop Std. Dev = {np.std(samples):.4f}")


if __name__ == "__main__":
    main()
