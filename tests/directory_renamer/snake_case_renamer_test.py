import unittest

from rename_wizard.enum.casing_type_enum import CasingTypeEnum
from rename_wizard.directory_renamer import DirectoryRenamer


class SnakeCaseRenamerTest(unittest.TestCase):
    def test_should_rename_simple_directory_with_snake_case(self):
        self.__assert_new_filename_given_directory_name_and_casing_type("test", CasingTypeEnum.snake_case, "test")
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test.txt", CasingTypeEnum.snake_case, "test.txt"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "Test.txt", CasingTypeEnum.snake_case, "test.txt"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "TEst.txt", CasingTypeEnum.snake_case, "test.txt"
        )

    def test_should_rename_medium_directory_with_snake_case(self):
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test-test", CasingTypeEnum.snake_case, "test_test"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test test", CasingTypeEnum.snake_case, "test_test"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "testTest", CasingTypeEnum.snake_case, "test_test"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "testTesT", CasingTypeEnum.snake_case, "test_tes_t"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "TestTesT", CasingTypeEnum.snake_case, "test_tes_t"
        )

    def test_should_rename_complicated_directory_with_snake_case(self):
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "ceciEstUnTest.json", CasingTypeEnum.snake_case, "ceci_est_un_test.json"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "CeciEstUnTest.json", CasingTypeEnum.snake_case, "ceci_est_un_test.json"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test1file1.tkt", CasingTypeEnum.snake_case, "test_1_file_1.tkt"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "12test13file1.tkt", CasingTypeEnum.snake_case, "12_test_13_file_1.tkt"
        )

    def __assert_new_filename_given_directory_name_and_casing_type(
        self, directory_name: str, casing_type: CasingTypeEnum, target_directory_name: str
    ):
        directory_renamer: DirectoryRenamer = DirectoryRenamer()
        renamed_directory: str = directory_renamer.rename_directory_for_casing_type(directory_name, casing_type)
        self.assertEqual(renamed_directory, target_directory_name)
