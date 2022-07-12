from setuptools import setup, find_packages

# The requirements to build the package
requirements = [
    "translators==5.3.1",
    "nltk>=3.7",
    "pyyaml==6.0"
]

# Read from Readme.md for long description
with open("./README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Setup the package
setup(
    name = "i18n-generator",
    version = "1.0.0",
    author = "Lucas Pauzies",
    author_email = "lucas.pauzies@hotmail.fr",
    maintainer = "Lucas Pauzies",
    maintainer_email = "lucas.pauzies@hotmail.fr",
    description = "Python package for i18n implementation and locales generation",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/LPauzies/i18n-generator",
    download_url = "https://pypi.org/project/i18n-generator/",
    project_urls = {
        'Documentation': 'https://github.com/LPauzies/i18n-generator/blob/master/README.md',
        'License': 'https://github.com/LPauzies/i18n-generator/blob/master/LICENSE',
        'CI': 'https://github.com/LPauzies/i18n-generator/actions',
        'Bug Tracker': 'https://github.com/LPauzies/i18n-generator/issues',
        'Source Code': "https://github.com/LPauzies/i18n-generator",
        'Funding': 'https://www.paypal.com/donate/?hosted_button_id=RDDVL7Y5T8MJJ'
    },
    packages = find_packages(
        exclude=["tests", "tests_e2e"]
    ),
    install_requires = requirements,
    setup_requires = ["pytest-runner", "flake8", "wheel", "twine"],
    tests_require = ["pytest"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires = ">=3.8"
)