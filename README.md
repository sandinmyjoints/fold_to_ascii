# fold_to_ascii

A Python port of the [Apache Lucene ASCII Folding
Filter](https://lucene.apache.org/core/4_0_0/analyzers-common/org/apache/lucene/analysis/miscellaneous/ASCIIFoldingFilter.html)
that converts alphabetic, numeric, and symbolic Unicode characters which are not
in the first 127 ASCII characters (the "Basic Latin" Unicode block) into ASCII
equivalents, if they exist.

## Usage

``` python
> from fold_to_ascii import fold
> s = u'Astroturf® paté'
> fold(s)
u'Astroturf pate'
> fold(s, u'?')
u'Astroturf? pate'
```

## Differences from [JS fold-to-ascii](https://www.npmjs.com/package/fold-to-ascii)

This library **always** removes astral characters, even when a replacement
character is specified. PRs welcome if you want to fix this.

## Differences from unidecode

There are a few Python unidecode libraries out there
([1](https://pypi.python.org/pypi/text-unidecode),
[2](https://pypi.python.org/pypi/Unidecode/)). They are based on a Perl program
that makes some interesting choices about what to replace, for example, `£`
(`POUND SIGN`) is replaced with the string `PS`. Also, they do not allow
specifying a replacement character to use other than the empty string for
unmapped characters.

## Development environment

``` shell
$ virtualenv -p python3 ~/.local/venvs/fold_to_ascii
$ source ~/.local/venvs/fold_to_ascii/bin/activate
$ pip install -r requirements.txt
```

## Test

``` shell
$ make lint && make test
```

## Release

Requires a [pypi](https://pypi.org/) account.

1. Bump the version in setup.py.
1. Build and upload:

``` shell
$ rm dist/* && python setup.py sdist bdist_wheel
$ twine upload dist/*
```
