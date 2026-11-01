import os


class Backupper:
    """
    backups the original file to the .backup folder
    """
    
    @staticmethod
    def backup(path: str) -> str:
        """
        saves the original file to the .backup folder,
        creates .backup folder if it didn't exist
        
        :param path: path to original file
        :returns: path to the backup file
        """
        with open(path, "rb") as file:
            data: bytes = file.read()
        folder, name = os.path.split(path)
        backup_folder: str = os.path.join(folder, ".backup")
        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)
        backup_file: str = os.path.join(backup_folder, name)
        with open(backup_file, "wb") as file:
            file.write(data)

        return backup_file
    