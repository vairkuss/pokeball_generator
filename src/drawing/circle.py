from .matrix_object import MatrixObject
from ..types.color import Color


class Circle(MatrixObject):

    def __init__(self, r, color: Color) -> None:
        super().__init__(r * 2, r * 2)
        for x in range(r * 2):
            for y in range(r * 2):
                c = sum(map(lambda v: (v + r) ** 2, [x, y]))
                if c < r:
                     self.__matrix.data[row][col] = color