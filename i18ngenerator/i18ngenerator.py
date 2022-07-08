import pathlib
import json
from typing import Dict, Any, List
from i18ngenerator.languages import Language
from i18ngenerator.transformer import Transformer
from i18ngenerator.translator import Translator


class I18nGenerator:
    """Main class of i18n generator"""

    def __init__(self) -> None:
        self.transformer = Transformer()

    def generate_translation_from_json(self, json_file: pathlib.Path, from_language: Language, to_language: List[Language], verbose: bool = False) -> None:
        """Generate the translation from `json_file` recursively, from language `from_language` to each language of `to_language`.

        Write the generated files under the same level of `json_file`.

        Args:
            json_file (pathlib.Path): The main json to internationalize using i18n implementation
            from_language (Language): The starting language of `json_file` file
            to_language (List[Language]): The list of languages to translate `json_file` to
        """
        # Build folder path where we want to save new files
        folder_to_generate_translation_files = pathlib.Path(json_file.cwd(), json_file.parent)
        # Load data from main json file
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        # For each language make the translation recursively
        for language in to_language:
            translated_dictionnary = self.generate_translation_from_dict(data, from_language, language)
            if verbose: print(f"Sucessfully translated from {Language.to_locale(from_language)} to {Language.to_locale(language)}")
            # Build path file using locale
            file_path = pathlib.Path(folder_to_generate_translation_files, f"{Language.to_locale(language)}.json")
            # Dump the dict to json file
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(translated_dictionnary, f, indent=4, ensure_ascii=False)
                if verbose: print(f"Sucessfully written translated file to {file_path}")

    def generate_translation_from_dict(self, json_data: Dict[str, Any], from_language: Language, to_language: Language) -> Dict[str, Any]:
        """Generate translation wrapping the main recursive function `I18nGenerator._generate_translation_rec`.

        Args:
            json_data (Dict[str, Any]): The data as json to be translated
            from_language (Language): The language of `json_data` values
            to_language (Language): The target language to translate `json_data` values from

        Returns:
            Dict[str, Any]: The `json_data` with string values translated to `to_language`
        """
        result = {}
        self._generate_translation_rec(result, json_data, from_language, to_language)
        return result

    def _generate_translation_rec(self, result: Dict[str, any], json_data: Dict[str, Any], from_language: Language, to_language: Language):
        """Recursively translate each string in dictionnary values.

        Keys will not be changed.
        
        Nested dictionnary is managed.

        Args:
            result (Dict[str, any]): The result of the recursive procedure
            json_data (Dict[str, Any]): The data as json to be translated
            from_language (Language): The language of `json_data` values
            to_language (Language): The target language to translate `json_data` values from
        """
        for key in json_data:
            # If instance of string, we should translate it
            if isinstance(json_data[key], str):
                s = json_data[key]
                s = self.transformer.strip_accents(s)
                s = self.transformer.capitalize(s)
                s = Translator.translate_text(s, from_language=from_language, to_language=to_language)
                result[key] = s
            # If instance of dict, it means it is nested, we make a recursive call by reference
            elif isinstance(json_data[key], dict):
                result[key] = {}
                self._generate_translation_rec(result[key], json_data[key], from_language, to_language)
            # Else we do not distort the value
            else:
                result[key] = json_data[key]
