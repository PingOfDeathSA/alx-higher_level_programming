#!/usr/bin/python3
start = 0
for lett in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(lett - start)), end="")
    start = 32 if start == 0 else 0
