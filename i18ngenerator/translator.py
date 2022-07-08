from typing import Dict, List
from i18ngenerator.languages import Language
import translators

class Translator:

    def translate_text(text: str, from_language: Language, to_language: Language) -> str:
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