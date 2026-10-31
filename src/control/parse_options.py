from argparse import ArgumentParser
from .options import Options


description: str = """Pokeball Generator
This is a simple program to generate pokeball bitmap on top of the original one.
If the exiting file is not provided, new will be generated using given parameters."""

argparser: ArgumentParser = ArgumentParser(description)
argparser.add_argument("file", nargs="?", help="the path to the file", default=None)
argparser.add_argument("-w", help="the width of the generated bitmap", type=int, default=None)
argparser.add_argument("-h", help="the height of the generated bitmap", type=int, default=None)
argparser.add_argument("-x", help="the x-coordinate of the pokeball in pixels", type=int, default=None)
argparser.add_argument("-y", help="the y-coordinate of the pokeball in pixels", type=int, default=None)
argparser.add_argument("-r", help="the radius of the pokeball", type=int, default=None)
argparser.add_argument("--pokerush", help="generate 100 random pokeballs", action="store_true")

options: Options = Options(argparser.parse_args())
