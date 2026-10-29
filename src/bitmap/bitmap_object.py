from typing import Optional
from src import BitmapMeta, MatrixObject
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
        self.matrix: MatrixObject = MatrixObject.from_bytes(self.meta.w, self.meta.h, self.meta.padding, data[54:])


    def to_bytes(self) -> bytes:
        """
        converts the BitmapObject to raw bytes

        :returns: raw bitmap data
        """
        return self.meta.data + self.matrix.to_bytes(self.meta.padding)
