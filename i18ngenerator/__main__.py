import pathlib
from typing import List, Optional
from i18ngenerator.i18ngenerator import I18nGenerator
from i18ngenerator.utils.config_parser import ConfigurationModel
from argparse import RawTextHelpFormatter, ArgumentParser
from i18ngenerator.utils.exceptions import MissingParameterException
from i18ngenerator.utils.config_parser import ConfigurationParser


def argument_parser() -> ArgumentParser:
    """Declare argument parser for i18ngenerator

    Returns:
        ArgumentParser: The argument parser for i18ngenerator
    """
    parser = ArgumentParser(
        prog="i18n generator",
        description="i18n implementation to help generate automatically translated files based on main language",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        "--config",
        dest="config_file",
        action="store",
        help=f"Target the YAML configuration file. {ConfigurationModel.format_help()}",
        type=pathlib.Path
    )
    parser.add_argument(
        "--main-file",
        dest="main_file",
        action="store",
        help="Main file that will be use as base for translation. Example: locales/fr.json. Considered only if argument '--config' is not used.",
        type=pathlib.Path
    )
    parser.add_argument(
        "--from-language",
        dest="from_language",
        action="store",
        help="Language of the main file. Example: en. Considered only if argument '--config' is not used.",
        type=str
    )
    parser.add_argument(
        "--to-language",
        dest="to_language",
        action="store",
        help="Languages to translate main file to, formatted as '<locale1>,<locale2>,<locale3>,...'. Example: fr,es,zh. Considered only if argument '--config' is not used.",
        type=str
    )
    return parser

def main(args: Optional[List[str]] = None, verbose: bool = True) -> None:
    """Main function to be used from CLI directly.

    Example : `python -m i18ngenerator --config <YAML FILE>`

    Args:
        args (Optional[List[str]], optional): The args to be defined for CLI use. Defaults to None.

    Raises:
        MissingParameterException: If CLI miss some mandatory parameters.
    """
    parser = argument_parser()
    args = parser.parse_args(args)
    # Retrieve configuration from
    if args.config_file:
        configuration = ConfigurationParser.parse_from_yaml(args.config_file)
    elif args.main_file and args.from_language and args.to_language:
        configuration = ConfigurationParser.parse_from_cli(args.main_file, args.from_language, args.to_language)
    else:
        raise MissingParameterException()
    # i18n generator
    i18n_generator = I18nGenerator()
    i18n_generator.generate_translation_from_json(configuration.main, configuration.from_language, configuration.to_language, verbose)


# Entry point when package is use as CLI
if __name__ == "__main__":
    main()
