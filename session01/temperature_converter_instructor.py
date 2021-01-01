#!/usr/bin/env python3
# temperature_converter_instructor.py

'''
for loop
range (start, stop, step)
scopes (indentation) and colon
'''
# for fahrenheit in range(-44, 216, 4):
#    celsius = (fahrenheit - 32) * 5 / 9
#    print(f"{fahrenheit} = {celsius}")

'''
Exclusive stop in range(), switch to 217
f-string formatting - colon: and then .3f
'''
# for fahrenheit in range(-44, 217, 4):
#    celsius = (fahrenheit - 32) * 5 / 9
#    print(f"{fahrenheit:.3f} F = {celsius:.3f} C")

'''
f-string formatting - >n for right justified, <n for left, ^for center
'''
for fahrenheit in range(-44, 217, 4):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:>6.2f} F = {celsius:>6.2f} C")
