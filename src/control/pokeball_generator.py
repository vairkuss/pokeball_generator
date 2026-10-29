from typing import Optional
from argparse import Namespace


class PokeballGenerator:
    """
    PokeballGenerator edits existing bitmap data
    or generates new, if data wasn't provided.
    """

    @staticmethod
    def generate(argv: Namespace, data: Optional[bytes] = None) -> bytes:
        ...
        

    @staticmethod
    def pokerush() -> bytes:
        ...