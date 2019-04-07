#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas']

setup_requirements = ['pandas', 'pyensembl']

setup(
    author="Gokcen Eraslan",
    author_email='geraslan@broadinstitute.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python package for conversions between ENSEMBL IDs and gene names (annotables + pyensembl)",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyannotables',
    name='pyannotables',
    packages=find_packages(),
    package_data={'': ['datafile_*']},
    setup_requires=setup_requirements,
    url='https://github.com/gokceneraslan/pyannotables',
    version='0.1.0',
    zip_safe=False,
)
