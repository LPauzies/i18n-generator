from typing import Any, Dict
import unittest
import pathlib
import json

from i18ngenerator.__main__ import main

EXPECTED_LOCALES_PATH = pathlib.Path("tests_e2e/expected-test-locales/")
TEST_LOCALES_PATH = pathlib.Path("tests_e2e/test-locales/")
MAIN_LOCALES_FILE = pathlib.Path(TEST_LOCALES_PATH, "fr.json")

def clean_test_folder_at_the_end(func):
    def wrapper_clean_test_folder_at_the_end(*args, **kwargs):
        func(*args, **kwargs)
        for file_ in TEST_LOCALES_PATH.iterdir():
            if MAIN_LOCALES_FILE != file_: file_.unlink()
    return wrapper_clean_test_folder_at_the_end

def from_json(file_path: pathlib.Path) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

class TestE2E(unittest.TestCase):

    @clean_test_folder_at_the_end
    def test_translation_fr_to_en_from_cli(self):
        locales = ["en"]
        main(args=["--main-file", str(MAIN_LOCALES_FILE), "--from-language", "fr", "--to-language", "en"])
        for locale in locales:
            expected = pathlib.Path(EXPECTED_LOCALES_PATH, f"{locale}.json")
            tested = pathlib.Path(TEST_LOCALES_PATH, f"{locale}.json")
            self.assertEqual(from_json(expected), from_json(tested))

    @clean_test_folder_at_the_end
    def test_translation_fr_to_en_zh_ru_pt_from_yaml(self):
        locales = ["en", "zh", "ru", "pt"]
        main(args=["--config", "tests_e2e/test_e2e.yaml"])
        for locale in locales:
            expected = pathlib.Path(EXPECTED_LOCALES_PATH, f"{locale}.json")
            tested = pathlib.Path(TEST_LOCALES_PATH, f"{locale}.json")
            self.assertEqual(from_json(expected), from_json(tested))

    @clean_test_folder_at_the_end
    def test_translation_fr_to_en_zh_ru_pt_from_cli(self):
        locales = ["en", "zh", "ru", "pt"]
        main(args=["--main-file", str(MAIN_LOCALES_FILE), "--from-language", "fr", "--to-language", "en,zh,ru,pt"])
        for locale in locales:
            expected = pathlib.Path(EXPECTED_LOCALES_PATH, f"{locale}.json")
            tested = pathlib.Path(TEST_LOCALES_PATH, f"{locale}.json")
            self.assertEqual(from_json(expected), from_json(tested))

