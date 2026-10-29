from copy import deepcopy
from typing import Optional
from src.types import Matrix, Color


class MatrixObject:
    """
    represents a 2D matrix of colors (RGB tuples),
    provides methods to manipulate and to convert it
    to and from binary data to use in bitmaps
    """

    @staticmethod
    def from_bytes(w: int, h: int, padding: int, data: bytes) -> MatrixObject:
        """
        creates MatrixObject from the raw binary bitmap data

        :param w: image width
        :param h: image height
        :param padding: image data padding, calculated in BitmapMeta's constructor
        :param data: image bytes of file (normally, offset is 54 bytes)
        """
        matrix: Matrix = []
        offset: int = w * 3 + padding
        for row in range(h):
            row_entries: list[Optional[Color]] = []
            for col in range(w):
                rgb: Color = tuple(value for value in data[row * offset : row * offset + 3])
                row_entries.append(rgb)
            matrix.append(row_entries)
        return MatrixObject(w, h, matrix)


    def __init__(self, w: int, h: int, data: Optional[Matrix] = None) -> None:
        """
        :param w: matrix width
        :param h: matrix height
        :param data: optional existing matrix data
        """
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
        paints the matrix on top of the current one, where there's a color

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
    

    def to_bytes(self, padding: int) -> bytes:
        """
        converts MatrixObject matrix to bitmap image data structure
        """
        data: bytes = b''
        for row in self.data:
            string: bytes = b''.join(bytes(color) for color in row) + b'\x00' * padding
            data = string + data
        return bytes(data)
