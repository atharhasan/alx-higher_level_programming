#!/usr/bin/python3
def print_last_digit(number):
    la_digit = abs(number) % 10
    print(la_digit, end='')
    return la_digit
