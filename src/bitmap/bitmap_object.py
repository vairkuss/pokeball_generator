from src import MatrixObject, Options


class BitmapObject:
    """
    represents a bitmap object to manipulate its data
    """

    def __init__(self, options: Options) -> None:
        """
        reads from provided data or generates new from options

        :param options: the options for the bitmap
        :param data: optinally provided raw binary data from the bitmap file
        """
        image_offset: int = 54
        self.__w: int = options.w
        self.__h: int = options.h
        self.__padding: int = (4 - ((self.__w * 3) % 4)) % 4
        self.__matrix: MatrixObject = MatrixObject(self.__w, self.__h)
        #TODO: umlcd & save previous header


    @property
    def data(self) -> bytes:
        """
        :returns: bitmap data assembled in raw bytes
        """
        return self.__convert_meta() + self.__matrix.to_bytes(self.__padding)


    def write(self, data: bytes, x: int = 0, y: int = 0) -> None:
        """
        parses MatrixObject from the given bytes and overwrites
        own matrix with its data using MatrixObject.paint() method

        :param data: bytes to parse
        :param x: x-coordinate of the top-left corner of the area to overwrite
        :param y: y-coordinate of the top-left corner of the area to overwrite
        """
        parsed_matrix: MatrixObject = MatrixObject.from_bytes(self.__w, self.__h, self.__padding, data)
        self.__matrix.paint(parsed_matrix.data, x, y)


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
