# -*- coding: utf-8 -*-

from .context import fold_to_ascii
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_none(self):
        self.assertEqual(fold_to_ascii.fold(None), "", "This is expected to return the empty string.")

    def test_bytestring_raises(self):
        with self.assertRaises(TypeError):
            fold_to_ascii.fold('á')

    def test_bytestring_replacement_raises(self):
        with self.assertRaises(TypeError):
            fold_to_ascii.fold('á', 'X')

    def test_fold(self):
        # Fold mapped characters.
        self.assertEqual(fold_to_ascii.fold(u'á'), u'a')

        # Remove unmapped characters.
        self.assertEqual(fold_to_ascii.fold(u'£'), u'')

        # Remove astral characters.
        self.assertEqual(fold_to_ascii.fold(u'💩'), u'')

    def test_fold_with_replacement(self):
        self.assertEqual(fold_to_ascii.fold(u'a', u'X'), u'a')
        self.assertEqual(fold_to_ascii.fold(u'á', u'X'), u'a')
        self.assertEqual(fold_to_ascii.fold(u'£', u'X'), u'X')

        # Remove astral characters, always. This is not what fold-to-ascii
        # does, but Python struggles with astral characters...
        self.assertEqual(fold_to_ascii.fold(u'💩'), u'')


if __name__ == '__main__':
    unittest.main()
