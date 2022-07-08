import unittest

from i18ngenerator.languages import Language

class TestLanguage(unittest.TestCase):

    def test_from_locale_exists(self):
        # Given
        locale = "fr"

        # Expected
        expected_language = Language.FRENCH

        # Do
        self.assertEqual(expected_language, Language.from_locale(locale))