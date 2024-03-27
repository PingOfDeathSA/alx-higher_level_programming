#!/usr/bin/python3

def magic_calculation(a, b):
  
    from magic_calculation_102 import add, sub

    if a < b:
        charec = add(a, b)
        for index in range(4, 6):
            charec = add(charec, index)
        return charec

    else:
        return sub(a, b)
