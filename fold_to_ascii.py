# -*- coding: utf-8 -*-

translate_table = dict([
  (ord(u'á'), u'a')
])

def fold(unicode_string):
    """Fold unicode_string to ASCII."""
    print type(unicode_string)
    if type(unicode_string) != unicode:
        raise TypeError('cannot fold bytestring')

    return unicode_string.translate(translate_table)
