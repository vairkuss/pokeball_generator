from argparse import ArgumentParser, Nam, Namespace


description: str = """Pokeball Generator
This is an util to generate pokeball images on top of the original ones.
If the exiting file is not provided, it will be generated using given parameters."""

argparser: ArgumentParser = ArgumentParser(description)
argparser.add_argument("file", help="a path to the file")
argparser.add_argument("-w", help="the width of the generated bitmap", type=int, default=100)
argparser.add_argument("-h", help="the height of the generated bitmap", type=int, default=100)
argparser.add_argument("-x", help="the x-coordinate of the pokeball", type=int, default=50)
argparser.add_argument("-y", help="the y-coordinate of the pokeball", type=int, default=50)
argparser.add_argument("-r", help="the radius of the pokeball", type=int, default=80)
argparser.add_argument("--pokerush", help="generate 100 pokeballs on the bitmap", action="store_true")

argv: Namespace = argparser.parse_args()
