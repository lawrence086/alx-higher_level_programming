#!/usr/bin/python3
"""Class Rectangle inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner of
            the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner
            of the rectangle. Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the top-left corner of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The x-coordinate of the top-left corner
            of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The y-coordinate of the top-left corner
            of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print rectangle instance using # character"""
        for line in range(self.__y):
            print()
        for i in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str method to return rectangle representation"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height)

        def update(self, *args, **kwargs):
            """assigns an argument to each list"""
        if (args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["width"] = self.width
        my_dict["height"] = self.height
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
