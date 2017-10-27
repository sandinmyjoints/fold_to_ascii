# -*- coding: utf-8 -*-

from .context import fold_to_ascii

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_bytestring_raises(self):
        with self.assertRaises(TypeError):
            fold_to_ascii.fold('á')

    def test_fold(self):
        self.assertEqual(fold_to_ascii.fold(u'á'), 'a')


if __name__ == '__main__':
    unittest.main()
