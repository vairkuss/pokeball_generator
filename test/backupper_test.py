import os
from ..classes.control.backupper import Backupper


print("Backupper:")
test_data: bytes = b'\xca\xfe\xba\xbe'
Backupper.backup("file.txt", test_data)

# check if folder was created
if not os.path.exists(".backup"):
    raise SystemExit("backup folder wasn't created")

#check if backup file wasn't written
backup: str = os.path.join(".backup", "file.txt")
if not os.path.exists(backup):
    raise SystemExit("backup folder wasn't created")

#check if backup file wasn't written correctly
with open(backup, "rb") as file:
    data: bytes = file.read()
    if data != test_data:
        raise SystemExit(f"backup file is written wrong, {data.hex()} != {test_data.hex()}")

# clean after test
os.unlink(".backup")

print("ok\n")
