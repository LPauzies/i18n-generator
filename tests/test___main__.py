from i18ngenerator.__main__ import main
import unittest

from i18ngenerator.utils.exceptions import MissingParameterException

class TestMain(unittest.TestCase):

    def test_main_without_correct_args(self):
        # Given
        command = ["--from-language", "fr"]

        # Expected
        # Raise MissingParameterException

        # Do
        with self.assertRaises(MissingParameterException):
            main(args=command)

    def test_main_with_blank_args(self):
        # Given
        command = []

        # Expected
        # Raise MissingParameterException

        # Do
        with self.assertRaises(MissingParameterException):
            main(args=command)
    
    def test_main_version_information(self):
        # Given
        commands = [
            ["-i"], ["--info"], 
            ["-v"], ["--version"]
        ]

        # Expected
        # Raise SystemExit

        # Do
        for command in commands:
            with self.assertRaises(SystemExit):
                main(args=command)
