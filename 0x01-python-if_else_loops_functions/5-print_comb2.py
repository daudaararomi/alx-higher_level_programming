#!/usr/bin/python3
# A program that prints numbers from 0 to 99.
for n in range(0, 100):
    if n <= 98:
        print("{:02d}".format(n), end=', ')
    else:
        print("{}".format(n))
