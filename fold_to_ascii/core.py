# -*- coding: utf-8 -*-
from __future__ import print_function
from collections import defaultdict
from . import mapping


def none_factory():
    return None

default_translate_table = defaultdict(none_factory, mapping.codepoint_to_replacement)

def fold(unicode_string, replacement=u''):
    """Fold unicode_string to ASCII.

Unmapped characters should be replaced with empty string by default, or other
replacement if provided.

All astral plane characters are always removed, even if a replacement is
provided.
    """

    if unicode_string is None:
        return u''

    if type(unicode_string) != unicode:
        raise TypeError('cannot fold bytestring')

    if type(replacement) != unicode:
        raise TypeError('cannot replace using bytestring')

    if replacement:
        def replacement_factory():
            return replacement

        translate_table = defaultdict(replacement_factory, \
                                      mapping.codepoint_to_replacement)
    else:
        translate_table = default_translate_table

    return unicode_string.translate(translate_table)
