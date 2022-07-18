import pathlib
import json
from tqdm import tqdm
from typing import Dict, Any, Generator, Iterable, List, Union
from i18ngenerator.languages import Language
from i18ngenerator.transformer import Transformer
from i18ngenerator.translator import Translator
from i18ngenerator.utils.tqdm import infinite_generator


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
            if verbose: 
                print(f"Sucessfully translated from {Language.to_locale(from_language)} to {Language.to_locale(language)}")
            # Build path file using locale
            file_path = pathlib.Path(folder_to_generate_translation_files, f"{Language.to_locale(language)}.json")
            # Dump the dict to json file
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(translated_dictionnary, f, indent=4, ensure_ascii=False)
                if verbose: 
                    print(f"Sucessfully written translated file to {file_path}")

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
        with tqdm(infinite_generator()) as progress_bar:
            progress_bar.set_description_str(f"Currently translating from {Language.to_locale(from_language)} to {Language.to_locale(to_language)}")
            self._generate_translation_rec(result, json_data, from_language, to_language, progress_bar)
        return result

    def _generate_translation_rec(self, result: Union[List[Any], Dict[str, Any]], json_data: Union[List[Any], Dict[str, Any]], from_language: Language, to_language: Language, progress_bar: tqdm):
        """Recursively translate each string in dictionnary values.
        Keys will not be changed.
        Nested dictionnaries are managed.
        Nested lists are managed.

        How it works ?
        - When recursive call is done, `result` should have the same type as `json_data`.
        - Values inside `json_data` are copied to `result`.
        - Each string, that are not keys of JSON dict are translated.

        Args:
            result (Union[List[Any], Dict[str, Any]]): The result of the recursive procedure, as list or dict
            json_data (Union[List[Any], Dict[str, Any]]): The data as json to be translated, as list or dict
            from_language (Language): The language of `json_data` values
            to_language (Language): The target language to translate `json_data` values from
        """
        # If two instances of dict, it means we are in classic JSON Dict or Nested Dict
        if isinstance(result, dict) and isinstance(json_data, dict):
            for key in json_data:
                # If instance of string, we should translate it
                if isinstance(json_data[key], str):
                    s = json_data[key]
                    s = self.transformer.capitalize(s, from_language)
                    s = Translator.translate_text(s, from_language=from_language, to_language=to_language)
                    result[key] = s
                    progress_bar.update()
                # If instance of list, it means it can be List[str], List[List[Any]], List[Dict[str, Any]] or List[Any]
                elif isinstance(json_data[key], list):
                    result[key] = []
                    for element in json_data[key]:
                        if isinstance(element, str):
                            s = self.transformer.capitalize(element, from_language)
                            s = Translator.translate_text(s, from_language=from_language, to_language=to_language)
                            result[key].append(s)
                            progress_bar.update()
                        elif isinstance(element, list):
                            # Append new empty list and fill it recursively
                            result[key].append([])
                            # Translate it by reference in the new empty list created
                            self._generate_translation_rec(result[key][-1], element, from_language, to_language, progress_bar)
                        elif isinstance(element, dict):
                            # Append new empty dict and fill it recursively
                            result[key].append({})
                            # Translate it by reference in the new empty dict created
                            self._generate_translation_rec(result[key][-1], element, from_language, to_language, progress_bar)
                        else:
                            # If another instance like int, float and so on, do not disturb the value
                            result[key].append(element)
                            progress_bar.update()
                # If instance of dict, it means it is nested, we make a recursive call by reference
                elif isinstance(json_data[key], dict):
                    # Add new empty dict to known key and fill it recursively
                    result[key] = {}
                    # Translate it by reference in the new empty dict created
                    self._generate_translation_rec(result[key], json_data[key], from_language, to_language, progress_bar)
                # Else we do not distort the value
                else:
                    result[key] = json_data[key]
                    progress_bar.update()
        # If two instances of list, it means we are in classic JSON List or Nested List
        elif isinstance(result, list) and isinstance(json_data, list):
            for element in json_data:
                # If instance of string, we should translate it
                if isinstance(element, str):
                    s = self.transformer.capitalize(element, from_language)
                    s = Translator.translate_text(s, from_language=from_language, to_language=to_language)
                    result.append(s)
                    progress_bar.update()
                # If instance of list, it means it can be List[str], List[List[Any]], List[Dict[str, Any]] or List[Any]
                elif isinstance(element, list):
                    result.append([])
                    for nested_element in element:
                        if isinstance(nested_element, str):
                            s = self.transformer.capitalize(nested_element, from_language)
                            s = Translator.translate_text(s, from_language=from_language, to_language=to_language)
                            result[-1].append(s)
                            progress_bar.update()
                        elif isinstance(element, list):
                            # Append new empty list and fill it recursively
                            result[-1].append([])
                            # Translate it by reference in the new empty list created
                            self._generate_translation_rec(result[-1][-1], element, from_language, to_language, progress_bar)
                        elif isinstance(nested_element, dict):
                            # Append new empty dict and fill it recursively
                            result[-1].append({})
                            # Translate it by reference in the new empty dict created
                            self._generate_translation_rec(result[-1][-1], nested_element, from_language, to_language, progress_bar)
                        else:
                            # If another instance like int, float and so on, do not disturb the value
                            result[-1].append(nested_element)
                            progress_bar.update()
                # If instance of dict, it means it is nested, we make a recursive call by reference
                elif isinstance(element, dict):
                    # Add new empty dict to known key and fill it recursively
                    result.append({})
                    # Translate it by reference in the new empty dict created
                    self._generate_translation_rec(result[-1], element, from_language, to_language, progress_bar)
                # Else we do not distort the value
                else:
                    result.append(element)
                    progress_bar.update()
