from .matrix_object import MatrixObject
from ..my_types import Color


class Circle(MatrixObject):

    def __init__(self, r, color: Color) -> None:
        super().__init__(r * 2, r * 2)
        for row in range(r * 2):
            for col in range(r * 2):
                self.__matrix.data[row][col] = color