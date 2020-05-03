# -*- coding: utf-8 -*-
from __future__ import print_function
from collections import defaultdict
from . import mapping


def none_factory():
    return None


default_translate_table = defaultdict(none_factory, mapping.translate_table)


def fold(str, replacement=''):
    """Fold string to ASCII.

Unmapped characters should be replaced with empty string by default, or other
replacement if provided.

All astral plane characters are always removed, even if a replacement is
provided.
    """

    if str is None:
        return ''

    try:
        # If string contains only ASCII characters, return it.
        str.encode('ascii')
        return str
    except UnicodeEncodeError:
        pass

    if replacement:
        def replacement_factory():
            return replacement

        translate_table = defaultdict(replacement_factory,
                                      mapping.translate_table)
    else:
        translate_table = default_translate_table

    return str.translate(translate_table)
