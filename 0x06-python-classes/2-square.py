e#!/usr/bin/python3

"""Writing class Square that defines a square"""


class Square:
"""Writing class Square that defines a square.No content"""

    def __init__(self, size=0):
            """initialize square
            Args:
                size (int): size of the square
            """
            if type(size) is not int:
                raise TypeError('size must be an integer')
            elif size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
