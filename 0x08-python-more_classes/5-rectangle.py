#!/usr/bin/python3

#!/usr/bin/python3
"""
Module 4-rectangle
Defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle by:
      - Private instance attributes `width` and `height`
      - Instantiation with optional `width` and `height`
      - Public instance method `area`
      - Public instance method `perimeter`
      - Print the rectangle with the `#` character using `str()`
      - Print the message "Bye rectangle..." when an instance of Rectangle is deleted
    """

    def __init__(self, width=0, height=0):
        """Initialize the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """Return the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print the message 'Bye rectangle...' when an instance of Rectangle is deleted"""
        print("Bye rectangle...")


