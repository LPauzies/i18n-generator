import unidecode
import nltk

class Transformer:

    def __init__(self) -> None:
        """Initialize needed files for ntlk use (grammar, tokenization, ...)"""
        # Tokenization
        nltk.download("punkt", quiet=True)

    def strip_accents(self, text: str) -> str:
        """Strip accents in `text` and replace by nearest character

        Args:
            text (str): The text to strip the accents in

        Returns:
            str: The accent stripped string
        """
        return unidecode.unidecode(text)

    def capitalize(self, text: str) -> str:
        """Capitalize each sentence in `text`

        Args:
            text (str): The text to capitalize sentences in

        Returns:
            str: The capitalized sentences of the `text`
        """
        sentences = nltk.tokenize.sent_tokenize(text)
        sentences = list(map(lambda s: f"{s[0].upper()}{s[1:]}", sentences))
        return " ".join(sentences)