#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
L_digit = abs(number) % 10
if number < 0:
       L_ digit = -L_digit
print(" Last digit of {0} is {1}".format(number,  L_digit), end="")
if L_digit > 5:
    print(" and is greater than 5")
elif L_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
