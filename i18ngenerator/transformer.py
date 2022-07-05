import unidecode
import nltk

class Transformer():

    def __init__(self) -> None:
        nltk.download("punkt", quiet=True) # To use tokenization

    def strip_accents(self, text: str) -> str:
        return unidecode.unidecode(text)

    def capitalize(self, text: str) -> str:
        sentences = nltk.tokenize.sent_tokenize(text)
        sentences = list(map(lambda s: f"{s[0].upper()}{s[1:]}", sentences))
        return " ".join(sentences)