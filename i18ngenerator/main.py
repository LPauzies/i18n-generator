import argparse
from i18ngenerator.translator import Translator
from i18ngenerator.transformer import Transformer
from i18ngenerator.languages import Language
from utils.config_parser import ConfigurationParser

print(ConfigurationParser.parse("i18n-generator.yaml"))