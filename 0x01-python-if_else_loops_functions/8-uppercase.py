#!/usr/bin/python3
def uppercase(str):
    msg = ''
    for i in range(0, len(str)):
        ch = str[i]
        if 'a' <= ch <= 'z':
            msg += '{}'.format(chr(ord(ch) - 32))
        else:
            msg += ch
    print(msg)

