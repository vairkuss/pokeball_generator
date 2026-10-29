from typing import Optional

from src.types import Options


class BitmapObject:
    """
    represents a bitmap image and provides methods to manipulate its pixel data
    """

    def __init__(self, options: Options, data: Optional[bytes]) -> None:
        """
        :param data: The raw bitmap data.
        :param options: The options for the bitmap.
        """
        self.meta: BitmapMeta = BitmapMeta(data=data[0:54], options=options)


    def to_bytes(self) -> bytes:
        """
        converts the BitmapObject to raw bytes

        :returns: raw bitmap data
        """
        return 
