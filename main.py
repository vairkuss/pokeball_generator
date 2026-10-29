import os
from typing import Optional
from src import Backupper, PokeballGenerator
from src.types import options


data: Optional[bytes] = None
if os.path.exists(options["file"]):
    with open(options["file"], "rb") as file:
        data = file.read()
    Backupper.backup(options["file"], data)

PokeballGenerator.generate(options, data)
