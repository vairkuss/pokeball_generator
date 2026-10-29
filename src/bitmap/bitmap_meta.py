from typing import Optional
from src.types import Options


class BitmapMeta:
    """
    generates an object for BitmapObject to store the essential metadata
    """

    def __init__(self, options: Options, data: Optional[bytes] = None) -> None:
        """
        reads existing metadata or generates new from provided options

        :param data: optinally provided bitmap header and info data (first 54 bytes of the bitmap file)
        :param options: the options for the bitmap
        """
        if data is not None:
            self.size: int = int.from_bytes(data[2:6], "little")
            self.w: int = int.from_bytes(data[18:22], "little")
            self.h: int = int.from_bytes(data[22:26], "little")
            self.data: bytes = data[:54]
        else:
            self.w: int = options["w"]
            self.h: int = options["h"]
        
        self.padding: int = (4 - ((self.w * 3) % 4)) % 4

        if data is None:
            self.size: int = (self.w + self.padding) * self.h
            self.data: bytes = self.__to_bytes()



    def __to_bytes(self) -> bytes:
        """
        :returns: current bitmap's raw header and info blocks
        """
        raw_data: bytes = b'BM' # bfType
        raw_data += (54 + self.size).to_bytes(4, "little") # bfSize
        raw_data += b'\x00\x00\x00\x00' # bfReserved
        raw_data += b'\x36\x00\x00\x00' # bfOffBits
        
        raw_data += b'\x28\x00\x00\x00' # biSize
        raw_data += self.w.to_bytes(4, "little") # biWidth
        raw_data += self.h.to_bytes(4, "little") # biHeight
        raw_data += b'\x01\x00' # biPlanes
        raw_data += b'\x18\x00' # biBitCount
        raw_data += b'\x00\x00\x00\x00' # biCompression
        raw_data += self.size.to_bytes(4, "little") #biSizeImage
        raw_data += b'\x00\x00\x00\x00' # biXPelsPerMeter
        raw_data += b'\x00\x00\x00\x00' # biYPelsPerMeter
        raw_data += b'\x00\x00\x00\x00' # biClrUsed
        raw_data += b'\x00\x00\x00\x00' # biClrImportant

        return raw_data
