from ..control import Options
from ..abstract import MatrixObject
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


    @property
    def data(self) -> bytes:
        """
        :returns: bitmap data assembled in raw bytes
        """
        data: bytearray = self.__template + self.__matrix.to_bytes(self.__padding)
        data[34:38] = (len(data) - 54).to_bytes(4, "little")
        return bytes(data) 


    def write(self, matrix: Matrix, x: int = 0, y: int = 0) -> None:
        """
        overwrites own matrix with the new data
        using MatrixObject.paint() method

        :param matrix: the matrix data to overwrite with
        :param x: x-coordinate of the top-left corner of the area to overwrite
        :param y: y-coordinate of the top-left corner of the area to overwrite
        """
        self.__matrix.paint(matrix, x, y)


    def __convert_meta(self) -> bytes:
        """
        :returns: header and info blocks assembled in raw bytes
        """
        raw: bytes = b'BM' # bfType
        raw += len(self.data).to_bytes(4, "little") # bfSize
        raw += b'\x00\x00\x00\x00' # bfReserved
        raw += b'\x36\x00\x00\x00' # bfOffBits
        
        raw += b'\x28\x00\x00\x00' # biSize
        raw += self.__w.to_bytes(4, "little") # biWidth
        raw += self.__h.to_bytes(4, "little") # biHeight
        raw += b'\x01\x00' # biPlanes
        raw += b'\x18\x00' # biBitCount
        raw += b'\x00\x00\x00\x00' # biCompression
        raw += (len(self.data) - 54).to_bytes(4, "little") #biSizeImage
        raw += b'\x00\x00\x00\x00' # biXPelsPerMeter
        raw += b'\x00\x00\x00\x00' # biYPelsPerMeter
        raw += b'\x00\x00\x00\x00' # biClrUsed
        raw += b'\x00\x00\x00\x00' # biClrImportant

        return raw
