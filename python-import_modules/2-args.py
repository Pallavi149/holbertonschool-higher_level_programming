#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if n == 2:
        print("{} argument:".format(n - 1))
        print("{}: {}".format(1, sys.argv[1]), end="")
        print()
    elif n > 2:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments.".format(n - 1))
