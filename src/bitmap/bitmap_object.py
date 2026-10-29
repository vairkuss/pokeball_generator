from typing import Optional
from ..drawing import MatrixObject
from ..types import Options
from .bitmap_meta import BitmapMeta


class BitmapObject:
    """
    BitmapObject represents a bitmap image and provides methods to manipulate and access its pixel data.
    """

    def __init__(self, data: Optional[bytes], options: Optional[Options]) -> None:
        """
        :param data: The raw bitmap data.
        :param options: The options for the bitmap.
        """
        self.meta: BitmapMeta = BitmapMeta(data=data[0:54], options=options)
        self.matrix: MatrixObject = MatrixObject.from_bitmap(self.meta.width, self.meta.height, self.meta.padding, data)

    def to_bytes(self) -> bytes:
        """
        Converts the BitmapObject to raw bytes

        :returns: raw bitmap data
        """
        return self.meta.data + self.matrix.to_bytes(self.meta.padding)
