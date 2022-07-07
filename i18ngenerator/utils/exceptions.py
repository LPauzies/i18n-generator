from typing import Iterable


class I18nGeneratorException(Exception):
    """Base class for other exceptions in i18n generator application"""
    pass

class WrongLocaleException(I18nGeneratorException):
    """Exception for wrong locale utilization"""

    def __init__(self, wrong_locale: str) -> None:
        super().__init__(f"Locale {wrong_locale} is wrong, cannot map it to the associated language.")

### Configuration parsing exception
class WrongParameterTypeException(I18nGeneratorException):
    """Exception for wrong parameter use in YAML file"""

    def __init__(self, yaml_key: str, wrong_type: type, expected_type: type) -> None:
        super().__init__(f"Key {yaml_key} has not right value type {wrong_type}, expected {expected_type}")

class WrongExtensionException(I18nGeneratorException):
    """Exception for wrong format for configuration file"""

    def __init__(self, wrong_format: str, target_format: Iterable[str]) -> None:
        super().__init__(f"Format {wrong_format} not valid for this configuration file, expected in {target_format}")