from typing import Optional
from ..drawing import MatrixObject
from ..types import Options
from .bitmap_meta import BitmapMeta


class BitmapObject:

    def __init__(self, data: Optional[bytes], options: Optional[Options]) -> None:
        self.meta: BitmapMeta = BitmapMeta()
        if options is not None:
            self.meta.options = options
        self.matrix: MatrixObject = MatrixObject.from_bitmap(self.meta.width, self.meta.height, self.meta.padding, data)
