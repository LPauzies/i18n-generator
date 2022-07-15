from typing import Any, Dict
import unittest
import pytest
import pathlib
import json

from i18ngenerator.__main__ import main
from i18ngenerator.utils.metadata import VERSION

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

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    @clean_test_folder_at_the_end
    def test_translation_fr_to_en_from_cli(self):
        locales = ["en"]
        main(args=["--main-file", str(MAIN_LOCALES_FILE), "--from-language", "fr", "--to-language", "en"])
        for locale in locales:
            expected = pathlib.Path(EXPECTED_LOCALES_PATH, f"{locale}.json")
            tested = pathlib.Path(TEST_LOCALES_PATH, f"{locale}.json")
            self.assertTrue(tested.exists())
            self.assertEqual(from_json(expected).keys(), from_json(tested).keys())

    @clean_test_folder_at_the_end
    def test_translation_fr_to_en_ru_pt_ko_zh_ja_from_yaml(self):
        locales = ["en", "ru", "pt", "ko", "zh", "ja"]
        main(args=["--config", "tests_e2e/test_e2e.yaml"])
        for locale in locales:
            expected = pathlib.Path(EXPECTED_LOCALES_PATH, f"{locale}.json")
            tested = pathlib.Path(TEST_LOCALES_PATH, f"{locale}.json")
            self.assertTrue(tested.exists())
            self.assertEqual(from_json(expected).keys(), from_json(tested).keys())

    @clean_test_folder_at_the_end
    def test_translation_fr_to_en_ru_pt_from_cli(self):
        locales = ["en", "ru", "pt", "ko", "zh", "ja"]
        main(args=["--main-file", str(MAIN_LOCALES_FILE), "--from-language", "fr", "--to-language", "en,ru,pt,ko,zh,ja"])
        for locale in locales:
            expected = pathlib.Path(EXPECTED_LOCALES_PATH, f"{locale}.json")
            tested = pathlib.Path(TEST_LOCALES_PATH, f"{locale}.json")
            self.assertTrue(tested.exists())
            self.assertEqual(from_json(expected).keys(), from_json(tested).keys())

    def test_version_system_exit(self):
        with self.assertRaises(SystemExit) as mocked_exception:
            main(args=["-v"])
        self.assertEqual(mocked_exception.exception.code, 0)
        self.assertIn(VERSION, self.capsys.readouterr().out)
