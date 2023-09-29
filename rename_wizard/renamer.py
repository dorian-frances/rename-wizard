import os
from typing import List

from rename_wizard.directory_renamer import DirectoryRenamer
from rename_wizard.enum.casing_type_enum import CasingTypeEnum
from rename_wizard.helper.file_helper import FileHelper


class Renamer:
    __directory_renamer: DirectoryRenamer
    __renamed_directory_counter: int

    def __init__(self, directory_renamer: DirectoryRenamer):
        self.__directory_renamer = directory_renamer
        self.__renamed_directory_counter = 0

    def rename(self, target_directory_path: str, casing_type: CasingTypeEnum) -> None:
        if FileHelper.is_a_file(target_directory_path):
            renamed_file_path: str = self.__get_renamed_directory_path(target_directory_path, casing_type)
            os.rename(target_directory_path, renamed_file_path)
            self.__renamed_directory_counter += 1
        elif FileHelper.is_an_empty_directory(target_directory_path):
            renamed_directory_path = self.__get_renamed_directory_path(target_directory_path, casing_type)
            os.rename(target_directory_path, renamed_directory_path)
            self.__renamed_directory_counter += 1
        else:
            renamed_directory_path = self.__get_renamed_directory_path(target_directory_path, casing_type)
            os.rename(target_directory_path, renamed_directory_path)
            self.__renamed_directory_counter += 1
            for directory in os.listdir(renamed_directory_path):
                directory_absolute_path: str = os.path.join(renamed_directory_path, directory)
                self.rename(directory_absolute_path, casing_type)

    def __get_renamed_directory_path(self, target_directory_path: str, casing_type: CasingTypeEnum):
        split_path: List[str] = target_directory_path.split("/")
        base_path: str = "/".join(split_path[:-1])
        target_file: str = split_path[-1]
        renamed_file_name: str = self.__directory_renamer.rename_directory_for_casing_type(target_file, casing_type)
        target_path_renamed: str = f"{base_path}/{renamed_file_name}"
        return target_path_renamed
