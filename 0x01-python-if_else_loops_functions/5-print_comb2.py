#!/usr/bin/python3
for sepnum_by_coma in range(0, 100):
    if sepnum_by_coma == 99:
        print("{}".format(sepnum_by_coma))
    else:
        print("{:02}".format(sepnum_by_coma), end=", ")
