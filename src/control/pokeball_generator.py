import random
from typing import Optional
from src.types.options import Options


class PokeballGenerator:
    """
    PokeballGenerator edits existing bitmap data
    or generates new, if data wasn't provided.
    """

    @staticmethod
    def generate(options: Options, data: Optional[bytes] = None) -> bytes:
        """
        :param options: the options for the bitmap
        :param data: the existing bitmap data
        :returns: the new bitmap data with a defined pokeball on it
        """
        ...
        

    @staticmethod
    def pokerush() -> bytes:
        for i in range(100):
            random_x = random.randint(0, 1000)
            random_y = random.randint(0, 1000)