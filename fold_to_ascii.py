# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import defaultdict

mapped_characters = [
    (u'á', u'a')
]

mapped_characters_ord = [(ord(k), v) for (k, v) in mapped_characters]

def none_factory():
    return None

default_translate_table = defaultdict(none_factory, mapped_characters_ord)

def fold(unicode_string, replacement=u''):
    """Fold unicode_string to ASCII.

Unmapped characters should be replaced with empty string by default, or other
replacement if provided.

All astral plane characters are always removed, even if a replacement is
provided.
    """

    if type(unicode_string) != unicode:
        raise TypeError('cannot fold bytestring')

    if type(replacement) != unicode:
        raise TypeError('cannot replace using bytestring')

    if replacement:
        def replacer():
            return replacement
        translate_table = defaultdict(replacer, mapped_characters_ord)
    else:
        translate_table = default_translate_table

    return unicode_string.translate(translate_table)
