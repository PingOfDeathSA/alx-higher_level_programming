#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    numcount = len(sys.argv) - 1
    if numcount == 0:
        print("0 arguments.")
    elif numcount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numcount))
    for index in range(numcount):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
