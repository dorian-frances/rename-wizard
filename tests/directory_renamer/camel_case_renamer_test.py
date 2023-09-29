import unittest

from rename_wizard.enum.casing_type_enum import CasingTypeEnum
from rename_wizard.directory_renamer import DirectoryRenamer


class CamelCaseRenamerTest(unittest.TestCase):
    def test_should_rename_simple_directory_with_camel_case(self):
        self.__assert_new_filename_given_directory_name_and_casing_type("test", CasingTypeEnum.camel_case, "test")
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test.txt", CasingTypeEnum.camel_case, "test.txt"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "Test.txt", CasingTypeEnum.camel_case, "test.txt"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "TEst.txt", CasingTypeEnum.camel_case, "test.txt"
        )

    def test_should_rename_medium_directory_with_camel_case(self):
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test-test", CasingTypeEnum.camel_case, "testTest"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test test", CasingTypeEnum.camel_case, "testTest"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "testTest", CasingTypeEnum.camel_case, "testTest"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "testTesT", CasingTypeEnum.camel_case, "testTesT"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "TestTesT", CasingTypeEnum.camel_case, "testTesT"
        )

    def test_should_rename_complicated_directory_with_camel_case(self):
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "ceciEstUnTest.json", CasingTypeEnum.camel_case, "ceciEstUnTest.json"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "CeciEstUnTest.json", CasingTypeEnum.camel_case, "ceciEstUnTest.json"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "test1file1.tkt", CasingTypeEnum.camel_case, "test1File1.tkt"
        )
        self.__assert_new_filename_given_directory_name_and_casing_type(
            "12test13file1.tkt", CasingTypeEnum.camel_case, "12Test13File1.tkt"
        )

    def __assert_new_filename_given_directory_name_and_casing_type(
        self, directory_name: str, casing_type: CasingTypeEnum, target_directory_name: str
    ):
        directory_renamer: DirectoryRenamer = DirectoryRenamer()
        renamed_directory: str = directory_renamer.rename_directory_for_casing_type(directory_name, casing_type)
        self.assertEqual(renamed_directory, target_directory_name)
