from typing import Optional
from src import MatrixObject
from src.types import Options


class BitmapObject:
    """
    generates an object for BitmapObject to store the essential metadata
    """

    def __init__(self, options: Options, data: Optional[bytes] = None) -> None:
        """
        reads existing metadata or generates new from provided options

        :param data: optinally provided bitmap binary data
        :param options: the options for the bitmap
        """
        if data is not None:
            self.w: int = int.from_bytes(data[18:22], "little")
            self.h: int = int.from_bytes(data[22:26], "little")
            self.data: bytes = data
        else:
            self.w: int = options["w"]
            self.h: int = options["h"]
        
        self.padding: int = (4 - ((self.w * 3) % 4)) % 4
        self.matrix: MatrixObject = MatrixObject.from_bytes(self.w, self.h, self.padding, data[54:])
        
        if data is None:
            self.data: bytes = self.__convert_meta() + self.matrix.to_bytes(self.padding)
        

    def __convert_meta(self) -> bytes:
        """
        :returns: combined header and info blocks in bytes
        """
        raw: bytes = b'BM' # bfType
        raw += len(self.data).to_bytes(4, "little") # bfSize
        raw += b'\x00\x00\x00\x00' # bfReserved
        raw += b'\x36\x00\x00\x00' # bfOffBits
        
        raw += b'\x28\x00\x00\x00' # biSize
        raw += self.w.to_bytes(4, "little") # biWidth
        raw += self.h.to_bytes(4, "little") # biHeight
        raw += b'\x01\x00' # biPlanes
        raw += b'\x18\x00' # biBitCount
        raw += b'\x00\x00\x00\x00' # biCompression
        raw += (len(self.data) - 54).to_bytes(4, "little") #biSizeImage
        raw += b'\x00\x00\x00\x00' # biXPelsPerMeter
        raw += b'\x00\x00\x00\x00' # biYPelsPerMeter
        raw += b'\x00\x00\x00\x00' # biClrUsed
        raw += b'\x00\x00\x00\x00' # biClrImportant

        return raw
