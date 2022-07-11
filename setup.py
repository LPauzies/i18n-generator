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
    version = "0.0.1",
    author = "Lucas Pauzies",
    author_email = "lucas.pauzies@hotmail.fr",
    maintainer = "Lucas Pauzies",
    maintainer_email = "lucas.pauzies@hotmail.fr",
    description = "Python package for i18n implementation and locales generation",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/LPauzies/i18n-generator",
    packages = find_packages(
        exclude=["tests"]
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
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires = ">=3.8"
)