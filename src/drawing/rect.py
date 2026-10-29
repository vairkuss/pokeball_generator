from src import MatrixObject
from src.types import Color


class Rect(MatrixObject):
    """
    represents a 2D matrix of colors (RGB tuples) in the shape of a rectangle,
    provides methods to manipulate and to convert it
    to and from binary data to use in bitmaps
    """

    def __init__(self, w: int, h: int, color: Color) -> None:
        super().__init__(w, h)
        for row in range(h):
            for col in range(w):
                self.data[row][col] = color
