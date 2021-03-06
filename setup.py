# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="data-distributer",
    version="0.1.0",
    description="A pip package",
    license="MIT",
    author="shin-kinoshita",
    packages=find_packages(),
    install_requires=["ConfigParser",
                      "docopt",
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ],
    scripts=[
        'scripts/dist',
        'scripts/lncopy',
        'scripts/mkconfig',
    ]
)
