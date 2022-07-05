from typing import Dict, List
from i18ngenerator.languages import Language
import translators

class Translator:

    def translate(text: str, from_language: Language, to_language: Language) -> str:
        """Translate `text` written in `from_language` to `to_language`.

        Args:
            text (str): The text to translate
            from_language (Language): The language `text` is written
            to_language (Language): The target language

        Raises:
            TypeError: If `from_language` or `to_language` are not instance of `Language`

        Returns:
            str: The translated `text`
        """
        if not isinstance(from_language, Language):
            raise TypeError(f"Cannot use type {type(from_language)} for function. Use {Language} instead.")
        if not isinstance(to_language, Language): 
            raise TypeError(f"Cannot use type {type(to_language)} for function. Use {Language} instead.")
        return translators.google(query_text=text.strip(), from_language=Language.to_locale(from_language), to_language=Language.to_locale(to_language), if_ignore_limit_of_length=True)
        
    def batch_translate_list(text_list: List[str], from_language: Language, to_language: Language) -> List[str]:
        """Translate a batch of text `text_list` written in `from_language` to `to_language`.

        Args:
            text_list (List[str]): The batch of text to translate
            from_language (Language): The language `text` is written
            to_language (Language): The target language

        Returns:
            List[str]: The translated batch of text
        """
        return [Translator.translate(text=text.strip(), from_language=Language.to_locale(from_language), to_language=Language.to_locale(to_language)) for text in text_list]

    def batch_translate_dict(text_dict: Dict[str, str], from_language: Language, to_language: Language) -> Dict[str, str]:
        """Translate a batch of text `text_dict` written in `from_language` to `to_language`. Preserves the keys of the dictionnary.

        Args:
            text_list (Dict[str, str]): The batch of text to translate
            from_language (Language): The language `text` is written
            to_language (Language): The target language

        Returns:
            Dict[str, str]: The translated batch of text
        """
        return {key : Translator.translate(text=text.strip(), from_language=Language.to_locale(from_language), to_language=Language.to_locale(to_language)) for key, text in text_dict.items()}