# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import defaultdict

# Mapped characters.
default_translate_table_ord = dict([
  (ord(u'á'), u'a')
])

default_translate_table = defaultdict(unicode, [
  (u'á', u'a')
])

# Unmapped characters should be replaced with empty string by default, or other
# replacement if provided.

# All astral plane characters are removed.

def fold(unicode_string, replacement=u''):
    """Fold unicode_string to ASCII."""

    if type(unicode_string) != unicode:
        raise TypeError('cannot fold bytestring')

    if replacement:
        translate_table = defaultdict(lambda x: replacement, [
            (u'á', u'a')
        ])
    else:
        translate_table = default_translate_table

    # TODO: This can possibly be done more efficiently using a translate table.
    #
    # return unicode_string.translate(default_translate_table_ord)
    result = u''

    for c in unicode_string:
        result += translate_table[c]

    return result
