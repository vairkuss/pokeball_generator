import os


class Backupper:
    """
    Backupper is used to save the original files
    It is not being asked for in the task statement,
    but I find backups important, when I work
    with files.
    """
    
    @staticmethod
    def backup(path: str, data: bytes) -> None:
        """
        saves byte data to the backup folder,
        creates one, if it didn't exist
        
        :param path: a path to original file
        :param data: original file's data in bytes
        """
        folder, name: str = os.path.split(path)
        backup_folder: str = os.path.join(folder, ".backup")
        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)
        backup: str = os.path.join(backup_folder, name)
        with open(backup, "wb") as file:
            file.write(data)
    