import os
from typing import Optional
from .src import argv, Backupper, PokeballGenerator


data: Optional[bytes] = None
if os.path.exists(argv.file):
    with open(argv.file, "rb") as file:
        data = file.read()
    Backupper.backup(argv.file, data)

PokeballGenerator.generate(argv, data)
