#!/usr/bin/python3

"""Writing class Square that defines a square"""


class Square:
"""Writing class Square that defines a square.No content"""


    def __init__(self, size=0):
        """defining fitst square.

        Args:
            size (int): 
        """
        if not isinstance(size, int):
            raise TypeError("size must be a number int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
