from ..control import Options
from ..matrix import MatrixObject
from ..types import Matrix


class BitmapObject:
    """
    represents a bitmap object to manipulate its data
    """

    def __init__(self, options: Options) -> None:
        """
        generates new BitmapObject from options

        :param options: the options for the bitmap
        """
        self.__w: int = options.meta.w
        self.__h: int = options.meta.h
        self.__padding: int = (4 - ((self.__w * 3) % 4)) % 4
        self.__matrix: MatrixObject = MatrixObject(self.__w, self.__h)
        self.__template: bytearray = options.meta.to_bytearray()


    def write(self, matrix: Matrix, x: int = 0, y: int = 0) -> None:
        """
        overwrites own matrix with the new data
        using MatrixObject.paint() method

        :param matrix: the matrix data to overwrite with
        :param x: x-coordinate of the top-left corner of the area to overwrite
        :param y: y-coordinate of the top-left corner of the area to overwrite
        """
        self.__matrix = self.__matrix.paint(matrix, x, y)


    @property
    def data(self) -> bytes:
        """
        :returns: bitmap data assembled in raw bytes
        """
        data: bytearray = self.__template + self.__matrix.to_bytes(self.__padding)
        data[2:6] = len(data).to_bytes(4, "little")
        return bytes(data) 
