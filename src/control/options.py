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
        self.data: Optional[bytes] = None
        if os.path.exists(self.file):
            with open(self.file, "rb") as file:
                self.data = file.read()
        self.meta: Meta = Meta(args.w, args.h, self.data)

        bad_args: list[tuple[str, int]] = []
        for i, arg in enumerate((args.w, args.h)):
            if arg < 20:
                bad_args.append(("wh"[i], arg))
        if bad_args:
            print("> should be 20 or greater:")
            for dimension, value in bad_args:
                print(f">\t-{dimension}: {value}")
            raise SystemExit
        
        self.r: int = int(min(self.meta.w, self.meta.h) // 2) if args.r is None else args.r
        self.x: int = (self.meta.w // 2 if args.x is None else args.x) - self.meta.w + self.r
        self.y: int = (self.meta.h // 2 if args.y is None else args.y) - self.meta.h + self.r
        self.pokerush: bool = args.pokerush is not None
        