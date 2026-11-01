import random
from typing import Optional
from src import Options, BitmapObject, MatrixObject, Rect, Circle
from src.types import Color


class PokeballGenerator:
    """
    generates a bitmap data with a pokeball on it
    or edits the existing data, if provided
    """

    @staticmethod
    def generate(options: Options, data: Optional[bytes] = None) -> bytes:
        """
        generates a bitmap with a single user-defined pokeball on it
        or edits an existing bitmap data, if provided
        
        :param options: options for the bitmap
        :param data: existing bitmap data
        :returns: new bitmap data with a defined pokeball on it
        """
        canvas: BitmapObject = BitmapObject(options)

        r = options.r
        d = r * 2

        WHITE: Color = (256, 256, 256)
        RED: Color = (256, 0, 0)
        BLACK: Color = (0, 0, 0)

        base: Circle = Circle(r, WHITE)

        red_top: Rect = Rect(d, r, RED)
        malasian_flag: MatrixObject = base.paint(red_top.data)

        black_stripe: Rect = Rect(d, d // 7, BLACK)
        pokeball_from_behind: MatrixObject = malasian_flag.shadow(black_stripe.data, 0, r // 7)

        button_ring: Circle = Circle(d // 4, BLACK)
        broken_pokeball: MatrixObject = pokeball_from_behind.paint(button_ring.data, r, r)

        button: Circle = Circle(d // 3, WHITE)
        pokeball: MatrixObject = broken_pokeball.paint(button.data, r, r)

        canvas.write(pokeball.data, options.x, options.y)
        return canvas.data



    @staticmethod
    def pokerush(options: Options, data: Optional[bytes] = None) -> bytes:
        """
        generates a bitmap with 100 random pokeballs on it
        or edits an existing bitmap data, if provided

        :param options: options for the bitmap
        :param data: existing bitmap data
        :returns: new bitmap data with 100 random pokeballs on it
        """
        if data is not None:
            w: int = int.from_bytes(data[18:22], byteorder="little")
            h: int = int.from_bytes(data[22:26], byteorder="little")
        else:
            w: int = options.meta.w
            h: int = options.meta.h
        max_r: int = int(max(w, h) / 2.5)

        canvas: BitmapObject = BitmapObject(options)
        
        for i in range(100):
            x: int = random.randint(0, w)
            y: int = random.randint(0, h)
            r: int = random.randint(7, max_r)
        return canvas.data
