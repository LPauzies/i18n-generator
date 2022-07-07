from setuptools import setup, find_packages

# The requirements to build the package
requirements = [
    "translators==5.3.1",
    "unidecode==1.3.4",
    "nltk"
]

# Read from Readme.md for long description
with open("./README.md", "r", encoding="utf-8") as f:
    readme = f.read() 

# Setup the package
setup(
    name = "i18n-generator",
    version = "0.0.1",
    author = "Lucas Pauzies",
    author_email = "lucas.pauzies@hotmail.fr",
    maintainer = "Lucas Pauzies",
    maintainer_email = "lucas.pauzies@hotmail.fr",
    description = "Python package for i18n implementation and conversion",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/LPauzies/i18n-generator",
    packages = find_packages(
        exclude=["tests"]
    ),
    install_requires = requirements,
    setup_requires = ["pytest-runner", "flake8", "wheel"],
    tests_require = ["pytest"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.8"
)