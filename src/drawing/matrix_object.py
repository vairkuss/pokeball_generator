from copy import deepcopy
from typing import Optional
from ..types import Matrix, Color


class MatrixObject:

    @staticmethod
    def from_bitmap(w: int, h: int, padding: int, data: bytes) -> MatrixObject:
        """
        this is a static method to create MatrixObject
        from the raw binary bitmap data

        :param w: image width
        :param h: image height
        :param padding: immage data padding, calculated in BitmapMeta's constructor
        :param data: image bytes of file (normally, offset is 54 bytes)
        """
        matrix: Matrix = []
        column_index: function = lambda row: data[len(data - padding) // height // 3
        for row in range(h):
            row_entries: list[Color] = []
            for col in data[]:
                row_entries.append()
            matrix.append(row_entries)
        return MatrixObject(w, h)


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
