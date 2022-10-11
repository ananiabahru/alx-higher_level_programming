#!/usr/bin/python3
# 2-square.py by Anania baharu
"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a 2Square.
        Args:
            size (int): The size of the 2square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
