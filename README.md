<p align="center">
    <img src=".assets/logo.png" alt="i18n-generator-logo" border="0" width="120">
</p>

# i18n Generator, a powerful library to easily internationalize projects

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build](https://github.com/LPauzies/i18n-generator/actions/workflows/build.yaml/badge.svg)](https://github.com/LPauzies/i18n-generator/actions/workflows/build.yaml)
[![Tests](https://github.com/LPauzies/i18n-generator/actions/workflows/tests.yaml/badge.svg)](https://github.com/LPauzies/i18n-generator/actions/workflows/tests.yaml)
[![PyPI version](https://badge.fury.io/py/i18n-generator.svg)](https://badge.fury.io/py/i18n-generator)
[![Coverage Status](https://coveralls.io/repos/github/LPauzies/i18n-generator/badge.svg?branch=master)](https://coveralls.io/github/LPauzies/i18n-generator?branch=master)
[![Downloads](https://pepy.tech/badge/i18n-generator)](https://pepy.tech/project/i18n-generator)

## What is it ?

**i18n-generator** is a Python package that provides a fast way to internationalize your app, based on your native language.

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
>>> from i18ngenerator.languages import Language
>>> list(Language)
>>> [<Language.ENGLISH: 'en'>, <Language.CHINESE: 'zh'>, <Language.FRENCH: 'fr'>, ...]
```

- Why is it sometimes slow to generate my translated files ?

This package is based on [translators](https://pypi.org/project/translators/) which is a free package and free to use. It is using Google translate API to make translation and sometimes, it is not instantly generated. The algorithm providing the translation then need to wait a bit for the translation.