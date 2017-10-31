# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fold_to_ascii',
    version='1.0.0',
    description='A Python port of the Apache Lucene ASCII Folding Filter that converts alphabetic, numeric, and symbolic Unicode characters which are not in the first 127 ASCII characters (the ‘Basic Latin’ Unicode block) into ASCII equivalents, if they exist.',
    long_description=readme,
    author='William Bert',
    author_email='william@spanishdict.com',
    url='https://github.com/spanishdict/fold_to_ascii',
    license=license,
    packages=find_packages(exclude=('tests'))
)
