import random
from typing import Optional
from src import Options, PokeballMatrix, BitmapObject, MatrixObject


class PokeballGenerator:
    """
    generates a bitmap data with a pokeball on it
    or edits the existing file, if provided
    """

    @staticmethod
    def generate(options: Options, data: Optional[bytes] = None) -> bytes:
        """
        generates a bitmap with a single defined pokeball on it
        or edits existing bitmap data, if provided
        
        :param options: the options for the bitmap
        :param data: the existing bitmap data
        :returns: the new bitmap data with a defined pokeball on it
        """
        canvas: BitmapObject = BitmapObject(options)
        canvas.write(PokeballMatrix(options.r).data, options.x, options.y)
        return canvas.data



    @staticmethod
    def pokerush(options: Options, data: Optional[bytes] = None) -> bytes:
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
            w: int = options.w
            h: int = options.h
        max_r: int = int(max(w, h) / 2.5)

        canvas: BitmapObject = BitmapObject(options)
        
        for i in range(100):
            x: int = random.randint(0, w)
            y: int = random.randint(0, h)
            r: int = random.randint(7, max_r)
        return canvas.data
