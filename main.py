import os
from argparse import ArgumentParser
from src import Options, Backupper, PokeballGenerator


def parse_args() -> Options:
    """
    sets the description, parses the command line arguments and returns an Options instance
    """
    description: str = """
    Pokeball Generator
    This is a simple program to generate pokeball on top of the windows bitmap.
    If the exiting file is not provided, new will be generated using given parameters.
    """

    argparser: ArgumentParser = ArgumentParser(description)
    argparser.add_argument("file", nargs="?", help="the path to the file", default=None)
    argparser.add_argument("--w", help="the width of the generated bitmap", type=int, default=None)
    argparser.add_argument("--h", help="the height of the generated bitmap", type=int, default=None)
    argparser.add_argument("--x", help="the x-coordinate of the pokeball in pixels", type=int, default=None)
    argparser.add_argument("--y", help="the y-coordinate of the pokeball in pixels", type=int, default=None)
    argparser.add_argument("--r", help="the radius of the pokeball", type=int, default=None)
    argparser.add_argument("--pokerush", help="generate 100 random pokeballs", action="store_true")

    return Options(argparser.parse_args())


if __name__ == "__main__":

    # parse arguments
    options: Options = parse_args()

    # check if path was valid
    prefix: str = "upd"
    if options.data is None:
        options.file = "pokeball.bmp"
        prefix = "cre"
    print(f'> {prefix}ating "{os.path.abspath(options.file)}"')

    # read and backup original file if existed
    if os.path.exists(options.file):
        backup: str = Backupper.backup(options.file)
        print(f'> backuped to "{os.path.abspath(backup)}"')

    # update or write new file with the pokeball(s) 
    with open(options.file, "wb") as file:
        updated_data: bytes = PokeballGenerator.generate(options)
        file.write(updated_data)

    print("> done")
