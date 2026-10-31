from argparse import Namespace


class Options:
    """
    stores the processed arguments provided by user
    """

    def __init__(self, args: Namespace) -> None:
        """
        proceeds through the given arguments and sets the defaults

        :param args: the return value of argparse.ArgumentParser.parse_args()
        """
        self.file: str = args.file
        self.w: int = 100 if args.w is None or args.w < 10 else args.w
        self.h: int = self.w if args.h is None or args.h < 10 else args.h
        self.r: int = min(self.w, self.h) // 2 if args.r is None else args.r
        self.x: int = self.r if args.x is None else args.x
        self.y: int = self.r if args.y is None else args.y
        self.pokerush: bool = args.pokerush
