#!/usr/bin/env python

import imp
import sys

from setuptools import setup, find_packages

VERSION = imp.load_source("", "plotly_helper/version.py").__version__

setup(
    name="plotly-helper",
    author="BlueBrain NSE",
    author_email="bbp-ou-nse@groupes.epfl.ch",
    version=VERSION,
    description="Package that makes plotly easy",
    url="https://bbpteam.epfl.ch/project/issues/projects/NSETM/issues",
    download_url="ssh://bbpcode.epfl.ch/nse/plotly-helper",
    license="BBP-internal-confidential",
    install_requires=[
        'plotly>=3.4.2',
        'numpy>=1.15.4',
        'neurom>=1.4.13',
        'six>=1.12.0',
        'click>=6.0',
    ],
    entry_points={
        'console_scripts': ['viewer=plotly_helper.cli:cli']
    },
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
