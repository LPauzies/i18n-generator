<p align="center">
    <img src="https://i.imgur.com/aBXsGkl.png" alt="i18n-generator-logo" border="0" width="120">
</p>

# i18n Generator, a powerful library to easily internationalize projects

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build](https://github.com/LPauzies/i18n-generator/actions/workflows/build.yaml/badge.svg)](https://github.com/LPauzies/i18n-generator/actions/workflows/build.yaml)
[![Tests](https://github.com/LPauzies/i18n-generator/actions/workflows/tests.yaml/badge.svg)](https://github.com/LPauzies/i18n-generator/actions/workflows/tests.yaml)
[![PyPI version](https://badge.fury.io/py/i18n-generator.svg)](https://badge.fury.io/py/i18n-generator)
[![Coverage Status](https://coveralls.io/repos/github/LPauzies/i18n-generator/badge.svg?branch=master)](https://coveralls.io/github/LPauzies/i18n-generator?branch=master)
[![Downloads](https://static.pepy.tech/personalized-badge/i18n-generator?period=total&units=international_system&left_color=blue&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/i18n-generator)

## What is it ?

**i18n-generator** is a Python package that provides a fast way to internationalize your app, based on your native language. 
Translation is done using these technologies depending of [language classification](https://en.wikipedia.org/wiki/List_of_language_families) :
- Koreanic : [Papago](https://papago.naver.com/)
- Chinese : [Iflytek](https://fanyi.xfyun.cn/console/trans/text)
- Japonic : [Iciba](https://www.iciba.com/fy)
- Latin : [Bing](https://www.bing.com/Translator)
- German : [Bing](https://www.bing.com/Translator)
- Cyrillic : [Google Translate](https://translate.google.com/)

For the rarest languages and by default if one service is not available : [Google Translate](https://translate.google.com/)

## Where to get it ?

The source code is currently hosted on GitHub at: https://github.com/LPauzies/i18n-generator

Binary installers for the latest released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/i18n-generator/).

```Bash
pip install i18n-generator
```

## How to use it
i18n-generator generates the translation from a native language to a list of other languages. To use it, you will need a `main.json` file that is containing a json document
### Command line
#### Help
```Bash
python -m i18ngenerator -h
```

#### Using configuration file
```Bash
python -m i18ngenerator --config config.yaml
```
With `config.yaml` :
```YAML
main-file: ~/main.json # Path to main file
from-language: fr # Should always be a short locale
to-language: # Should be a list of short locale
- en
- zh
- ru
- pt
```
You can find the list of i18n locales [here](https://www.science.co.il/language/Locale-codes.php). For France for example, the short locale would be "fr". For China, the short locale would be "zh".

#### Using CLI arguments
```Bash
# Example of use with CLI arguments
python -m i18ngenerator --main-file main.json --from-language fr --to-language es,zh,en
```
With `main.json` as main json file containing values to translate from french (fr) to spanish, chinese and english (es,zh,en)

### Python package
#### From JSON file

```Python
from i18ngenerator.i18ngenerator import I18nGenerator
from i18ngenerator.languages import Language
import pathlib

# Using json file
json_file = pathlib.Path("path/to/main.json")
from_language = Language.ENGLISH
to_language = [
    Language.FRENCH,
    Language.CHINESE
]

i18n_generator = I18nGenerator()
i18n_generator.generate_translation_from_json(json_file, from_language, to_language)
```
#### From Python dict
```Python
from i18ngenerator.i18ngenerator import I18nGenerator
from i18ngenerator.languages import Language

# Using dict object
json_dict = {"dummy_key_1": "Hello", "dummy_key_2": "I am Lucas ! I am 24 years old."}
from_language = Language.ENGLISH
to_language = Language.FRENCH

i18n_generator = I18nGenerator()
result = i18n_generator.generate_translation_from_dict(json_dict, from_language, to_language)
print(result)
>>> {"dummy_key_1": "Bonjour", "dummy_key_2": "Je suis Lucas! J'ai 24 ans."}
```

#### Just for translation
```Python
from i18ngenerator.translator import Translator
from i18ngenerator.languages import Language

text = "Bonjour, je suis Lucas."
from_language = Language.FRENCH
to_language = Language.ENGLISH
translated_text = Translator.translate_text(text, from_language, to_language)
print(translated_text)
>>> "Hello, I am Lucas."
```

## Dependencies
- [translators - Translators is a library which aims to bring free, multiple, enjoyable translation](https://pypi.org/project/translators/)
- [nltk - The Natural Language Toolkit (NLTK) is a Python package for natural language processing](https://pypi.org/project/nltk/)
- [pyyaml - YAML parser and emitter for Python](https://pypi.org/project/PyYAML/)

## Build from sources

Download the sources : [here](https://pypi.org/project/i18n-generator/#files)

```Bash
python setup.py install
```

## License
[GPLv3](https://github.com/LPauzies/i18n-generator/blob/master/LICENSE)

## How to contribute ?
[![Open Source Helpers](https://www.codetriage.com/lpauzies/i18n-generator/badges/users.svg)](https://www.codetriage.com/lpauzies/i18n-generator)

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

## FAQ & Troubleshooting

- Which languages can I use ?

You can consider using these lines of code to see which languages are supported by i18n-generator
```Python
from i18ngenerator.languages import Language

print(list(Language))
>>> [<Language.ENGLISH: 'en'>, <Language.CHINESE: 'zh'>, <Language.FRENCH: 'fr'>, ...]
```

- Why is it sometimes slow to generate my translated files ?

This package is based on [translators](https://pypi.org/project/translators/) which is a free package and free to use. It is using Google translate API to make translation and sometimes, it is not instantly generated. The algorithm providing the translation then need to wait a bit for the translation.