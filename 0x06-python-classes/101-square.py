#!/usr/bin/python3

class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.
        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The size to set.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        Args:
            value (tuple): The position to set.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """Return string representation of the square."""
        if self.__size == 0:
            return ""
        lines = []
        for _ in range(self.__position[1]):
            lines.append("\n")
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "".join(lines)


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)

