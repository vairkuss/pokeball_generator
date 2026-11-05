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
        :raises: SystemExit if user won't want to overwrite the backup
        :returns: path to the backup file
        """
        with open(path, "rb") as file:
            data: bytes = file.read()
        folder, name = os.path.split(path)
        backup_folder: str = os.path.join(folder, ".backup")
        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)
        backup_file: str = os.path.join(backup_folder, name)
        if os.path.exists(backup_file):
            asking: bool = True
            while asking:
                user_input: str = input("> backup would be overwritten! continue? [Y/n]")
                if user_input.lower() == "n":
                    raise SystemExit("> overwrite cancelled")
                elif not user_input or user_input.lower() == "y":
                    asking = False
        with open(backup_file, "wb") as file:
            file.write(data)

        return backup_file
    