#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = "is-alive-cli"
URL = "https://github.com/antonkravtsevich/is-alive-cli"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


def load_requirements(filename):
    with open(os.path.join(PROJECT_ROOT, filename), "r") as f:
        return f.read().splitlines()


def load_readme():
    readme_path = os.path.join(PROJECT_ROOT, "README.md")
    with io.open(readme_path, encoding="utf-8") as f:
        return "\n" + f.read()


setup(
    name=NAME,
    long_description=load_readme(),
    long_description_content_type="text/markdown",
    url=URL,
    download_url=URL,
    packages=find_packages(exclude=("tests", )),
    entry_points={
        "console_scripts": [
            "is-alive-cli=is_alive_cli.script:main",
        ],
    },
    install_requires=load_requirements("requirements.txt"),
    include_package_data=True,
)
