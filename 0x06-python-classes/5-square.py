#!/usr/bin/python3

'''A module containing a `Square` klas'''


class Square:
    '''Square klas with a size private instance attribute'''

    def __init__(self, size=0) -> None:
        '''instantiates an square instace while validating the size input'''
        self.size = size

    @property
    def size(self):
        '''returns the size private attribute'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''calculates the area of a square

        Return:
            area (int): the area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        """prints a square of `size` size using the `#` character"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
