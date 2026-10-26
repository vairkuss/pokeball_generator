from copy import deepcopy
from ..my_types import Optional, Matrix


class MatrixObject:

    def __init__(self, w, h, data: Optional[Matrix] = None) -> None:
        h = w if h is None else h
        self.data: Matrix = data if data is not None else [[[None] * w] * h]

    def paint(self, matrix: Matrix, x=0, y=0) -> MatrixObject:
        clone = deepcopy(self)
        for i, row in enumerate(matrix):
            clone.data[i + y][x: x + len(row)] = row
        return clone

    def shadow(self, matrix: Matrix, x=0, y=0) -> MatrixObject:
        clone = deepcopy(self)
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if clone.data[i + y][j + x] is not None:
                    clone.data[i + y][j + x] = row[j]
        return clone
