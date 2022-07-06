from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setup(
    name="i18n-generator",
    version="0.0.1",
    description='Python package for i18n implementation and conversion',
    author='Lucas Pauzies',
    author_email='lucas.pauzies@hotmail.fr',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=find_packages(
        where="i18generator", 
        exclude=["tests"]
    ),
    install_requires=requirements,
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
)