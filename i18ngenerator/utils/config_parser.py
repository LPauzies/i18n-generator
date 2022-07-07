from dataclasses import dataclass
from typing import List
from yaml import load, Loader
import os

from utils.exceptions import WrongParameterTypeException, WrongExtensionException
from i18ngenerator.languages import Language

class ConfigurationModel:
    MAIN_FILE = "main-file"
    FROM = "from-language"
    TO = "to-language"

@dataclass
class Configuration:
    """DAO for i18n generator configuration"""
    main: str
    from_language: Language
    to_language: List[Language]

class ConfigurationParser:

    ACCEPTED_FORMAT = (".yaml", ".yml")

    def parse(path: str) -> Configuration:
        
        # Format testing
        _, extension = os.path.splitext(path)
        if extension not in ConfigurationParser.ACCEPTED_FORMAT:
            raise WrongExtensionException(extension, ConfigurationParser.ACCEPTED_FORMAT)

        # Load yaml file
        with open(path, "r", encoding="utf-8") as f:
            configuration = load(f, Loader=Loader)

            # Check type of values
            if not isinstance(configuration[ConfigurationModel.MAIN_FILE], str):
                raise WrongParameterTypeException(
                    ConfigurationModel.MAIN_FILE, 
                    type(configuration[ConfigurationModel.MAIN_FILE]),
                    str
                )
            if not isinstance(configuration[ConfigurationModel.FROM], str):
                raise WrongParameterTypeException(
                    ConfigurationModel.FROM, 
                    type(configuration[ConfigurationModel.FROM]),
                    str
                )
            if not isinstance(configuration[ConfigurationModel.TO], list):
                raise WrongParameterTypeException(
                    ConfigurationModel.TO, 
                    type(configuration[ConfigurationModel.TO]),
                    list
                )

            # Convert to languages
            from_language = Language.from_locale(configuration[ConfigurationModel.FROM])
            to_language = list(map(lambda lang: Language.from_locale(lang), configuration[ConfigurationModel.TO]))

            return Configuration(
                main = configuration[ConfigurationModel.MAIN_FILE],
                from_language = from_language,
                to_language = to_language
            )