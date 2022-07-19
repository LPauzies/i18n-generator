import contextlib
import io
from typing import Any, Dict
import unittest
import pathlib
import json


from i18ngenerator.i18ngenerator import I18nGenerator
from i18ngenerator.languages import Language

def from_json(file_path: pathlib.Path) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

PATH_FR_TEST = pathlib.Path("tests/data/fr_test_case.json")
PATH_EN_EXPECTED = pathlib.Path("tests/data/en_test_case.json")
ITEM_COUNT = 32


class TestI18NGenerator(unittest.TestCase):
    
    def test_generate_translation_from_dict(self):
        # Given
        test_json = from_json(PATH_FR_TEST)
        i18n_generator = I18nGenerator()
        from_language = Language.FRENCH
        to_language = Language.ENGLISH
        
        # Expected
        expected_json = from_json(PATH_EN_EXPECTED)

        # Do
        with io.StringIO() as buffer_stdout:
            with contextlib.redirect_stdout(buffer_stdout):
                tested_json = i18n_generator.generate_translation_from_dict(test_json, from_language, to_language)
                self.assertEqual(expected_json, tested_json)
                self.assertEqual(expected_json.keys(), tested_json.keys())
            self.assertIn(f"Currently translating from {Language.to_locale(from_language)} to {Language.to_locale(to_language)}...", buffer_stdout.getvalue())
            self.assertIn(f"Successfully translated {ITEM_COUNT} items.", buffer_stdout.getvalue())

    def test__generate_translation_rec(self):
        # Given
        test_json = from_json(PATH_FR_TEST)
        i18n_generator = I18nGenerator()

        # Expected
        expected_json = from_json(PATH_EN_EXPECTED)

        # Do
        tested_result = {}
        tested_metadata_method = {"translated_item_count": 0}
        i18n_generator._generate_translation_rec(tested_result, test_json, Language.FRENCH, Language.ENGLISH, tested_metadata_method)
        self.assertEqual(expected_json, tested_result)
        self.assertEqual(ITEM_COUNT, tested_metadata_method["translated_item_count"])