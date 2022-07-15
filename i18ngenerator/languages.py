from enum import Enum

from i18ngenerator.utils.exceptions import WrongLocaleException

# Define the type
Language = "Language"


class Language(Enum):
    ENGLISH = "en"
    CHINESE = "zh"
    ARABIC = "ar"
    RUSSIAN = "ru"
    FRENCH = "fr"
    GERMAN = "de"
    SPANISH = "es"
    PORTUGUESE = "pt"
    ITALIAN = "it"
    JAPANESE = "ja"
    KOREAN = "ko"
    GREEK = "el"
    DUTCH = "nl"
    HINDI = "hi"
    TURKISH = "tr"
    MALAY = "ms"
    THAI = "th"
    VIETNAMESE = "vi"
    INDONESIAN = "id"
    POLISH = "pl"
    MONGOLIAN = "mn"
    CZECH = "cs"
    HUNGARIAN = "hu"
    ESTONIAN = "et"
    BULGARIAN = "bg"
    DANISH = "da"
    FINNISH = "fi"
    ROMANIAN = "ro"
    SWEDISH = "sv"
    SLOVENIAN = "sl"
    PERSIAN = "fa"
    FARSI = "fa"
    BOSNIAN = "bs"
    SERBIAN = "sr"
    FILIPINO = "tl"
    HAITIAN = "ht"
    CATALAN = "ca"
    CROATIAN = "hr"
    LATVIAN = "lv"
    LITHUANIAN = "lt"
    URDU = "ur"
    UKRAINIAN = "uk"
    WELSH = "cy"
    SWAHILI = "sw"
    SAMOAN = "sm"
    SLOVAK = "sk"
    AFRIKAANS = "af"
    NORWEGIAN = "no"
    BENGALI = "bn"
    MALAGASY = "mg"
    MALTESE = "mt"
    GUJARATI = "gu"
    TAMIL = "ta"
    TELUGU = "te"
    PUNJABI = "pa"
    AMHARIC = "am"
    AZERBAIJANI = "az"
    BELARUSIAN = "be"
    CEBUANO = "ceb"
    ESPERANTO = "eo"
    BASQUE = "eu"
    IRISH = "ga"

    def from_locale(locale: str) -> Language:
        for language in list(Language):
            if locale == Language.to_locale(language): 
                return language
        raise WrongLocaleException(wrong_locale=locale)

    def to_locale(language: Language) -> str:
        return language.value


# Define groups of languages
KOREANIC_LANGUAGES = [
    Language.KOREAN
]

CHINESE_LANGUAGES = [
    Language.CHINESE
]

JAPONIC_LANGUAGES = [
    Language.JAPANESE
]

LATIN_LANGUAGES = [
    Language.FRENCH,
    Language.SPANISH,
    Language.PORTUGUESE,
    Language.ROMANIAN,
    Language.CATALAN,
    Language.ITALIAN,
    Language.BASQUE
]

GERMAN_LANGUAGES = [
    Language.DUTCH,
    Language.ENGLISH,
    Language.SWEDISH,
    Language.NORWEGIAN,
    Language.GERMAN,
    Language.DANISH,
    Language.AFRIKAANS
]

CYRILLIC_LANGUAGES = [
    Language.RUSSIAN,
    Language.BELARUSIAN,
    Language.BULGARIAN,
    Language.SERBIAN,
    Language.CZECH,
    Language.UKRAINIAN,
    Language.POLISH,
    Language.CROATIAN
]
