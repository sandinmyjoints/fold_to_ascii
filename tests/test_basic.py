# -*- coding: utf-8 -*-

from .context import fold_to_ascii
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_none(self):
        self.assertEqual(fold_to_ascii.fold(None), "",
                         "This is expected to return the empty string.")

    def test_fold(self):
        # Fold mapped characters.
        self.assertEqual(fold_to_ascii.fold('á'), 'a')

        # Remove unmapped characters.
        self.assertEqual(fold_to_ascii.fold('£'), '')

        # Remove astral characters.
        self.assertEqual(fold_to_ascii.fold('💩'), '')

    def test_fold_with_replacement(self):
        self.assertEqual(fold_to_ascii.fold('a', 'X'), 'a')
        self.assertEqual(fold_to_ascii.fold('á', 'X'), 'a')
        self.assertEqual(fold_to_ascii.fold('£', 'X'), 'X')

        # Remove astral characters, always. This is not what fold-to-ascii
        # does, but Python struggles with astral characters...
        self.assertEqual(fold_to_ascii.fold('💩'), '')


if __name__ == '__main__':
    unittest.main()
