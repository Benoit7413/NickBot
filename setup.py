#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'nickbot'
DESCRIPTION = 'Discord bot to manage Nicknames'
URL = 'https://github.com/Benoit7413/NickBot'
EMAIL = None
AUTHOR = 'Benoit7413'
REQUIRES_PYTHON = '>=3.5.2'
VERSION = None


REQUIRED = [
    'discord',
]

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['nickbot', 'nickbot.classes'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='GNU',
    entry_points={
        'console_scripts': [
            'nickbot = nickbot:main'
        ]
    }
)
