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
    
    def test_main_blank_args(self):
        # Given
        # Nothing

        # Expected
        # Raise SystemExit

        # Do
        with self.assertRaises(SystemExit):
            main()
