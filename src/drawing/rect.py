from src import MatrixObject
from src.types import Color


class Rect(MatrixObject):
    """
    creates a matrix filled with the rgb tuples of chosen color
    """

    def __init__(self, w: int, h: int, color: Color) -> None:
        """
        :param w: width of the rectangle
        :param h: height of the rectangle
        :param color: color of the rectangle
        """
        super().__init__(w, h)
        for row in range(h):
            for col in range(w):
                self.data[row][col] = color
