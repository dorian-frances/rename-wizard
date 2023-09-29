import re
from typing import List

from rename_wizard.enum.casing_type_enum import CasingTypeEnum


class DirectoryRenamer:
    def rename_directory_for_casing_type(self, target_directory_name: str, casing_type: CasingTypeEnum) -> str:
        match casing_type:
            case CasingTypeEnum.snake_case:
                return self.__snake_case_renamer(target_directory_name)
            case CasingTypeEnum.camel_case:
                return self.__camel_case_renamer(target_directory_name)
            case CasingTypeEnum.pascal_case:
                return self.__pascal_case_renamer(target_directory_name)
            case CasingTypeEnum.kebab_case:
                return self.__kebab_case_renamer(target_directory_name)

    def __camel_case_renamer(self, target_directory_name) -> str:
        formatted_directory_name: str = self.__snake_case_renamer(target_directory_name)
        split_directory_name: List[str] = formatted_directory_name.split("_")
        camel_case_directory_name: str = split_directory_name[
            0
        ] + self.__capitalize_first_letter_of_each_word_of_the_list(split_directory_name[1:])
        return camel_case_directory_name

    def __pascal_case_renamer(self, target_directory_name) -> str:
        formatted_directory_name: str = self.__snake_case_renamer(target_directory_name)
        split_directory_name: List[str] = formatted_directory_name.split("_")
        pascal_case_directory_name: str = self.__capitalize_first_letter_of_each_word_of_the_list(split_directory_name)
        return pascal_case_directory_name

    @staticmethod
    def __kebab_case_renamer(target_directory_name):
        formatted_directory_name: str = re.sub("([a-z0-9])([A-Z])", r"\1_\2", target_directory_name)
        formatted_directory_name: str = re.sub("([a-zA-Z])([0-9])", r"\1_\2", formatted_directory_name)
        formatted_directory_name: str = re.sub("([0-9])([a-zA-Z])", r"\1_\2", formatted_directory_name)
        formatted_directory_name = formatted_directory_name.replace(" ", "-")
        formatted_directory_name = formatted_directory_name.replace("_", "-")
        formatted_directory_name = formatted_directory_name.lower()
        return formatted_directory_name

    @staticmethod
    def __snake_case_renamer(target_directory_name) -> str:
        formatted_directory_name: str = re.sub("([a-z0-9])([A-Z])", r"\1_\2", target_directory_name)
        formatted_directory_name: str = re.sub("([a-zA-Z])([0-9])", r"\1_\2", formatted_directory_name)
        formatted_directory_name: str = re.sub("([0-9])([a-zA-Z])", r"\1_\2", formatted_directory_name)
        formatted_directory_name = formatted_directory_name.replace(" ", "_")
        formatted_directory_name = formatted_directory_name.replace("-", "_")
        formatted_directory_name = formatted_directory_name.lower()
        return formatted_directory_name

    @staticmethod
    def __capitalize_first_letter_of_each_word_of_the_list(word_list: List[str]) -> str:
        final_world: str = ""
        for word in word_list:
            final_world = final_world + word.capitalize()
        return final_world
