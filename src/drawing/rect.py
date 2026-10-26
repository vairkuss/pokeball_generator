from .matrix_object import MatrixObject
from ..types.color import Color


class Rect(MatrixObject):

    def __init__(self, w, h, color: Color) -> None:
        super().__init__(w, h)
        for row in range(h):
            for col in range(w):
                self.data[row][col] = color
