from typing import Optional
from ..types import Options


class BitmapMeta:
    """
    This class generates an object for BitmapObject to use
    as a buffer with the metadata needed
    """

    def __init__(self, options: Options, file: Optional[bytes] = None) -> None:
        """
        reads existing metadata or generates new

        :param file: optinally provided file's data
        :param options: the options for the bitmap
        """
        if file is not None:
            self.size: int = int.from_bytes(file[2:6], "little")
            self.w: int = int.from_bytes(file[18:22], "little")
            self.h: int = int.from_bytes(file[22:26], "little")
            self.data: bytes = file[:54]
        else:
            self.w: int = options["w"]
            self.h: int = options["h"]
        
        self.padding: int = (4 - ((self.w * 3) % 4)) % 4

        if file is None:
            self.size: int = (self.w + self.padding) * self.h
            self.data: bytes = self.__to_bytes()



    def __to_bytes(self) -> bytes:
        """
        :returns: current bitmap's header and info blocks in bytes
        """
        
        raw_data: bytearray = bytearray(b'BM') # bfType
        raw_data.append((self.size + 54).to_bytes(4, "little")) # bfSize
        raw_data.append(b'\x00\x00\x00\x00') # bfReserved
        raw_data.append(b'\x36\x00\x00\x00') # bfOffBits
        
        raw_data.append(b'\x28\x00\x00\x00') # biSize
        raw_data.append(self.w.to_bytes(4, "little")) # biWidth
        raw_data.append(self.h.to_bytes(4, "little")) # biHeight
        raw_data.append(b'\x01\x00') # biPlanes
        raw_data.append(b'\x18\x00') # biBitCount
        raw_data.append(b'\x00\x00\x00\x00') # biCompression
        raw_data.append(self.size.to_bytes(4, "little")) #biSizeImage
        raw_data.append(b'\x00\x00\x00\x00') # biXPelsPerMeter
        raw_data.append(b'\x00\x00\x00\x00') # biYPelsPerMeter
        raw_data.append(b'\x00\x00\x00\x00') # biClrUsed
        raw_data.append(b'\x00\x00\x00\x00') # biClrImportant

        return bytes(raw_data)
