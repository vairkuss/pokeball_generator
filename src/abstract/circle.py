from .matrix_object import MatrixObject
from ..types import Color


class Circle(MatrixObject):
    """
    creates a matrix filled with the rgb tuples of chosen color,
    the filling is in the shape of a circle
    """

    def __init__(self, r: int, color: Color) -> None:
        """
        :param r: radius of the circle
        :param color: color of the circle
        """
        d = r * 2
        super().__init__(d, d)
        for y in range(d):
            for x in range(d):
                c = x ** 2 + y ** 2
                if c <= r:
                    self.data[y][x] = color
