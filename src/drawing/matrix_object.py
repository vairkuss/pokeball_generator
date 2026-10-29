from copy import deepcopy
from typing import Optional
from ..types import Matrix, Color


class MatrixObject:
    """
    A class that represents a 2D matrix of colors (RGB tuples),
    it provides methods to manipulate and to convert it to and
    from binary data to use in bitmaps
    """

    @staticmethod
    def from_bitmap(w: int, h: int, padding: int, data: bytes) -> MatrixObject:
        """
        creates MatrixObject from the raw binary bitmap data

        :param w: image width
        :param h: image height
        :param padding: image data padding, calculated in BitmapMeta's constructor
        :param data: image bytes of file (normally, offset is 54 bytes)
        """
        matrix: Matrix = []
        for row in range(h):
            row_entries: list[Color] = []
            for col in range(len(data) - padding):
                rgb = tuple(data[row * col * 3: row * col * 3 + 3])
                row_entries.append(rgb)
            matrix.append(row_entries)
        return MatrixObject(w, h, matrix)


    def __init__(self, w: int, h: int, data: Optional[Matrix] = None) -> None:
        h = w if h is None else h
        self.data: Matrix = data if data is not None else [[[None] * w] * h]


    def paint(self, matrix: Matrix, x: int = 0, y: int = 0) -> MatrixObject:
        """
        paints the matrix on top of the current one
        
        :param matrix: a matrix to paint on top of the current one
        :param x: x-coordinate of the top-left corner of the area to paint
        :param y: y-coordinate of the top-left corner of the area to paint
        :returns: a shallow copy of the current MatrixObject with the painted data
        """
        clone: MatrixObject = deepcopy(self)
        for i, row in enumerate(matrix):
            if i + y >= len(clone.data):
                break
            elif i + y < 0:
                continue
            for j in range(len(row)):
                if j + x >= len(clone.data[i + y]):
                    break
                elif j + x < 0:
                    continue
                clone.data[i + y][x + j] = row[j]
        return clone
    

    def shadow(self, matrix: Matrix, x: int = 0, y: int = 0) -> MatrixObject:
        """
        paints the matrix on top of the current one, but only where the current one is None

        :param matrix: a matrix to shadow on top of the current one
        :param x: x-coordinate of the top-left corner of the area to shadow
        :param y: y-coordinate of the top-left corner of the area to shadow
        :returns: a shallow copy of the current MatrixObject with the shadowed data
        """
        clone: MatrixObject = deepcopy(self)
        for i, row in enumerate(matrix):
            if i + y >= len(clone.data):
                break
            elif i + y < 0:
                continue
            for j in range(len(row)):
                if j + x >= len(clone.data[i + y]):
                    break
                elif j + x < 0:
                    continue
                if clone.data[i + y][j + x] is not None:
                    clone.data[i + y][j + x] = row[j]
        return clone
    

    @property
    def raw(self) -> bytes:
        """
        converts the matrix of MatrixObject to bytes, with padding
        """
        data: bytearray = bytearray()
        for row in self.data:
            for color in row:
                data.extend(color)
            padding = (4 - len(row) % 4) % 4
            data.extend(b'\x00' * padding)
        return bytes(data)
