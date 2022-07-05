class I18nGeneratorException(Exception):
    """Base class for other exceptions in i18n generator application"""
    pass

class WrongLocaleException(I18nGeneratorException):
    """Exception for wrong locale utilization"""

    def __init__(self, wrong_locale: str) -> None:
        super().__init__(f"Locale {wrong_locale} is wrong, cannot map it to the associated language.")