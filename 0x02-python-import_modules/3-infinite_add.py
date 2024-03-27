#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    c = 0
    for index in range(len(sys.argv) - 1):
        startcount += int(sys.argv[index + 1])
    print("{}".format(startcount))
