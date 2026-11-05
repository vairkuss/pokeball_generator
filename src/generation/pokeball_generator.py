import random
from .bitmap_object import BitmapObject
from ..control import Options
from ..matrix import MatrixObject, Rect, Circle
from ..types import Color


class PokeballGenerator:
    """
    generates a bitmap data with a pokéball on it
    or edits the existing data, if provided
    """

    @staticmethod
    def __render_pokeball(r: int) -> MatrixObject:
        """
        generates a MatrixObject with a single user-defined pokéball on it
        
        :param r: radius of the pokéball
        :returns: new pokéball matrix
        """
        d = r * 2

        WHITE: Color = (255, 255, 255)
        RED: Color = (255, 0, 0)
        BLACK: Color = (0, 0, 0)

        base: Circle = Circle(r, WHITE)

        red_top: Rect = Rect(d, r, RED)
        malasian_flag: MatrixObject = base.shadow(red_top.data)

        stripe_width: int = d // 7
        stripe_offset: int = r - stripe_width // 2
        black_stripe: Rect = Rect(d, stripe_width, BLACK)
        pokeball_from_behind: MatrixObject = malasian_flag.shadow(black_stripe.data, 0, stripe_offset)

        button_ring_r: int = stripe_width * 3 // 2
        button_ring_offset: int = r - button_ring_r
        button_ring: Circle = Circle(button_ring_r, BLACK)
        broken_pokeball: MatrixObject = pokeball_from_behind.paint(button_ring.data, button_ring_offset, button_ring_offset)

        button: Circle = Circle(stripe_width // 2, WHITE)
        pokeball: MatrixObject = broken_pokeball.paint(button.data, stripe_offset, stripe_offset)

        return pokeball
    

    @staticmethod
    def overwrite_data(options: Options) -> bytes:
        """
        generates a bitmap with a single user-defined pokéball on it
        or edits an existing bitmap data, if provided; if pokerush is
        set, generates 10 to 100 random pokéballs on the bitmap instead
        
        :param options: options for the bitmap
        :param data: existing bitmap data
        :returns: new bitmap data with a defined pokéball on it
        """
        canvas: BitmapObject = BitmapObject(options)
        if options.data is not None:
            image: MatrixObject = MatrixObject.from_bytes(options.meta.w, options.meta.h, options.data[options.meta.image_offset:])
            canvas.write(image.data)
        if options.pokerush:
            for _ in range(random.randint(10, 100)):
                x: int = random.randint(0, options.meta.w)
                y: int = random.randint(0, options.meta.h)
                r: int = random.randint(10, min(options.meta.w, options.meta.h) // 2)
                pokeball: MatrixObject = PokeballGenerator.__render_pokeball(r)
                canvas.write(pokeball.data, x + r, y + r)
        else:
            r: int = options.r
            x: int = options.x + r
            y: int = options.y + r
            pokeball: MatrixObject = PokeballGenerator.__render_pokeball(options.r)
            canvas.write(pokeball.data, x, y)

        return canvas.data
