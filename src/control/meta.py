from typing import Optional


class Meta:
    """
    stores the metadata of the bitmap file
    """

    def __init__(self, data: Optional[bytes]) -> None:
        """
        parses the metadata from the given bitmap data or sets the defaults

        :param data: the raw bytes of the bitmap file
        """
        if data is None:
            self.image_offset: int = 54
            self.w: int = 100
            self.h: int = 100
            self.__template: bytearray = bytearray(b'BM' + b'\x00' * 52)
            self.__template[10:14] = self.image_offset.to_bytes(4, "little")
            self.__template[14:18] = (self.image_offset - 14).to_bytes(4, "little")
            self.__template[26:28] = b'\x01\x00'
            self.__template[28:30] = b'\x18\x00'
        else:
            self.image_offset: int = int.from_bytes(data[10:14], byteorder="little")
            self.w: int = int.from_bytes(data[18:22], byteorder="little")
            self.h: int = int.from_bytes(data[22:26], byteorder="little")
            self.__template: bytearray = bytearray(data[:self.image_offset])


    def to_bytearray(self) -> bytearray:
        """
        :returns: the raw bytes of the bitmap meta block
        """
        meta: bytearray = self.__template
        meta[10:14] = self.image_offset.to_bytes(4, "little")
        meta[18:22] = self.w.to_bytes(4, "little")
        meta[22:26] = self.h.to_bytes(4, "little")
        return meta
