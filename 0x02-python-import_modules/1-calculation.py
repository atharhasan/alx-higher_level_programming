#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as ee
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, ee.add(a, b)))
    print("{} - {} = {}".format(a, b, ee.sub(a, b)))
    print("{} * {} = {}".format(a, b, ee.mul(a, b)))
    print("{} / {} = {}".format(a, b, ee.div(a, b)))
