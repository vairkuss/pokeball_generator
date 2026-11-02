import random
from typing import Optional
from .bitmap_object import BitmapObject
from ..control import Options
from ..abstract import MatrixObject, Rect, Circle
from ..types import Color


class PokeballGenerator:
    """
    generates a bitmap data with a pokeball on it
    or edits the existing data, if provided
    """

    @staticmethod
    def construct(r: int, x: int, y: int) -> MatrixObject:
        """
        generates a MatrixObject with a single user-defined pokeball on it
        
        :param r: radius of the pokeball
        :param x: x-coordinate of the pokeball
        :param y: y-coordinate of the pokeball
        :returns: new pokeball matrix
        """
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

        return pokeball
    

    @staticmethod
    def generate(options: Options, data: Optional[bytes] = None) -> bytes:
        """
        generates a bitmap with a single user-defined pokeball on it
        or edits an existing bitmap data, if provided; if pokerush is
        set, generates 100 random pokeballs on the bitmap instead
        
        :param options: options for the bitmap
        :param data: existing bitmap data
        :returns: new bitmap data with a defined pokeball on it
        """
        canvas: BitmapObject = BitmapObject(options)
        if data is not None:
            image: MatrixObject = MatrixObject.from_bytes(options.meta.w, options.meta.h, data)
            canvas.write(image.data)
        if options.pokerush:
            for _ in range(100):
                x: int = random.randint(0, options.meta.w)
                y: int = random.randint(0, options.meta.h)
                r: int = random.randint(4, int(max(options.meta.w, options.meta.h) / 2.5))
                pokeball: MatrixObject = PokeballGenerator.construct(r, x, y)
                canvas.write(pokeball.data, x, y)
        else:
            pokeball: MatrixObject = PokeballGenerator.construct(options.r, options.x, options.y)
            canvas.write(pokeball.data, options.x, options.y)
        return canvas.data
