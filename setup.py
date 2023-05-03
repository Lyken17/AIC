#!/usr/bin/env python
import os, sys
import shutil
import datetime

from setuptools import setup, find_packages
from setuptools.command.install import install

VERSION = "0.0.1"

# requirements = [
#     "PyInquirer",
#     "Markdown",
#     "openai",
# ]

requirements = open("requirements.txt").read().splitlines()

VERSION += "_" + datetime.datetime.now().strftime("%Y%m%d%H%M")[2:]
print(VERSION)

setup(
    # Metadata
    name="aic",
    version=VERSION,
    # author="Ligeng Zhu",
    # author_email="ligeng.zhu+github@gmail.com",
    entry_points={
        "console_scripts": ["aic = aic.aic_gen:main"],
    },
    # description="",
    # long_description_content_type="text/markdown",
    # license="MIT",
    # Package info
    # packages=find_packages(exclude=("*test*",)),
    #
    # zip_safe=True,
    install_requires=requirements,
    # Classifiers
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    # ],
)
