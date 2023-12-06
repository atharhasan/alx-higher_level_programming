#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = set()
    sum = 0
    for i in my_list:
        if i not in n:
            n.add(i)
            sum += i
    return sum
