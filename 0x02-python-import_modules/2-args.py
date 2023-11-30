#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    arg = len(argv) - 1
    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("{} argument:".format(arg))
    else:
        print("{} arguments:".format(arg))
    for i in range(1, arg):
        print("{}: {}".format(i, arg[i]))
