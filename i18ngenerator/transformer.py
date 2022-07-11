import nltk

from i18ngenerator.languages import Language


class Transformer:

    def __init__(self) -> None:
        """Initialize needed files for ntlk use (grammar, tokenization, ...)"""
        # Tokenization
        nltk.download("punkt", quiet=True)

    def capitalize(self, text: str, language: Language) -> str:
        """Capitalize each sentence in `text`

        Args:
            text (str): The text to capitalize sentences in

        Returns:
            str: The capitalized sentences of the `text`
        """
        not_capitalizable_languages = [
            Language.CHINESE,
            Language.ARABIC,
            Language.KOREAN,
            Language.JAPANESE,
            Language.HINDI,
            Language.BENGALI,
            Language.TAMIL,
            Language.GUJARATI,
            Language.THAI,
            Language.PUNJABI
        ]
        if language in not_capitalizable_languages:
            return text
        sentences = nltk.tokenize.sent_tokenize(text)
        sentences = list(map(lambda s: f"{s[0].upper()}{s[1:]}", sentences))
        return " ".join(sentences)
