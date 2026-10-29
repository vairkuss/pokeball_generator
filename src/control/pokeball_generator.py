import random
from typing import Optional
from src import PokeballMatrix, BitmapObject, MatrixObject
from src.types import Options


class PokeballGenerator:
    """
    generates a bitmap data with a pokeball on it
    or edits the existing file, if provided
    """

    @staticmethod
    def generate(options: Options, data: Optional[bytes] = None) -> MatrixObject:
        """
        generates a bitmap with a single defined pokeball on it
        or edits existing bitmap data, if provided
        
        :param options: the options for the bitmap
        :param data: the existing bitmap data
        :returns: the new bitmap data with a defined pokeball on it
        """
        canvas: BitmapObject = BitmapObject(data, options)
        return canvas.matrix.paint(PokeballMatrix(options), options["x"], options["y"])



    @staticmethod
    def pokerush(options: Options, data: Optional[bytes] = None) -> MatrixObject:
        """
        generates a bitmap with 100 random pokeballs on it
        or edits existing bitmap data, if provided

        :param options: the options for the bitmap
        :param data: the existing bitmap data
        :returns: the new bitmap data with 100 random pokeballs on it
        """
        if data is not None:
            w: int = int.from_bytes(data[18:22], byteorder="little")
            h: int = int.from_bytes(data[22:26], byteorder="little")
        else:
            w: int = 1000 if options["w"] is None else options["w"]
            h: int = w if options["h"] is None else options["h"]
        max_r: int = min(w, h) * 0.4 if options["r"] is None else options["r"]

        canvas: BitmapObject = BitmapObject(data, options)
        
        for i in range(100):
            x: int = random.randint(0, w)
            y: int = random.randint(0, h)
            r: int = random.randint(7, max_r)
        return canvas.to_bytes()
