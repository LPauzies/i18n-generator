import unittest

from i18ngenerator.languages import Language
from i18ngenerator.utils.exceptions import WrongLocaleException

class TestLanguage(unittest.TestCase):

    def test_from_locale_exists(self):
        # Given
        locales = map(lambda lang: Language.to_locale(lang), list(Language))

        # Expected
        expected_languages = list(Language)

        # Do
        for locale, expected_language in zip(locales, expected_languages):
            self.assertEqual(expected_language, Language.from_locale(locale))

    def test_from_locale_not_exists(self):
        # Given
        locales_not_supported = ["ba", "tlh", "otq", "cv", "emj"]

        # Expected
        # Raise WrongLocaleException

        # Do
        with self.assertRaises(WrongLocaleException):
            for locale in locales_not_supported:
                Language.from_locale(locale)

    def test_to_locale(self):
        # Given
        languages = list(Language)

        # Expected
        expected_locales = map(lambda lang: Language.to_locale(lang), list(Language))

        # Do
        for language, expected_locale in zip(languages, expected_locales):
            self.assertEqual(expected_locale, Language.to_locale(language))
