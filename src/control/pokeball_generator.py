from typing import Optional


class PokeballGenerator:
    """
    PokeballGenerator edits existing bitmap data
    or generates new, if data wasn't provided.
    """

    @staticmethod
    def generate(x: Optional[int], y: Optional[int], r: Optional[int]) -> bytes:
        ...

    @staticmethod
    def pokerush() -> bytes:
        ...