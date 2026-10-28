from .matrix_object import MatrixObject
from ..types.color import Color


class Circle(MatrixObject):
    """
    a class that represents a 2D matrix of colors (RGB tuples) in the shape of a circle,
    it provides methods to manipulate and to convert it to and from binary data to use in bitmaps
    """

    def __init__(self, r, color: Color) -> None:
        d = r * 2
        super().__init__(d, d)
        for y in range(d):
            for x in range(d):
                c = x ** 2 + y ** 2
                if c < r:
                    self.data[y][x] = color
