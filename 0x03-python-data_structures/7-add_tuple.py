#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a or tuple_b is smaller than 2, fill the missing values with 0
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Take only the first two elements from each tuple and add them
    result = (a[0] + b[0], a[1] + b[1])
    
    return result
