#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    val = tuple_a + (0, 0)
    val2 = tuple_b + (0, 0)
    add1 = val[0] + val2[0]
    add2 = val[1] + val2[1]
    return (add1, add2)
