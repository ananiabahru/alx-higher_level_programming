#!/usr/bin/python3
# 3-square.py by Anania baharu
""" defines a 3square """

class square:
    """A class that represents a square"""

def __int__(self, size=0):
    """Initializing this 3square class
    Args:
        size (int): The size of the new square.
    """
    
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    self.__size = size

def area(self):
    """
    Calculate area of the square
    Returns: The square of the size
    """

    return (self.__size ** 2)
