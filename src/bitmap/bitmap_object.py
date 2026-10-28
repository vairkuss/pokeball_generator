from typing import Optional
from ..drawing import MatrixObject
from ..types import Options
from .bitmap_meta import BitmapMeta


class BitmapObject:

    def __init__(self, file: bytes, options: Options) -> None:
        self.meta: BitmapMeta = BitmapMeta()
        self.matrix: MatrixObject = 