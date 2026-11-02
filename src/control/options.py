import os
from argparse import Namespace
from typing import Optional
from .meta import Meta


class Options:
    """
    stores variables, important for the bitmap file and the pokeball generation
    """

    def __init__(self, args: Namespace) -> None:
        """
        stores provided arguments, creates Meta instance from the provided file data

        :param args: the return value of argparse.ArgumentParser.parse_args()
        """
        self.file: str = "" if args.file is None else args.file
        self.data: Optional[bytes] = None
        if os.path.exists(self.file):
            with open(self.file, "rb") as file:
                self.data = file.read()
        self.meta: Meta = Meta(self.data)
        self.meta.w = self.meta.w if args.w is None or args.w < 10 else args.w
        self.meta.h = self.meta.h if args.h is None or args.h < 10 else args.h
        self.r: int = int(min(self.meta.w, self.meta.h) // 2.5) if args.r is None else args.r
        self.x: int = self.r if args.x is None else args.x
        self.y: int = self.r if args.y is None else args.y
        self.pokerush: bool = args.pokerush

        error_message: list[str] = []
        if self.meta.w < 0:
            error_message.append("width must be a positive integer")
        if self.meta.h < 0:
            error_message.append("height must be a positive integer")
        if self.r < 0:
            error_message.append("radius must be a positive integer")
        if len(error_message):
            raise ValueError(f"$ bad arguments:{'\n'.join(error_message)}")
        