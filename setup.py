# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fold-to-ascii',
    version='1.0.0',
    description='A Python port of the Apache Lucene ASCII Folding Filter that converts alphabetic, numeric, and symbolic Unicode characters which are not in the first 127 ASCII characters (the ‘Basic Latin’ Unicode block) into a ASCII equivalents, if they exist.',
    long_description=readme,
    author='William Bert',
    author_email='william@spanishdict.com',
    url='https://github.com/spanishdict/fold-to-ascii',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
