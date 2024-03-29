#!/usr/bin/python3
"""
Module 7-rectangle
Defines a Rectangle class
Private instance attributes: width and height
"""


class Rectangle:
    """ Defines a rectangle class """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of Rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Prints a message when an instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ Gets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Gets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """ Prints a string representation of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """ Returns a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

