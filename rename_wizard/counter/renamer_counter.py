import os

from rename_wizard.helper.file_helper import FileHelper


class RenamerCounter:
    directory_counter: int

    def __init__(self):
        self.directory_counter = 0

    def count_directories(self, target_directory_path) -> None:
        if FileHelper.is_a_file(target_directory_path):
            self.directory_counter += 1
        elif FileHelper.is_an_empty_directory(target_directory_path):
            self.directory_counter += 1
        else:
            self.directory_counter += 1
            for directory in os.listdir(target_directory_path):
                directory_absolute_path: str = os.path.join(target_directory_path, directory)
                self.count_directories(directory_absolute_path)
