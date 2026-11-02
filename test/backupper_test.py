import os
from src import Backupper


def test_backup(path: str, test_data: bytes) -> None:
    #write test file
    with open(path, "wb") as file:
        file.write(test_data)

    Backupper.backup(path)

    #check if backup file wasn't written
    backup: str = os.path.join(".backup", path)
    if not os.path.exists(backup):
        raise SystemExit("backup folder wasn't created")

    #check if backup file was written correctly
    with open(backup, "rb") as file:
        data: bytes = file.read()
        if data != test_data:
            raise SystemExit(f"wrong data in backup file, {data.hex()} != {test_data.hex()}")
        
    os.unlink(backup)
    os.unlink(path)


print("Backupper:")

# check if folder existed before test
delete_after: bool = False
if not os.path.exists(".backup"):
    delete_after = True

# test class
test_backup("test1.class", b'\xca\xfe\xba\xbe')
test_backup("test2.ext", b'\xde\xad\xbe\xef')


# delete excessive folder after test
if delete_after:
    os.rmdir(".backup")


print("ok\n")
