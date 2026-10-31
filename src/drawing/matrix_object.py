from copy import deepcopy
from typing import Optional
from src.types import Matrix, Color


class MatrixObject:
    """
    creates a matrix of rgb tuples, converts it
    to and from binary data for the bitmaps
    """

    @staticmethod
    def from_bytes(w: int, h: int, padding: int, data: bytes) -> MatrixObject:
        """
        creates new MatrixObject from the raw binary bitmap data

        :param w: image width
        :param h: image height
        :param padding: image data padding, calculated in BitmapMeta's constructor
        :param data: image data in raw bytes
        """
        matrix: Matrix = []
        row_length: int = w * 3 + padding
        for row in range(h):
            row_entries: list[Optional[Color]] = []
            for col in range(w):
                offset: int = row * row_length + col * 3
                r, g, b = data[offset : offset + 3]
                color: Color = (r, g, b)
                row_entries.append(color)
            matrix.append(row_entries)
        return MatrixObject(w, h, matrix)


    def __init__(self, w: int, h: int, matrix: Optional[Matrix] = None) -> None:
        """
        saves provided matrix in own attributes or generates new, filled with None

        :param w: matrix width
        :param h: matrix height
        :param data: optional existing matrix data
        """
        self.data: Matrix = matrix if matrix is not None else [[None for _ in range(w)] * h]


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
            string: bytes = b''.join(b'\x00' * 3 if color is None else bytes(color) for color in row)
            data = string + b'\x00' * padding + data
        return bytes(data)
