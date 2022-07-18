from typing import Any, Dict
import unittest
import pathlib
import json

from tqdm import tqdm

from i18ngenerator.i18ngenerator import I18nGenerator
from i18ngenerator.languages import Language
from i18ngenerator.utils.tqdm import infinite_generator

def from_json(file_path: pathlib.Path) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


class TestI18NGenerator(unittest.TestCase):
    
    def test_generate_translation_from_dict(self):
        # Given
        test_json = from_json(pathlib.Path("tests/data/fr_test_case.json"))
        i18n_generator = I18nGenerator()

        # Expected
        expected_json = from_json(pathlib.Path("tests/data/en_test_case.json"))

        # Do
        tested_json = i18n_generator.generate_translation_from_dict(test_json, Language.FRENCH, Language.ENGLISH)
        self.assertEqual(expected_json, tested_json)
        self.assertEqual(expected_json.keys(), tested_json.keys())

    def test__generate_translation_rec(self):
        # Given
        test_json = from_json(pathlib.Path("tests/data/fr_test_case.json"))
        i18n_generator = I18nGenerator()

        # Expected
        expected_json = from_json(pathlib.Path("tests/data/en_test_case.json"))

        # Do
        tested_result = {}
        with tqdm(infinite_generator()) as progress_bar:
            i18n_generator._generate_translation_rec(tested_result, test_json, Language.FRENCH, Language.ENGLISH, progress_bar)
            self.assertEqual(expected_json, tested_result)
            self.assertEqual(expected_json.keys(), tested_result.keys())