# -*- coding: utf-8 -*-

import setuptools


with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='fold_to_ascii',
    version='1.0.2',
    description='A Python port of the Apache Lucene ASCII Folding Filter that converts alphabetic, numeric, and symbolic Unicode characters which are not in the first 127 ASCII characters (the ‘Basic Latin’ Unicode block) into ASCII equivalents, if they exist.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='William Bert',
    author_email='william@spanishdict.com',
    url='https://github.com/spanishdict/fold_to_ascii',
    license="MIT License",
    packages=setuptools.find_packages(exclude=('tests')),
    keywords="ascii unicode sanitize diacritics fold folding ligatures"
)
