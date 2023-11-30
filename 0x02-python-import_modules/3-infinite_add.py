#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    ad = 0
    for i in range(1, len(argv)):
        ad += int(argv[i])
    print(f"{ad}")
