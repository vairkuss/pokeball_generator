import os
from src import options, Backupper, PokeballGenerator, BitmapObject


# check if path was provided
filepath: str = options.file
prefix: str = "$ upd"
if filepath is None:
    filepath = "pokeball.bmp"
    prefix = "$ cre"
print(f'{prefix}ating "{os.path.abspath(filepath)}"')

# create canvas
bitmap_object: BitmapObject = BitmapObject(options)
if os.path.exists(filepath):
    with open(filepath, "rb") as file:
        data: bytes = file.read()
    Backupper.backup(options.file, data)
    print(f"$ File backup created '.backup/{options.file}'")

# run the pokeball generator and write the new data to the file
with open(options.file, "wb") as file:
    if options.pokerush:
        updated_data: bytes = PokeballGenerator.pokerush(options, data)
    else:
        updated_data: bytes = PokeballGenerator.generate(options, data)
    file.write(updated_data)

print(f"$ File '{options.file}' updated successfully")
