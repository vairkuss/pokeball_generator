import os
from argparse import ArgumentParser
from src import Options, Backupper, PokeballGenerator


def parse_args() -> Options:
    """
    sets the description and stores command line argument in Options instance
    
    :returns: Options instance
    """

    description: str = """
    Pokéball Generator
    This is a simple program to generate a pokéball on top of the windows bitmap.
    If the exiting file is not provided, new will be generated using given parameters.
    """

    argparser: ArgumentParser = ArgumentParser(description, add_help=False)
    argparser.add_argument("file", help="the path to the file", nargs="?", default=None)
    argparser.add_argument("-w", help="the width of the generated bitmap", type=int, default=21)
    argparser.add_argument("-h", help="the height of the generated bitmap", type=int)
    argparser.add_argument("-x", help="the x-coordinate of the pokéball in pixels", type=int)
    argparser.add_argument("-y", help="the y-coordinate of the pokéball in pixels", type=int)
    argparser.add_argument("-r", help="the radius of the pokéball", type=int)
    argparser.add_argument("pokerush", help="generate 100 random pokéballs", nargs="?", choices=["pokerush"])
    argparser.add_argument("--help", help="show this message", action="help")

    return Options(argparser.parse_args())


if __name__ == "__main__":

    # parse arguments
    options: Options = parse_args()

    # prove that user really wants to name the file as "pokerush"
    if options.file == "pokerush":
        name_pokerush: str = input('> do You really want to name the file as "pokerush"? [y/N] ')
        if name_pokerush.lower() != "y":
            options.file = input("> please, write new file name or path\n> ")
            options.pokerush = True

    # check if file existed and correct file name
    prefix: str = "upd"
    if options.data is None:
        if not options.file:
            print("> no file name provided, using the default")
            options.file = "pokéball.bmp"
        prefix = "cre"
    if not options.file.endswith(".bmp"):
        options.file += ".bmp"
    print(f'> {prefix}ating "{os.path.abspath(options.file)}"')

    # read and backup original file if existed
    if os.path.exists(options.file):
        backup_file_path: str = Backupper.backup(options.file)
        print(f'> backuped to "{os.path.abspath(backup_file_path)}"')

    # update or write new file with the pokéball(s)
    new_data: bytes = PokeballGenerator.overwrite_data(options)
    with open(options.file, "wb") as file:
        file.write(new_data)

    print("> done")
