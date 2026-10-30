import os
from src import Backupper


def test_backup(path: str, test_data: bytes) -> None:
    Backupper.backup(path, test_data)

    #check if backup file wasn't written
    backup: str = os.path.join(".backup", path)
    if not os.path.exists(backup):
        raise SystemExit("backup folder wasn't created")

    #check if backup file wasn't written correctly
    with open(backup, "rb") as file:
        data: bytes = file.read()
        if data != test_data:
            raise SystemExit(f"wrong data in backup file, {data.hex()} != {test_data.hex()}")
        
    os.unlink(backup)


print("Backupper:")

# check if folder existed before test
delete_after: bool = False
if not os.path.exists(".backup"):
    delete_after = True

# test class
test_backup("test1.txt", b'\xca\xfe\xba\xbe')
test_backup("test2.txt", b'\xde\xad\xbe\xef')


# delete excessive folder after test
if delete_after:
    os.rmdir(".backup")


print("ok\n")
