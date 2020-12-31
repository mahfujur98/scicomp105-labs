#!/usr/bin/env python3
# newton_sqrt.py

x = 168923

lowEnd = 0
highEnd = x

estimate = (highEnd + lowEnd) / 2
estimateSquared = estimate * estimate

epsilon = 1e-14

while abs(estimateSquared - x) > epsilon:
    if estimateSquared > x:
        highEnd = estimate
    else:
        lowEnd = estimate

    estimate = (highEnd + lowEnd) / 2
    estimateSquared = estimate * estimate

    if highEnd == lowEnd:
        break

print(f"Estimated square root of \n {x:,}")
print(f"is \n {estimate:.14f}")
