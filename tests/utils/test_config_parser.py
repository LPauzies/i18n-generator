import pathlib
import unittest
import os
from i18ngenerator.languages import Language
from i18ngenerator.utils.config_parser import Configuration, ConfigurationModel, ConfigurationParser
from i18ngenerator.utils.exceptions import FileNotFoundException, WrongExtensionException, WrongParameterTypeException

class TestConfigurationParser(unittest.TestCase):
    
    def test_parse_from_yaml(self):
        # Given
        path_yaml = pathlib.Path("tests", "data", "config.yaml")

        # Expected
        expected_configuration = Configuration(
            pathlib.Path("tests", "data", "fr.json"),
            Language.FRENCH,
            [
                Language.ENGLISH,
                Language.CHINESE,
                Language.RUSSIAN,
                Language.PORTUGUESE
            ]
        )

        # Do
        configuration = ConfigurationParser.parse_from_yaml(path_yaml)
        self.assertEqual(configuration, expected_configuration)

    def test_parse_from_yaml_not_exist(self):
        # Given
        path_yaml = pathlib.Path("tests", "data", "config_not_exists.yaml")

        # Expected
        # Raise FileNotFoundException

        # Do
        with self.assertRaises(FileNotFoundException):
            configuration = ConfigurationParser.parse_from_yaml(path_yaml)

    def test_parse_from_json(self):
        # Given
        path = pathlib.Path("tests", "data", "config.json")

        # Expected
        # Raise FileNotFoundException

        # Do
        with self.assertRaises(WrongExtensionException):
            configuration = ConfigurationParser.parse_from_yaml(path)

    def test_parse_from_yaml_main_locale_file_not_exist(self):
        # Given
        path_yaml = pathlib.Path("tests", "data", "main_locale_not_exist-config.yaml")

        # Expected
        # Raise FileNotFoundException

        # Do
        with self.assertRaises(FileNotFoundException):
            configuration = ConfigurationParser.parse_from_yaml(path_yaml)

    def test_check_configuration_type(self):
        # Given
        configuration_dict = {
            ConfigurationModel.MAIN_FILE: "dummy/path/locale.json",
            ConfigurationModel.FROM: "fr",
            ConfigurationModel.TO: ["en", "es", "zh"]
        }

        # Expected
        configuration_model = [
            (ConfigurationModel.MAIN_FILE, str),
            (ConfigurationModel.FROM, str),
            (ConfigurationModel.TO, list)
        ]

        # Do
        for key_conf_model in configuration_model:
            try:
                ConfigurationParser._check_configuration_type(configuration_dict, key_conf_model[0], key_conf_model[1])
            except Exception as e:
                self.fail(e)

    def test_check_configuration_type_without_good_keys(self):
        # Given
        configuration_dict = {
            "dummy": "dummy/path/locale.json",
            ConfigurationModel.FROM: "fr",
            ConfigurationModel.TO: ["en", "es", "zh"]
        }

        # Expected
        configuration_model = [
            (ConfigurationModel.MAIN_FILE, str),
            (ConfigurationModel.FROM, str),
            (ConfigurationModel.TO, list)
        ]

        # Do
        with self.assertRaises(KeyError):
            for key_conf_model in configuration_model:
                ConfigurationParser._check_configuration_type(configuration_dict, key_conf_model[0], key_conf_model[1])

    def test_check_configuration_type_without_good_type(self):
        # Given
        configuration_dict = {
            ConfigurationModel.MAIN_FILE: ["dummy", "dummy", "dummy"],
            ConfigurationModel.FROM: "fr",
            ConfigurationModel.TO: ["en", "es", "zh"]
        }

        # Expected
        configuration_model = [
            (ConfigurationModel.MAIN_FILE, str),
            (ConfigurationModel.FROM, str),
            (ConfigurationModel.TO, list)
        ]

        # Do
        with self.assertRaises(WrongParameterTypeException):
            for key_conf_model in configuration_model:
                ConfigurationParser._check_configuration_type(configuration_dict, key_conf_model[0], key_conf_model[1])