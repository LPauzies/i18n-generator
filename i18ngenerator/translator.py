from i18ngenerator.languages import CHINESE_LANGUAGES, CYRILLIC_LANGUAGES, GERMAN_LANGUAGES, JAPONIC_LANGUAGES, KOREANIC_LANGUAGES, LATIN_LANGUAGES, Language
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
        try:
            if from_language in KOREANIC_LANGUAGES or to_language in KOREANIC_LANGUAGES:
                return translators.papago(
                    query_text=text,
                    from_language=Language.to_locale(from_language),
                    to_language=Language.to_locale(to_language),
                    if_ignore_limit_of_length=True
                )
            if from_language in CHINESE_LANGUAGES or to_language in CHINESE_LANGUAGES:
                return translators.iflytek(
                    query_text=text,
                    from_language=Language.to_locale(from_language),
                    to_language=Language.to_locale(to_language),
                    if_ignore_limit_of_length=True
                )
            if from_language in JAPONIC_LANGUAGES or to_language in JAPONIC_LANGUAGES:
                return translators.iciba(
                    query_text=text,
                    from_language=Language.to_locale(from_language),
                    to_language=Language.to_locale(to_language),
                    if_ignore_limit_of_length=True
                )
            if from_language in LATIN_LANGUAGES or \
                to_language in LATIN_LANGUAGES or \
                from_language in GERMAN_LANGUAGES or \
                to_language in GERMAN_LANGUAGES:
                return translators.bing(
                    query_text=text,
                    from_language=Language.to_locale(from_language),
                    to_language=Language.to_locale(to_language),
                    if_ignore_limit_of_length=True
                )
            if from_language in CYRILLIC_LANGUAGES or to_language in CYRILLIC_LANGUAGES:
                return translators.yandex(
                    query_text=text,
                    from_language=Language.to_locale(from_language),
                    to_language=Language.to_locale(to_language),
                    if_ignore_limit_of_length=True
                )
            # Default one
            return translators.google(
                query_text=text,
                from_language=Language.to_locale(from_language),
                to_language=Language.to_locale(to_language),
                if_ignore_limit_of_length=True
            )
        # If we catch exception then just use Google translate by default
        except Exception:
            return translators.google(
                query_text=text,
                from_language=Language.to_locale(from_language),
                to_language=Language.to_locale(to_language),
                if_ignore_limit_of_length=True
            )
