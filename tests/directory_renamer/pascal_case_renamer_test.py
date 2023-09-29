import unittest

from rename_wizard.enum.casing_type_enum import CasingTypeEnum
from rename_wizard.directory_renamer import DirectoryRenamer


class PascalCaseRenamerTest(unittest.TestCase):
    def test_should_rename_simple_directory_with_pascal_case(self):
        self.__assert_new_filename_given_directory_name_and_casing_type("test", CasingTypeEnum.pascal_case, "Test")
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test.txt", CasingTypeEnum.pascal_case, "Test.txt"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "Test.txt", CasingTypeEnum.pascal_case, "Test.txt"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "TEst.txt", CasingTypeEnum.pascal_case, "Test.txt"
        )

    def test_should_rename_medium_directory_with_pascal_case(self):
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test-test", CasingTypeEnum.pascal_case, "TestTest"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test test", CasingTypeEnum.pascal_case, "TestTest"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "testTest", CasingTypeEnum.pascal_case, "TestTest"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "testTesT", CasingTypeEnum.pascal_case, "TestTesT"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "TestTesT", CasingTypeEnum.pascal_case, "TestTesT"
        )

    def test_should_rename_complicated_directory_with_camel_case(self):
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "ceciEstUnTest.json", CasingTypeEnum.pascal_case, "CeciEstUnTest.json"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "CeciEstUnTest.json", CasingTypeEnum.pascal_case, "CeciEstUnTest.json"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test1file1.tkt", CasingTypeEnum.pascal_case, "Test1File1.tkt"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "12test13file1.tkt", CasingTypeEnum.pascal_case, "12Test13File1.tkt"
        )

    def __assert_new_filename_given_directory_name_and_casing_type(
        self, directory_name: str, casing_type: CasingTypeEnum, target_filename: str
    ):
        directory_renamer: DirectoryRenamer = DirectoryRenamer()
        renamed_directory: str = directory_renamer.rename_directory_for_casing_type(directory_name, casing_type)
        self.assertEqual(renamed_directory, target_filename)
