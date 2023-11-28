#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    la_digit = number % 10
else:
    la_digit = number % -10

if la_digit > 5:
    print(f"Last digit of {number} is {la_digit} and is greater than 5")
elif la_digit == 0:
    print(f"Last digit of {number} is {la_digit} and is 0")
elif la_digit < 6 and la_digit != 0:
    print(f"Last digit of {number} is {la_digit} and is less than 6 and not 0")
