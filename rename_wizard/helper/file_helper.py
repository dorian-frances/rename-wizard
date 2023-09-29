import os


class FileHelper:
    @staticmethod
    def is_a_file(path) -> bool:
        return os.path.isfile(path)

    @staticmethod
    def is_an_empty_directory(path) -> bool:
        return len(os.listdir(path)) == 0
