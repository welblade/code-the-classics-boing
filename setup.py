# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Package meta-data.
NAME = 'boind'
DESCRIPTION = 'Boing - a Pong game like game'
URL = 'https://gitlab.com/dio-my-study-camp/code-the-classics/boing'
EMAIL = 'wellington.oliveira.dev@gmail.com'
AUTHOR = 'Wellington Oliveira'
REQUIRES_PYTHON = '>=3.10.0'
VERSION = '0.1.0'

# What packages are required for this module to be executed?
with open('requirements.txt') as f:
    REQUIRED = f.read().split("\n")

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url='URL',
    license=LICENSE,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    packages=find_packages(exclude=('tests'))
)