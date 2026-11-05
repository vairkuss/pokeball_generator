import os
from argparse import Namespace
from typing import Optional
from .meta import Meta


class Options:
    """
    stores variables, important for the bitmap file and the pokéball generation
    """

    def __init__(self, args: Namespace) -> None:
        """
        stores provided arguments, creates Meta instance from the provided file data, sets the defaults

        :param args: the return value of argparse.ArgumentParser.parse_args()
        :raises: ValueError if -w or -h are lesser than 20
        """
        self.file: str = "" if args.file is None else args.file
        if self.file and not self.file.endswith(".bmp"):
            self.file += ".bmp"
        self.data: Optional[bytes] = None
        if os.path.exists(self.file):
            with open(self.file, "rb") as file:
                self.data = file.read()
        self.meta: Meta = Meta(args.w, args.h, self.data)

        bad_args: list[tuple[str, int]] = []
        for i, arg in enumerate((self.meta.w, self.meta.h)):
            if arg < 20:
                bad_args.append(("wh"[i], arg))
        if bad_args:
            msg: str ="> should be 20 or greater:\n"
            for dimension, value in bad_args:
                msg += f">\t-{dimension}: {value}\n"
            raise ValueError(msg)
        
        self.r: int = int(min(self.meta.w, self.meta.h) // 2) if args.r is None else args.r
        self.x: int = self.meta.w // 2 if args.x is None else self.meta.w - args.x
        self.y: int = self.meta.h // 2 if args.y is None else self.meta.h - args.y
        self.pokerush: bool = args.pokerush is not None
        