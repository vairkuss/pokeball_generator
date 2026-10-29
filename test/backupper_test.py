import os
from os import path
from src import Backupper


print("Backupper:")

# check if folder was created
if not os.path.exists(".backup"):
    raise SystemExit("backup folder wasn't created")


def check_backup_file(path: str, test_data: bytes) -> None:
    Backupper.backup(path, test_data)

    #check if backup file wasn't written
    backup: str = os.path.join(".backup", path)
    if not os.path.exists(backup):
        raise SystemExit("backup folder wasn't created")

    #check if backup file wasn't written correctly
    with open(backup, "rb") as file:
        data: bytes = file.read()
        if data != test_data:
            raise SystemExit(f"backup file is written wrong, {data.hex()} != {test_data.hex()}")


check_backup_file("test1.txt", b'\xca\xfe\xba\xbe')
check_backup_file("test2.txt", b'\xde\xad\xbe\xef')


# clean after test
for file in os.listdir(".backup"):
    os.unlink(os.path.join(".backup", file))
os.rmdir(".backup")


print("ok\n")
