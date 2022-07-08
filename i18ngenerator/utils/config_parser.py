from dataclasses import dataclass
import pathlib
from typing import Any, Dict, List
from yaml import load, Loader

from i18ngenerator.utils.exceptions import WrongParameterTypeException, WrongExtensionException, FileNotFoundException
from i18ngenerator.languages import Language

class ConfigurationModel:
    """YAML model configuration for i18n generator"""
    MAIN_FILE = "main-file"
    FROM = "from-language"
    TO = "to-language"

    def format_help():
        s = ["\n"]
        s.append("YAML configuration file should be formatted as follow :")
        s.append("=== YAML file ===")
        s.append(f"{ConfigurationModel.MAIN_FILE}: locales/fr.json")
        s.append(f"{ConfigurationModel.FROM}: fr")
        s.append(f"{ConfigurationModel.TO}:")
        s.append("- en")
        s.append("- zh")
        s.append("- ru")
        s.append("- pt")
        s.append("=================")
        return "\n".join(s)

@dataclass
class Configuration:
    """DAO for i18n generator configuration"""
    main: pathlib.Path
    from_language: Language
    to_language: List[Language]

class ConfigurationParser:
    """Configuration parser for i18n generator. Can manage CLI or YAML file."""

    ACCEPTED_FORMAT = (".yaml", ".yml")

    def parse_from_yaml(path: pathlib.Path) -> Configuration:
        """Parse the YAML configuration file

        Args:
            path (str): The path to search for YAML configuration file

        Raises:
            WrongExtensionException: If the file extension is wrong
            WrongParameterTypeException: If the parameters in YAML file are from wrong type

        Returns:
            Configuration: The DAO representing Configuration
        """
        # Existence testing
        if not(path.exists() and path.is_file()):
            raise FileNotFoundException(path)

        # Format testing
        extension = path.suffix
        if extension not in ConfigurationParser.ACCEPTED_FORMAT:
            raise WrongExtensionException(extension, ConfigurationParser.ACCEPTED_FORMAT)

        # Load yaml file
        with open(path, "r", encoding="utf-8") as f:
            configuration = load(f, Loader=Loader)

            # Check type of values
            ConfigurationParser._check_configuration_type(configuration, ConfigurationModel.MAIN_FILE, str)
            ConfigurationParser._check_configuration_type(configuration, ConfigurationModel.FROM, str)
            ConfigurationParser._check_configuration_type(configuration, ConfigurationModel.TO, list)

            # Convert to cli formatted arguments
            main_file_ = pathlib.Path(configuration[ConfigurationModel.MAIN_FILE])
            from_language_ = configuration[ConfigurationModel.FROM]
            to_language_ = ",".join(configuration[ConfigurationModel.TO])

            # Re-use code =)
            return ConfigurationParser.parse_from_cli(
                main_file = main_file_,
                from_language = from_language_,
                to_language = to_language_
            )

    def parse_from_cli(main_file: pathlib.Path, from_language: str, to_language: str) -> Configuration:
        """Parse configuration from CLI arguments

        Args:
            main_file (pathlib.Path): The path of the main file
            from_language (str): The language of the main file
            to_language (str): The formatted string containing target languages to translate main_file to. Example: fr,es,zh.

        Raises:
            FileNotFoundException: If main file path does not exist

        Returns:
            Configuration: The DAO representing Configuration
        """
        
        if not(main_file.exists() and main_file.is_file()):
            raise FileNotFoundException(main_file)
        
        # Parse to-language CLI argument
        to_language_ = to_language.split(",") # Should be "fr,en,zh"

        # Convert to languages
        from_language_ = Language.from_locale(from_language)
        to_language_ = list(map(lambda lang: Language.from_locale(lang), to_language_))

        return Configuration(
            main = main_file,
            from_language = from_language_,
            to_language = to_language_
        )

    def _check_configuration_type(configuration_dict: Dict[str, Any], configuration_model_key: str, expected_type: type):
        """Check the types of values mapped to keys in YAML configuration file

        Args:
            configuration_dict (Dict[str, Any]): The configuration file as Dict[str, Any]
            configuration_model_key (str): The YAML key in model of the configuration file
            expected_type (type): The expected type for the mapped value to YAML key

        Raises:
            WrongParameterTypeException: If the parameter for YAML key is wrong
        """
        if not isinstance(configuration_dict[configuration_model_key], expected_type):
            raise WrongParameterTypeException(
                configuration_model_key,
                type(configuration_dict[configuration_model_key]),
                expected_type
            )