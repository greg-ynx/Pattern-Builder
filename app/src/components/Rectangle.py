class Rectangle:

    def __init__(self, width: float, height: float, filled: bool = False, color: str = None, filled_color: str = None):
        """
        Rectangle instance initialization.

        :param width: width of the rectangle
        :param height: height of the rectangle
        :param filled: is the rectangle is filled or not with color
        :param color: color of the rectangle
        :param filled_color: inner color of the rectangle
        """
        self.__width: int = int(width)
        self.__height: int = int(height)
        self.__filled: bool = filled
        self.__color: str = color

    def get_width(self) -> int:
        """
        Returns the rectangle's width.

        :return: width of the rectangle instance
        """
        return self.__width

    def set_width(self, width: float):
        """
        Set the rectangle width.

        :param width: new width value
        """
        self.__width = width

    def get_height(self) -> int:
        """
        Returns the rectangle's height.

        :return: height of the rectangle instance
        """
        return self.__height

    def set_height(self, height: float):
        """
        Set the rectangle height.

        :param height: new height value
        """
        self.__height = height

    def is_filled(self) -> bool:
        """
        Check if the rectangle is filled or not.

        :return: filled boolean state of the rectangle

        """
        return self.__filled

    def set_filled(self, filled: bool):
        """
        Set the rectangle filled state.

        :param filled: new filled boolean state
        """
        self.__filled = filled
