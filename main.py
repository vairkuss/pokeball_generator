import os
from typing import Optional
from src import options, Backupper, PokeballGenerator


# check if the file path is provided
if options["file"] is None:
    options["file"] = "pokeball.bmp"
    print(f"$ File path not provided, default: {options['file']}")

# check if the file exists, if yes, read the data and backup it
data: Optional[bytes] = None
if os.path.exists(options["file"]):
    with open(options["file"], "rb") as file:
        data: bytes = file.read()
    Backupper.backup(options["file"], data)
    print(f"$ File backup created '.backup/{options['file']}'")

# run the pokeball generator and write the new data to the file
with open(options["file"], "wb") as file:
    if options["pokerush"]:
        updated_data: bytes = PokeballGenerator.pokerush(options, data)
    else:
        updated_data: bytes = PokeballGenerator.generate(options, data)
    file.write(updated_data)

print(f"$ File '{options['file']}' updated successfully")
