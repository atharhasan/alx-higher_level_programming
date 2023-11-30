#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    arg = len(sys.argv)
    if arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    ober = sys.argv[2]
    b = int(sys.argv[3])
    if ober == "+":
        print("{} {} {} = {}".format(a, ober, b, a + b))
    elif ober == "-":
        print("{} {} {} = {}".format(a, ober, b, a - b))
    elif ober == "*":
        print("{} {} {} = {}".format(a, ober, b, a * b))
    elif ober == "/":
        print("{} {} {} = {}".format(a, ober, b, a / b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
