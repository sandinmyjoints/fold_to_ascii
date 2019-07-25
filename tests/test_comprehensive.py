# -*- coding: utf-8 -*-
# flake8: noqa

from .context import fold_to_ascii
import unittest


class ComprehensiveTestSuite(unittest.TestCase):
  """Comprehensive test cases."""

  def test_all(self):
    # nullTest
    self.assertEqual(fold_to_ascii.fold(None), "", "This is expected to return the empty string.")


    # numberTest
    self.assertEqual(fold_to_ascii.fold('123456789'), "123456789", "This is expected to return a numeric sequence.")


    # emptyTest
    self.assertEqual(fold_to_ascii.fold(""), "", "This is expected to return the empty string.")


    # NoneTest
    self.assertEqual(fold_to_ascii.fold(None), "", "This is expected to return the empty string.")


    # spaceTabTest
    self.assertEqual(fold_to_ascii.fold(" 	 "), " 	 ", "This is expected to return a space-tab-space sequence.")


    # escapeSequenceTest
    self.assertEqual(fold_to_ascii.fold(" \b \t \n \v \f \r "), " \b \t \n \v \f \r ", "This is expected to return the escape sequences \\b \\t \\n \\v \\f \\r.")


    # controlCharacterTest
    controlCharacters = (chr(0x8) + chr(0x9) + chr(0xA) + chr(0xC) + chr(0xD))
    self.assertEqual(fold_to_ascii.fold(controlCharacters), controlCharacters, "This is expected to return control chracters.")


    # asciiPrintableTest
    self.assertEqual(fold_to_ascii.fold("0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ !\"#$%&'()*+,-./"), "0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ !\"#$%&'()*+,-./", "This is expected to return the ASCII printable characters.")


    # ATest
    self.assertEqual(fold_to_ascii.fold(chr(0xc0)), "A", "This is function is expected to escape the unicode sequence '\\u00C0' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0xc1)), "A", "This is function is expected to escape the unicode sequence '\\u00C1' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0xc2)), "A", "This is function is expected to escape the unicode sequence '\\u00C2' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0xc3)), "A", "This is function is expected to escape the unicode sequence '\\u00C3' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0xc4)), "A", "This is function is expected to escape the unicode sequence '\\u00C4' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0xc5)), "A", "This is function is expected to escape the unicode sequence '\\u00C5' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x100)), "A", "This is function is expected to escape the unicode sequence '\\u0100' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x102)), "A", "This is function is expected to escape the unicode sequence '\\u0102' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x104)), "A", "This is function is expected to escape the unicode sequence '\\u0104' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x18f)), "A", "This is function is expected to escape the unicode sequence '\\u018F' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1cd)), "A", "This is function is expected to escape the unicode sequence '\\u01CD' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1de)), "A", "This is function is expected to escape the unicode sequence '\\u01DE' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e0)), "A", "This is function is expected to escape the unicode sequence '\\u01E0' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1fa)), "A", "This is function is expected to escape the unicode sequence '\\u01FA' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x200)), "A", "This is function is expected to escape the unicode sequence '\\u0200' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x202)), "A", "This is function is expected to escape the unicode sequence '\\u0202' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x226)), "A", "This is function is expected to escape the unicode sequence '\\u0226' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x23a)), "A", "This is function is expected to escape the unicode sequence '\\u023A' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d00)), "A", "This is function is expected to escape the unicode sequence '\\u1D00' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e00)), "A", "This is function is expected to escape the unicode sequence '\\u1E00' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea0)), "A", "This is function is expected to escape the unicode sequence '\\u1EA0' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea2)), "A", "This is function is expected to escape the unicode sequence '\\u1EA2' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea4)), "A", "This is function is expected to escape the unicode sequence '\\u1EA4' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea6)), "A", "This is function is expected to escape the unicode sequence '\\u1EA6' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea8)), "A", "This is function is expected to escape the unicode sequence '\\u1EA8' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eaa)), "A", "This is function is expected to escape the unicode sequence '\\u1EAA' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eac)), "A", "This is function is expected to escape the unicode sequence '\\u1EAC' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eae)), "A", "This is function is expected to escape the unicode sequence '\\u1EAE' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb0)), "A", "This is function is expected to escape the unicode sequence '\\u1EB0' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb2)), "A", "This is function is expected to escape the unicode sequence '\\u1EB2' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb4)), "A", "This is function is expected to escape the unicode sequence '\\u1EB4' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb6)), "A", "This is function is expected to escape the unicode sequence '\\u1EB6' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24b6)), "A", "This is function is expected to escape the unicode sequence '\\u24B6' to 'A'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff21)), "A", "This is function is expected to escape the unicode sequence '\\uFF21' to 'A'")


    # aTest
    self.assertEqual(fold_to_ascii.fold(chr(0xe0)), "a", "This is function is expected to escape the unicode sequence '\\u00E0' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0xe1)), "a", "This is function is expected to escape the unicode sequence '\\u00E1' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0xe2)), "a", "This is function is expected to escape the unicode sequence '\\u00E2' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0xe3)), "a", "This is function is expected to escape the unicode sequence '\\u00E3' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0xe4)), "a", "This is function is expected to escape the unicode sequence '\\u00E4' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0xe5)), "a", "This is function is expected to escape the unicode sequence '\\u00E5' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x101)), "a", "This is function is expected to escape the unicode sequence '\\u0101' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x103)), "a", "This is function is expected to escape the unicode sequence '\\u0103' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x105)), "a", "This is function is expected to escape the unicode sequence '\\u0105' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ce)), "a", "This is function is expected to escape the unicode sequence '\\u01CE' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1df)), "a", "This is function is expected to escape the unicode sequence '\\u01DF' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e1)), "a", "This is function is expected to escape the unicode sequence '\\u01E1' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1fb)), "a", "This is function is expected to escape the unicode sequence '\\u01FB' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x201)), "a", "This is function is expected to escape the unicode sequence '\\u0201' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x203)), "a", "This is function is expected to escape the unicode sequence '\\u0203' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x227)), "a", "This is function is expected to escape the unicode sequence '\\u0227' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x250)), "a", "This is function is expected to escape the unicode sequence '\\u0250' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x259)), "a", "This is function is expected to escape the unicode sequence '\\u0259' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x25a)), "a", "This is function is expected to escape the unicode sequence '\\u025A' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d8f)), "a", "This is function is expected to escape the unicode sequence '\\u1D8F' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d95)), "a", "This is function is expected to escape the unicode sequence '\\u1D95' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e01)), "a", "This is function is expected to escape the unicode sequence '\\u1E01' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e9a)), "a", "This is function is expected to escape the unicode sequence '\\u1E9A' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea1)), "a", "This is function is expected to escape the unicode sequence '\\u1EA1' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea3)), "a", "This is function is expected to escape the unicode sequence '\\u1EA3' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea5)), "a", "This is function is expected to escape the unicode sequence '\\u1EA5' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea7)), "a", "This is function is expected to escape the unicode sequence '\\u1EA7' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea9)), "a", "This is function is expected to escape the unicode sequence '\\u1EA9' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eab)), "a", "This is function is expected to escape the unicode sequence '\\u1EAB' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ead)), "a", "This is function is expected to escape the unicode sequence '\\u1EAD' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eaf)), "a", "This is function is expected to escape the unicode sequence '\\u1EAF' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb1)), "a", "This is function is expected to escape the unicode sequence '\\u1EB1' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb3)), "a", "This is function is expected to escape the unicode sequence '\\u1EB3' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb5)), "a", "This is function is expected to escape the unicode sequence '\\u1EB5' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb7)), "a", "This is function is expected to escape the unicode sequence '\\u1EB7' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2090)), "a", "This is function is expected to escape the unicode sequence '\\u2090' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2094)), "a", "This is function is expected to escape the unicode sequence '\\u2094' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d0)), "a", "This is function is expected to escape the unicode sequence '\\u24D0' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c65)), "a", "This is function is expected to escape the unicode sequence '\\u2C65' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c6f)), "a", "This is function is expected to escape the unicode sequence '\\u2C6F' to 'a'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff41)), "a", "This is function is expected to escape the unicode sequence '\\uFF41' to 'a'")


    # AATest
    self.assertEqual(fold_to_ascii.fold(chr(0xa732)), "AA", "This is function is expected to escape the unicode sequence '\\uA732' to 'AA'")


    # AETest
    self.assertEqual(fold_to_ascii.fold(chr(0xc6)), "AE", "This is function is expected to escape the unicode sequence '\\u00C6' to 'AE'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e2)), "AE", "This is function is expected to escape the unicode sequence '\\u01E2' to 'AE'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1fc)), "AE", "This is function is expected to escape the unicode sequence '\\u01FC' to 'AE'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d01)), "AE", "This is function is expected to escape the unicode sequence '\\u1D01' to 'AE'")


    # AOTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa734)), "AO", "This is function is expected to escape the unicode sequence '\\uA734' to 'AO'")


    # AUTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa736)), "AU", "This is function is expected to escape the unicode sequence '\\uA736' to 'AU'")


    # AVTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa738)), "AV", "This is function is expected to escape the unicode sequence '\\uA738' to 'AV'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa73a)), "AV", "This is function is expected to escape the unicode sequence '\\uA73A' to 'AV'")


    # AYTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa73c)), "AY", "This is function is expected to escape the unicode sequence '\\uA73C' to 'AY'")


    # LeftParenthesisLatinSmallLetterARightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x249c)), "(a)", "This is function is expected to escape the unicode sequence '\\u249C' to '(a)'")


    # aaTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa733)), "aa", "This is function is expected to escape the unicode sequence '\\uA733' to 'aa'")


    # aeTest
    self.assertEqual(fold_to_ascii.fold(chr(0xe6)), "ae", "This is function is expected to escape the unicode sequence '\\u00E6' to 'ae'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e3)), "ae", "This is function is expected to escape the unicode sequence '\\u01E3' to 'ae'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1fd)), "ae", "This is function is expected to escape the unicode sequence '\\u01FD' to 'ae'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d02)), "ae", "This is function is expected to escape the unicode sequence '\\u1D02' to 'ae'")


    # aoTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa735)), "ao", "This is function is expected to escape the unicode sequence '\\uA735' to 'ao'")


    # auTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa737)), "au", "This is function is expected to escape the unicode sequence '\\uA737' to 'au'")


    # avTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa739)), "av", "This is function is expected to escape the unicode sequence '\\uA739' to 'av'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa73b)), "av", "This is function is expected to escape the unicode sequence '\\uA73B' to 'av'")


    # ayTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa73d)), "ay", "This is function is expected to escape the unicode sequence '\\uA73D' to 'ay'")


    # BTest
    self.assertEqual(fold_to_ascii.fold(chr(0x181)), "B", "This is function is expected to escape the unicode sequence '\\u0181' to 'B'")
    self.assertEqual(fold_to_ascii.fold(chr(0x182)), "B", "This is function is expected to escape the unicode sequence '\\u0182' to 'B'")
    self.assertEqual(fold_to_ascii.fold(chr(0x243)), "B", "This is function is expected to escape the unicode sequence '\\u0243' to 'B'")
    self.assertEqual(fold_to_ascii.fold(chr(0x299)), "B", "This is function is expected to escape the unicode sequence '\\u0299' to 'B'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d03)), "B", "This is function is expected to escape the unicode sequence '\\u1D03' to 'B'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e02)), "B", "This is function is expected to escape the unicode sequence '\\u1E02' to 'B'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e04)), "B", "This is function is expected to escape the unicode sequence '\\u1E04' to 'B'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e06)), "B", "This is function is expected to escape the unicode sequence '\\u1E06' to 'B'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24b7)), "B", "This is function is expected to escape the unicode sequence '\\u24B7' to 'B'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff22)), "B", "This is function is expected to escape the unicode sequence '\\uFF22' to 'B'")


    # bTest
    self.assertEqual(fold_to_ascii.fold(chr(0x180)), "b", "This is function is expected to escape the unicode sequence '\\u0180' to 'b'")
    self.assertEqual(fold_to_ascii.fold(chr(0x183)), "b", "This is function is expected to escape the unicode sequence '\\u0183' to 'b'")
    self.assertEqual(fold_to_ascii.fold(chr(0x253)), "b", "This is function is expected to escape the unicode sequence '\\u0253' to 'b'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d6c)), "b", "This is function is expected to escape the unicode sequence '\\u1D6C' to 'b'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d80)), "b", "This is function is expected to escape the unicode sequence '\\u1D80' to 'b'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e03)), "b", "This is function is expected to escape the unicode sequence '\\u1E03' to 'b'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e05)), "b", "This is function is expected to escape the unicode sequence '\\u1E05' to 'b'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e07)), "b", "This is function is expected to escape the unicode sequence '\\u1E07' to 'b'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d1)), "b", "This is function is expected to escape the unicode sequence '\\u24D1' to 'b'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff42)), "b", "This is function is expected to escape the unicode sequence '\\uFF42' to 'b'")


    # LeftParenthesisLatinSmallLetterBRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x249d)), "(b)", "This is function is expected to escape the unicode sequence '\\u249D' to '(b)'")


    # CTest
    self.assertEqual(fold_to_ascii.fold(chr(0xc7)), "C", "This is function is expected to escape the unicode sequence '\\u00C7' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x106)), "C", "This is function is expected to escape the unicode sequence '\\u0106' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x108)), "C", "This is function is expected to escape the unicode sequence '\\u0108' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x10a)), "C", "This is function is expected to escape the unicode sequence '\\u010A' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x10c)), "C", "This is function is expected to escape the unicode sequence '\\u010C' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x187)), "C", "This is function is expected to escape the unicode sequence '\\u0187' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x23b)), "C", "This is function is expected to escape the unicode sequence '\\u023B' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x297)), "C", "This is function is expected to escape the unicode sequence '\\u0297' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d04)), "C", "This is function is expected to escape the unicode sequence '\\u1D04' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e08)), "C", "This is function is expected to escape the unicode sequence '\\u1E08' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24b8)), "C", "This is function is expected to escape the unicode sequence '\\u24B8' to 'C'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff23)), "C", "This is function is expected to escape the unicode sequence '\\uFF23' to 'C'")


    # cTest
    self.assertEqual(fold_to_ascii.fold(chr(0xe7)), "c", "This is function is expected to escape the unicode sequence '\\u00E7' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x107)), "c", "This is function is expected to escape the unicode sequence '\\u0107' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x109)), "c", "This is function is expected to escape the unicode sequence '\\u0109' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x10b)), "c", "This is function is expected to escape the unicode sequence '\\u010B' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x10d)), "c", "This is function is expected to escape the unicode sequence '\\u010D' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x188)), "c", "This is function is expected to escape the unicode sequence '\\u0188' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x23c)), "c", "This is function is expected to escape the unicode sequence '\\u023C' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x255)), "c", "This is function is expected to escape the unicode sequence '\\u0255' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e09)), "c", "This is function is expected to escape the unicode sequence '\\u1E09' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2184)), "c", "This is function is expected to escape the unicode sequence '\\u2184' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d2)), "c", "This is function is expected to escape the unicode sequence '\\u24D2' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa73e)), "c", "This is function is expected to escape the unicode sequence '\\uA73E' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa73f)), "c", "This is function is expected to escape the unicode sequence '\\uA73F' to 'c'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff43)), "c", "This is function is expected to escape the unicode sequence '\\uFF43' to 'c'")


    # LeftParenthesisLatinSmallLetterCRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x249e)), "(c)", "This is function is expected to escape the unicode sequence '\\u249E' to '(c)'")


    # DTest
    self.assertEqual(fold_to_ascii.fold(chr(0xd0)), "D", "This is function is expected to escape the unicode sequence '\\u00D0' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x10e)), "D", "This is function is expected to escape the unicode sequence '\\u010E' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x110)), "D", "This is function is expected to escape the unicode sequence '\\u0110' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x189)), "D", "This is function is expected to escape the unicode sequence '\\u0189' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x18a)), "D", "This is function is expected to escape the unicode sequence '\\u018A' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x18b)), "D", "This is function is expected to escape the unicode sequence '\\u018B' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d05)), "D", "This is function is expected to escape the unicode sequence '\\u1D05' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d06)), "D", "This is function is expected to escape the unicode sequence '\\u1D06' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e0a)), "D", "This is function is expected to escape the unicode sequence '\\u1E0A' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e0c)), "D", "This is function is expected to escape the unicode sequence '\\u1E0C' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e0e)), "D", "This is function is expected to escape the unicode sequence '\\u1E0E' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e10)), "D", "This is function is expected to escape the unicode sequence '\\u1E10' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e12)), "D", "This is function is expected to escape the unicode sequence '\\u1E12' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24b9)), "D", "This is function is expected to escape the unicode sequence '\\u24B9' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa779)), "D", "This is function is expected to escape the unicode sequence '\\uA779' to 'D'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff24)), "D", "This is function is expected to escape the unicode sequence '\\uFF24' to 'D'")


    # dTest
    self.assertEqual(fold_to_ascii.fold(chr(0xf0)), "d", "This is function is expected to escape the unicode sequence '\\u00F0' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x10f)), "d", "This is function is expected to escape the unicode sequence '\\u010F' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x111)), "d", "This is function is expected to escape the unicode sequence '\\u0111' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x18c)), "d", "This is function is expected to escape the unicode sequence '\\u018C' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x221)), "d", "This is function is expected to escape the unicode sequence '\\u0221' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x256)), "d", "This is function is expected to escape the unicode sequence '\\u0256' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x257)), "d", "This is function is expected to escape the unicode sequence '\\u0257' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d6d)), "d", "This is function is expected to escape the unicode sequence '\\u1D6D' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d81)), "d", "This is function is expected to escape the unicode sequence '\\u1D81' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d91)), "d", "This is function is expected to escape the unicode sequence '\\u1D91' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e0b)), "d", "This is function is expected to escape the unicode sequence '\\u1E0B' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e0d)), "d", "This is function is expected to escape the unicode sequence '\\u1E0D' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e0f)), "d", "This is function is expected to escape the unicode sequence '\\u1E0F' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e11)), "d", "This is function is expected to escape the unicode sequence '\\u1E11' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e13)), "d", "This is function is expected to escape the unicode sequence '\\u1E13' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d3)), "d", "This is function is expected to escape the unicode sequence '\\u24D3' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa77a)), "d", "This is function is expected to escape the unicode sequence '\\uA77A' to 'd'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff44)), "d", "This is function is expected to escape the unicode sequence '\\uFF44' to 'd'")


    # DZTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1c4)), "DZ", "This is function is expected to escape the unicode sequence '\\u01C4' to 'DZ'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1f1)), "DZ", "This is function is expected to escape the unicode sequence '\\u01F1' to 'DZ'")


    # DzTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1c5)), "Dz", "This is function is expected to escape the unicode sequence '\\u01C5' to 'Dz'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1f2)), "Dz", "This is function is expected to escape the unicode sequence '\\u01F2' to 'Dz'")


    # LeftParenthesisLatinSmallLetterDRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x249f)), "(d)", "This is function is expected to escape the unicode sequence '\\u249F' to '(d)'")


    # dbTest
    self.assertEqual(fold_to_ascii.fold(chr(0x238)), "db", "This is function is expected to escape the unicode sequence '\\u0238' to 'db'")


    # dzTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1c6)), "dz", "This is function is expected to escape the unicode sequence '\\u01C6' to 'dz'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1f3)), "dz", "This is function is expected to escape the unicode sequence '\\u01F3' to 'dz'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2a3)), "dz", "This is function is expected to escape the unicode sequence '\\u02A3' to 'dz'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2a5)), "dz", "This is function is expected to escape the unicode sequence '\\u02A5' to 'dz'")


    # ETest
    self.assertEqual(fold_to_ascii.fold(chr(0xc8)), "E", "This is function is expected to escape the unicode sequence '\\u00C8' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0xc9)), "E", "This is function is expected to escape the unicode sequence '\\u00C9' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0xca)), "E", "This is function is expected to escape the unicode sequence '\\u00CA' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0xcb)), "E", "This is function is expected to escape the unicode sequence '\\u00CB' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x112)), "E", "This is function is expected to escape the unicode sequence '\\u0112' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x114)), "E", "This is function is expected to escape the unicode sequence '\\u0114' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x116)), "E", "This is function is expected to escape the unicode sequence '\\u0116' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x118)), "E", "This is function is expected to escape the unicode sequence '\\u0118' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x11a)), "E", "This is function is expected to escape the unicode sequence '\\u011A' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x18e)), "E", "This is function is expected to escape the unicode sequence '\\u018E' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x190)), "E", "This is function is expected to escape the unicode sequence '\\u0190' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x204)), "E", "This is function is expected to escape the unicode sequence '\\u0204' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x206)), "E", "This is function is expected to escape the unicode sequence '\\u0206' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x228)), "E", "This is function is expected to escape the unicode sequence '\\u0228' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x246)), "E", "This is function is expected to escape the unicode sequence '\\u0246' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d07)), "E", "This is function is expected to escape the unicode sequence '\\u1D07' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e14)), "E", "This is function is expected to escape the unicode sequence '\\u1E14' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e16)), "E", "This is function is expected to escape the unicode sequence '\\u1E16' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e18)), "E", "This is function is expected to escape the unicode sequence '\\u1E18' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e1a)), "E", "This is function is expected to escape the unicode sequence '\\u1E1A' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e1c)), "E", "This is function is expected to escape the unicode sequence '\\u1E1C' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb8)), "E", "This is function is expected to escape the unicode sequence '\\u1EB8' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eba)), "E", "This is function is expected to escape the unicode sequence '\\u1EBA' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ebc)), "E", "This is function is expected to escape the unicode sequence '\\u1EBC' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ebe)), "E", "This is function is expected to escape the unicode sequence '\\u1EBE' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec0)), "E", "This is function is expected to escape the unicode sequence '\\u1EC0' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec2)), "E", "This is function is expected to escape the unicode sequence '\\u1EC2' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec4)), "E", "This is function is expected to escape the unicode sequence '\\u1EC4' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec6)), "E", "This is function is expected to escape the unicode sequence '\\u1EC6' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24ba)), "E", "This is function is expected to escape the unicode sequence '\\u24BA' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c7b)), "E", "This is function is expected to escape the unicode sequence '\\u2C7B' to 'E'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff25)), "E", "This is function is expected to escape the unicode sequence '\\uFF25' to 'E'")


    # eTest
    self.assertEqual(fold_to_ascii.fold(chr(0xe8)), "e", "This is function is expected to escape the unicode sequence '\\u00E8' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0xe9)), "e", "This is function is expected to escape the unicode sequence '\\u00E9' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0xea)), "e", "This is function is expected to escape the unicode sequence '\\u00EA' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0xeb)), "e", "This is function is expected to escape the unicode sequence '\\u00EB' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x113)), "e", "This is function is expected to escape the unicode sequence '\\u0113' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x115)), "e", "This is function is expected to escape the unicode sequence '\\u0115' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x117)), "e", "This is function is expected to escape the unicode sequence '\\u0117' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x119)), "e", "This is function is expected to escape the unicode sequence '\\u0119' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x11b)), "e", "This is function is expected to escape the unicode sequence '\\u011B' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1dd)), "e", "This is function is expected to escape the unicode sequence '\\u01DD' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x205)), "e", "This is function is expected to escape the unicode sequence '\\u0205' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x207)), "e", "This is function is expected to escape the unicode sequence '\\u0207' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x229)), "e", "This is function is expected to escape the unicode sequence '\\u0229' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x247)), "e", "This is function is expected to escape the unicode sequence '\\u0247' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x258)), "e", "This is function is expected to escape the unicode sequence '\\u0258' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x25b)), "e", "This is function is expected to escape the unicode sequence '\\u025B' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x25c)), "e", "This is function is expected to escape the unicode sequence '\\u025C' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x25d)), "e", "This is function is expected to escape the unicode sequence '\\u025D' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x25e)), "e", "This is function is expected to escape the unicode sequence '\\u025E' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x29a)), "e", "This is function is expected to escape the unicode sequence '\\u029A' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d08)), "e", "This is function is expected to escape the unicode sequence '\\u1D08' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d92)), "e", "This is function is expected to escape the unicode sequence '\\u1D92' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d93)), "e", "This is function is expected to escape the unicode sequence '\\u1D93' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d94)), "e", "This is function is expected to escape the unicode sequence '\\u1D94' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e15)), "e", "This is function is expected to escape the unicode sequence '\\u1E15' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e17)), "e", "This is function is expected to escape the unicode sequence '\\u1E17' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e19)), "e", "This is function is expected to escape the unicode sequence '\\u1E19' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e1b)), "e", "This is function is expected to escape the unicode sequence '\\u1E1B' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e1d)), "e", "This is function is expected to escape the unicode sequence '\\u1E1D' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb9)), "e", "This is function is expected to escape the unicode sequence '\\u1EB9' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ebb)), "e", "This is function is expected to escape the unicode sequence '\\u1EBB' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ebd)), "e", "This is function is expected to escape the unicode sequence '\\u1EBD' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ebf)), "e", "This is function is expected to escape the unicode sequence '\\u1EBF' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec1)), "e", "This is function is expected to escape the unicode sequence '\\u1EC1' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec3)), "e", "This is function is expected to escape the unicode sequence '\\u1EC3' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec5)), "e", "This is function is expected to escape the unicode sequence '\\u1EC5' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec7)), "e", "This is function is expected to escape the unicode sequence '\\u1EC7' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2091)), "e", "This is function is expected to escape the unicode sequence '\\u2091' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d4)), "e", "This is function is expected to escape the unicode sequence '\\u24D4' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c78)), "e", "This is function is expected to escape the unicode sequence '\\u2C78' to 'e'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff45)), "e", "This is function is expected to escape the unicode sequence '\\uFF45' to 'e'")


    # LeftParenthesisLatinSmallLetterERightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a0)), "(e)", "This is function is expected to escape the unicode sequence '\\u24A0' to '(e)'")


    # FTest
    self.assertEqual(fold_to_ascii.fold(chr(0x191)), "F", "This is function is expected to escape the unicode sequence '\\u0191' to 'F'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e1e)), "F", "This is function is expected to escape the unicode sequence '\\u1E1E' to 'F'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24bb)), "F", "This is function is expected to escape the unicode sequence '\\u24BB' to 'F'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa730)), "F", "This is function is expected to escape the unicode sequence '\\uA730' to 'F'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa77b)), "F", "This is function is expected to escape the unicode sequence '\\uA77B' to 'F'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa7fb)), "F", "This is function is expected to escape the unicode sequence '\\uA7FB' to 'F'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff26)), "F", "This is function is expected to escape the unicode sequence '\\uFF26' to 'F'")


    # fTest
    self.assertEqual(fold_to_ascii.fold(chr(0x192)), "f", "This is function is expected to escape the unicode sequence '\\u0192' to 'f'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d6e)), "f", "This is function is expected to escape the unicode sequence '\\u1D6E' to 'f'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d82)), "f", "This is function is expected to escape the unicode sequence '\\u1D82' to 'f'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e1f)), "f", "This is function is expected to escape the unicode sequence '\\u1E1F' to 'f'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e9b)), "f", "This is function is expected to escape the unicode sequence '\\u1E9B' to 'f'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d5)), "f", "This is function is expected to escape the unicode sequence '\\u24D5' to 'f'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa77c)), "f", "This is function is expected to escape the unicode sequence '\\uA77C' to 'f'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff46)), "f", "This is function is expected to escape the unicode sequence '\\uFF46' to 'f'")


    # LeftParenthesisLatinSmallLetterFRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a1)), "(f)", "This is function is expected to escape the unicode sequence '\\u24A1' to '(f)'")


    # ffTest
    self.assertEqual(fold_to_ascii.fold(chr(0xfb00)), "ff", "This is function is expected to escape the unicode sequence '\\uFB00' to 'ff'")


    # ffiTest
    self.assertEqual(fold_to_ascii.fold(chr(0xfb03)), "ffi", "This is function is expected to escape the unicode sequence '\\uFB03' to 'ffi'")


    # fflTest
    self.assertEqual(fold_to_ascii.fold(chr(0xfb04)), "ffl", "This is function is expected to escape the unicode sequence '\\uFB04' to 'ffl'")


    # fiTest
    self.assertEqual(fold_to_ascii.fold(chr(0xfb01)), "fi", "This is function is expected to escape the unicode sequence '\\uFB01' to 'fi'")


    # flTest
    self.assertEqual(fold_to_ascii.fold(chr(0xfb02)), "fl", "This is function is expected to escape the unicode sequence '\\uFB02' to 'fl'")


    # GTest
    self.assertEqual(fold_to_ascii.fold(chr(0x11c)), "G", "This is function is expected to escape the unicode sequence '\\u011C' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x11e)), "G", "This is function is expected to escape the unicode sequence '\\u011E' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x120)), "G", "This is function is expected to escape the unicode sequence '\\u0120' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x122)), "G", "This is function is expected to escape the unicode sequence '\\u0122' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x193)), "G", "This is function is expected to escape the unicode sequence '\\u0193' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e4)), "G", "This is function is expected to escape the unicode sequence '\\u01E4' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e5)), "G", "This is function is expected to escape the unicode sequence '\\u01E5' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e6)), "G", "This is function is expected to escape the unicode sequence '\\u01E6' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e7)), "G", "This is function is expected to escape the unicode sequence '\\u01E7' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1f4)), "G", "This is function is expected to escape the unicode sequence '\\u01F4' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x262)), "G", "This is function is expected to escape the unicode sequence '\\u0262' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x29b)), "G", "This is function is expected to escape the unicode sequence '\\u029B' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e20)), "G", "This is function is expected to escape the unicode sequence '\\u1E20' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24bc)), "G", "This is function is expected to escape the unicode sequence '\\u24BC' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa77d)), "G", "This is function is expected to escape the unicode sequence '\\uA77D' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa77e)), "G", "This is function is expected to escape the unicode sequence '\\uA77E' to 'G'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff27)), "G", "This is function is expected to escape the unicode sequence '\\uFF27' to 'G'")


    # gTest
    self.assertEqual(fold_to_ascii.fold(chr(0x11d)), "g", "This is function is expected to escape the unicode sequence '\\u011D' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x11f)), "g", "This is function is expected to escape the unicode sequence '\\u011F' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x121)), "g", "This is function is expected to escape the unicode sequence '\\u0121' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x123)), "g", "This is function is expected to escape the unicode sequence '\\u0123' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1f5)), "g", "This is function is expected to escape the unicode sequence '\\u01F5' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x260)), "g", "This is function is expected to escape the unicode sequence '\\u0260' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x261)), "g", "This is function is expected to escape the unicode sequence '\\u0261' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d77)), "g", "This is function is expected to escape the unicode sequence '\\u1D77' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d79)), "g", "This is function is expected to escape the unicode sequence '\\u1D79' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d83)), "g", "This is function is expected to escape the unicode sequence '\\u1D83' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e21)), "g", "This is function is expected to escape the unicode sequence '\\u1E21' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d6)), "g", "This is function is expected to escape the unicode sequence '\\u24D6' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa77f)), "g", "This is function is expected to escape the unicode sequence '\\uA77F' to 'g'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff47)), "g", "This is function is expected to escape the unicode sequence '\\uFF47' to 'g'")


    # LeftParenthesisLatinSmallLetterGRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a2)), "(g)", "This is function is expected to escape the unicode sequence '\\u24A2' to '(g)'")


    # HTest
    self.assertEqual(fold_to_ascii.fold(chr(0x124)), "H", "This is function is expected to escape the unicode sequence '\\u0124' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x126)), "H", "This is function is expected to escape the unicode sequence '\\u0126' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x21e)), "H", "This is function is expected to escape the unicode sequence '\\u021E' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x29c)), "H", "This is function is expected to escape the unicode sequence '\\u029C' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e22)), "H", "This is function is expected to escape the unicode sequence '\\u1E22' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e24)), "H", "This is function is expected to escape the unicode sequence '\\u1E24' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e26)), "H", "This is function is expected to escape the unicode sequence '\\u1E26' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e28)), "H", "This is function is expected to escape the unicode sequence '\\u1E28' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e2a)), "H", "This is function is expected to escape the unicode sequence '\\u1E2A' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24bd)), "H", "This is function is expected to escape the unicode sequence '\\u24BD' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c67)), "H", "This is function is expected to escape the unicode sequence '\\u2C67' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c75)), "H", "This is function is expected to escape the unicode sequence '\\u2C75' to 'H'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff28)), "H", "This is function is expected to escape the unicode sequence '\\uFF28' to 'H'")


    # hTest
    self.assertEqual(fold_to_ascii.fold(chr(0x125)), "h", "This is function is expected to escape the unicode sequence '\\u0125' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x127)), "h", "This is function is expected to escape the unicode sequence '\\u0127' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x21f)), "h", "This is function is expected to escape the unicode sequence '\\u021F' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x265)), "h", "This is function is expected to escape the unicode sequence '\\u0265' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x266)), "h", "This is function is expected to escape the unicode sequence '\\u0266' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2ae)), "h", "This is function is expected to escape the unicode sequence '\\u02AE' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2af)), "h", "This is function is expected to escape the unicode sequence '\\u02AF' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e23)), "h", "This is function is expected to escape the unicode sequence '\\u1E23' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e25)), "h", "This is function is expected to escape the unicode sequence '\\u1E25' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e27)), "h", "This is function is expected to escape the unicode sequence '\\u1E27' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e29)), "h", "This is function is expected to escape the unicode sequence '\\u1E29' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e2b)), "h", "This is function is expected to escape the unicode sequence '\\u1E2B' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e96)), "h", "This is function is expected to escape the unicode sequence '\\u1E96' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d7)), "h", "This is function is expected to escape the unicode sequence '\\u24D7' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c68)), "h", "This is function is expected to escape the unicode sequence '\\u2C68' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c76)), "h", "This is function is expected to escape the unicode sequence '\\u2C76' to 'h'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff48)), "h", "This is function is expected to escape the unicode sequence '\\uFF48' to 'h'")


    # HVTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1f6)), "HV", "This is function is expected to escape the unicode sequence '\\u01F6' to 'HV'")


    # LeftParenthesisLatinSmallLetterHRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a3)), "(h)", "This is function is expected to escape the unicode sequence '\\u24A3' to '(h)'")


    # hvTest
    self.assertEqual(fold_to_ascii.fold(chr(0x195)), "hv", "This is function is expected to escape the unicode sequence '\\u0195' to 'hv'")


    # ITest
    self.assertEqual(fold_to_ascii.fold(chr(0xcc)), "I", "This is function is expected to escape the unicode sequence '\\u00CC' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0xcd)), "I", "This is function is expected to escape the unicode sequence '\\u00CD' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0xce)), "I", "This is function is expected to escape the unicode sequence '\\u00CE' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0xcf)), "I", "This is function is expected to escape the unicode sequence '\\u00CF' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x128)), "I", "This is function is expected to escape the unicode sequence '\\u0128' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x12a)), "I", "This is function is expected to escape the unicode sequence '\\u012A' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x12c)), "I", "This is function is expected to escape the unicode sequence '\\u012C' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x12e)), "I", "This is function is expected to escape the unicode sequence '\\u012E' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x130)), "I", "This is function is expected to escape the unicode sequence '\\u0130' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x196)), "I", "This is function is expected to escape the unicode sequence '\\u0196' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x197)), "I", "This is function is expected to escape the unicode sequence '\\u0197' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1cf)), "I", "This is function is expected to escape the unicode sequence '\\u01CF' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x208)), "I", "This is function is expected to escape the unicode sequence '\\u0208' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x20a)), "I", "This is function is expected to escape the unicode sequence '\\u020A' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x26a)), "I", "This is function is expected to escape the unicode sequence '\\u026A' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d7b)), "I", "This is function is expected to escape the unicode sequence '\\u1D7B' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e2c)), "I", "This is function is expected to escape the unicode sequence '\\u1E2C' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e2e)), "I", "This is function is expected to escape the unicode sequence '\\u1E2E' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec8)), "I", "This is function is expected to escape the unicode sequence '\\u1EC8' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eca)), "I", "This is function is expected to escape the unicode sequence '\\u1ECA' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24be)), "I", "This is function is expected to escape the unicode sequence '\\u24BE' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa7fe)), "I", "This is function is expected to escape the unicode sequence '\\uA7FE' to 'I'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff29)), "I", "This is function is expected to escape the unicode sequence '\\uFF29' to 'I'")


    # iTest
    self.assertEqual(fold_to_ascii.fold(chr(0xec)), "i", "This is function is expected to escape the unicode sequence '\\u00EC' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0xed)), "i", "This is function is expected to escape the unicode sequence '\\u00ED' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0xee)), "i", "This is function is expected to escape the unicode sequence '\\u00EE' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0xef)), "i", "This is function is expected to escape the unicode sequence '\\u00EF' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x129)), "i", "This is function is expected to escape the unicode sequence '\\u0129' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x12b)), "i", "This is function is expected to escape the unicode sequence '\\u012B' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x12d)), "i", "This is function is expected to escape the unicode sequence '\\u012D' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x12f)), "i", "This is function is expected to escape the unicode sequence '\\u012F' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x131)), "i", "This is function is expected to escape the unicode sequence '\\u0131' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d0)), "i", "This is function is expected to escape the unicode sequence '\\u01D0' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x209)), "i", "This is function is expected to escape the unicode sequence '\\u0209' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x20b)), "i", "This is function is expected to escape the unicode sequence '\\u020B' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x268)), "i", "This is function is expected to escape the unicode sequence '\\u0268' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d09)), "i", "This is function is expected to escape the unicode sequence '\\u1D09' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d62)), "i", "This is function is expected to escape the unicode sequence '\\u1D62' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d7c)), "i", "This is function is expected to escape the unicode sequence '\\u1D7C' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d96)), "i", "This is function is expected to escape the unicode sequence '\\u1D96' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e2d)), "i", "This is function is expected to escape the unicode sequence '\\u1E2D' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e2f)), "i", "This is function is expected to escape the unicode sequence '\\u1E2F' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec9)), "i", "This is function is expected to escape the unicode sequence '\\u1EC9' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ecb)), "i", "This is function is expected to escape the unicode sequence '\\u1ECB' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2071)), "i", "This is function is expected to escape the unicode sequence '\\u2071' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d8)), "i", "This is function is expected to escape the unicode sequence '\\u24D8' to 'i'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff49)), "i", "This is function is expected to escape the unicode sequence '\\uFF49' to 'i'")


    # IJTest
    self.assertEqual(fold_to_ascii.fold(chr(0x132)), "IJ", "This is function is expected to escape the unicode sequence '\\u0132' to 'IJ'")


    # LeftParenthesisLatinSmallLetterIRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a4)), "(i)", "This is function is expected to escape the unicode sequence '\\u24A4' to '(i)'")


    # ijTest
    self.assertEqual(fold_to_ascii.fold(chr(0x133)), "ij", "This is function is expected to escape the unicode sequence '\\u0133' to 'ij'")


    # JTest
    self.assertEqual(fold_to_ascii.fold(chr(0x134)), "J", "This is function is expected to escape the unicode sequence '\\u0134' to 'J'")
    self.assertEqual(fold_to_ascii.fold(chr(0x248)), "J", "This is function is expected to escape the unicode sequence '\\u0248' to 'J'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d0a)), "J", "This is function is expected to escape the unicode sequence '\\u1D0A' to 'J'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24bf)), "J", "This is function is expected to escape the unicode sequence '\\u24BF' to 'J'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff2a)), "J", "This is function is expected to escape the unicode sequence '\\uFF2A' to 'J'")


    # jTest
    self.assertEqual(fold_to_ascii.fold(chr(0x135)), "j", "This is function is expected to escape the unicode sequence '\\u0135' to 'j'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1f0)), "j", "This is function is expected to escape the unicode sequence '\\u01F0' to 'j'")
    self.assertEqual(fold_to_ascii.fold(chr(0x237)), "j", "This is function is expected to escape the unicode sequence '\\u0237' to 'j'")
    self.assertEqual(fold_to_ascii.fold(chr(0x249)), "j", "This is function is expected to escape the unicode sequence '\\u0249' to 'j'")
    self.assertEqual(fold_to_ascii.fold(chr(0x25f)), "j", "This is function is expected to escape the unicode sequence '\\u025F' to 'j'")
    self.assertEqual(fold_to_ascii.fold(chr(0x284)), "j", "This is function is expected to escape the unicode sequence '\\u0284' to 'j'")
    self.assertEqual(fold_to_ascii.fold(chr(0x29d)), "j", "This is function is expected to escape the unicode sequence '\\u029D' to 'j'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d9)), "j", "This is function is expected to escape the unicode sequence '\\u24D9' to 'j'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c7c)), "j", "This is function is expected to escape the unicode sequence '\\u2C7C' to 'j'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff4a)), "j", "This is function is expected to escape the unicode sequence '\\uFF4A' to 'j'")


    # LeftParenthesisLatinSmallLetterJRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a5)), "(j)", "This is function is expected to escape the unicode sequence '\\u24A5' to '(j)'")


    # KTest
    self.assertEqual(fold_to_ascii.fold(chr(0x136)), "K", "This is function is expected to escape the unicode sequence '\\u0136' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0x198)), "K", "This is function is expected to escape the unicode sequence '\\u0198' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e8)), "K", "This is function is expected to escape the unicode sequence '\\u01E8' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d0b)), "K", "This is function is expected to escape the unicode sequence '\\u1D0B' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e30)), "K", "This is function is expected to escape the unicode sequence '\\u1E30' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e32)), "K", "This is function is expected to escape the unicode sequence '\\u1E32' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e34)), "K", "This is function is expected to escape the unicode sequence '\\u1E34' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c0)), "K", "This is function is expected to escape the unicode sequence '\\u24C0' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c69)), "K", "This is function is expected to escape the unicode sequence '\\u2C69' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa740)), "K", "This is function is expected to escape the unicode sequence '\\uA740' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa742)), "K", "This is function is expected to escape the unicode sequence '\\uA742' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa744)), "K", "This is function is expected to escape the unicode sequence '\\uA744' to 'K'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff2b)), "K", "This is function is expected to escape the unicode sequence '\\uFF2B' to 'K'")


    # kTest
    self.assertEqual(fold_to_ascii.fold(chr(0x137)), "k", "This is function is expected to escape the unicode sequence '\\u0137' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0x199)), "k", "This is function is expected to escape the unicode sequence '\\u0199' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e9)), "k", "This is function is expected to escape the unicode sequence '\\u01E9' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0x29e)), "k", "This is function is expected to escape the unicode sequence '\\u029E' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d84)), "k", "This is function is expected to escape the unicode sequence '\\u1D84' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e31)), "k", "This is function is expected to escape the unicode sequence '\\u1E31' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e33)), "k", "This is function is expected to escape the unicode sequence '\\u1E33' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e35)), "k", "This is function is expected to escape the unicode sequence '\\u1E35' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24da)), "k", "This is function is expected to escape the unicode sequence '\\u24DA' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c6a)), "k", "This is function is expected to escape the unicode sequence '\\u2C6A' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa741)), "k", "This is function is expected to escape the unicode sequence '\\uA741' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa743)), "k", "This is function is expected to escape the unicode sequence '\\uA743' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa745)), "k", "This is function is expected to escape the unicode sequence '\\uA745' to 'k'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff4b)), "k", "This is function is expected to escape the unicode sequence '\\uFF4B' to 'k'")


    # LeftParenthesisLatinSmallLetterKRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a6)), "(k)", "This is function is expected to escape the unicode sequence '\\u24A6' to '(k)'")


    # LTest
    self.assertEqual(fold_to_ascii.fold(chr(0x139)), "L", "This is function is expected to escape the unicode sequence '\\u0139' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x13b)), "L", "This is function is expected to escape the unicode sequence '\\u013B' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x13d)), "L", "This is function is expected to escape the unicode sequence '\\u013D' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x13f)), "L", "This is function is expected to escape the unicode sequence '\\u013F' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x141)), "L", "This is function is expected to escape the unicode sequence '\\u0141' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x23d)), "L", "This is function is expected to escape the unicode sequence '\\u023D' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x29f)), "L", "This is function is expected to escape the unicode sequence '\\u029F' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d0c)), "L", "This is function is expected to escape the unicode sequence '\\u1D0C' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e36)), "L", "This is function is expected to escape the unicode sequence '\\u1E36' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e38)), "L", "This is function is expected to escape the unicode sequence '\\u1E38' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e3a)), "L", "This is function is expected to escape the unicode sequence '\\u1E3A' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e3c)), "L", "This is function is expected to escape the unicode sequence '\\u1E3C' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c1)), "L", "This is function is expected to escape the unicode sequence '\\u24C1' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c60)), "L", "This is function is expected to escape the unicode sequence '\\u2C60' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c62)), "L", "This is function is expected to escape the unicode sequence '\\u2C62' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa746)), "L", "This is function is expected to escape the unicode sequence '\\uA746' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa748)), "L", "This is function is expected to escape the unicode sequence '\\uA748' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa780)), "L", "This is function is expected to escape the unicode sequence '\\uA780' to 'L'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff2c)), "L", "This is function is expected to escape the unicode sequence '\\uFF2C' to 'L'")


    # lTest
    self.assertEqual(fold_to_ascii.fold(chr(0x13a)), "l", "This is function is expected to escape the unicode sequence '\\u013A' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x13c)), "l", "This is function is expected to escape the unicode sequence '\\u013C' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x13e)), "l", "This is function is expected to escape the unicode sequence '\\u013E' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x140)), "l", "This is function is expected to escape the unicode sequence '\\u0140' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x142)), "l", "This is function is expected to escape the unicode sequence '\\u0142' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x19a)), "l", "This is function is expected to escape the unicode sequence '\\u019A' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x234)), "l", "This is function is expected to escape the unicode sequence '\\u0234' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x26b)), "l", "This is function is expected to escape the unicode sequence '\\u026B' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x26c)), "l", "This is function is expected to escape the unicode sequence '\\u026C' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x26d)), "l", "This is function is expected to escape the unicode sequence '\\u026D' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d85)), "l", "This is function is expected to escape the unicode sequence '\\u1D85' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e37)), "l", "This is function is expected to escape the unicode sequence '\\u1E37' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e39)), "l", "This is function is expected to escape the unicode sequence '\\u1E39' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e3b)), "l", "This is function is expected to escape the unicode sequence '\\u1E3B' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e3d)), "l", "This is function is expected to escape the unicode sequence '\\u1E3D' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24db)), "l", "This is function is expected to escape the unicode sequence '\\u24DB' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c61)), "l", "This is function is expected to escape the unicode sequence '\\u2C61' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa747)), "l", "This is function is expected to escape the unicode sequence '\\uA747' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa749)), "l", "This is function is expected to escape the unicode sequence '\\uA749' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa781)), "l", "This is function is expected to escape the unicode sequence '\\uA781' to 'l'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff4c)), "l", "This is function is expected to escape the unicode sequence '\\uFF4C' to 'l'")


    # LJTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1c7)), "LJ", "This is function is expected to escape the unicode sequence '\\u01C7' to 'LJ'")


    # LLTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1efa)), "LL", "This is function is expected to escape the unicode sequence '\\u1EFA' to 'LL'")


    # LjTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1c8)), "Lj", "This is function is expected to escape the unicode sequence '\\u01C8' to 'Lj'")


    # LeftParenthesisLatinSmallLetterLRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a7)), "(l)", "This is function is expected to escape the unicode sequence '\\u24A7' to '(l)'")


    # ljTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1c9)), "lj", "This is function is expected to escape the unicode sequence '\\u01C9' to 'lj'")


    # llTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1efb)), "ll", "This is function is expected to escape the unicode sequence '\\u1EFB' to 'll'")


    # lsTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2aa)), "ls", "This is function is expected to escape the unicode sequence '\\u02AA' to 'ls'")


    # lzTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2ab)), "lz", "This is function is expected to escape the unicode sequence '\\u02AB' to 'lz'")


    # MTest
    self.assertEqual(fold_to_ascii.fold(chr(0x19c)), "M", "This is function is expected to escape the unicode sequence '\\u019C' to 'M'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d0d)), "M", "This is function is expected to escape the unicode sequence '\\u1D0D' to 'M'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e3e)), "M", "This is function is expected to escape the unicode sequence '\\u1E3E' to 'M'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e40)), "M", "This is function is expected to escape the unicode sequence '\\u1E40' to 'M'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e42)), "M", "This is function is expected to escape the unicode sequence '\\u1E42' to 'M'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c2)), "M", "This is function is expected to escape the unicode sequence '\\u24C2' to 'M'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c6e)), "M", "This is function is expected to escape the unicode sequence '\\u2C6E' to 'M'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa7fd)), "M", "This is function is expected to escape the unicode sequence '\\uA7FD' to 'M'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa7ff)), "M", "This is function is expected to escape the unicode sequence '\\uA7FF' to 'M'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff2d)), "M", "This is function is expected to escape the unicode sequence '\\uFF2D' to 'M'")


    # mTest
    self.assertEqual(fold_to_ascii.fold(chr(0x26f)), "m", "This is function is expected to escape the unicode sequence '\\u026F' to 'm'")
    self.assertEqual(fold_to_ascii.fold(chr(0x270)), "m", "This is function is expected to escape the unicode sequence '\\u0270' to 'm'")
    self.assertEqual(fold_to_ascii.fold(chr(0x271)), "m", "This is function is expected to escape the unicode sequence '\\u0271' to 'm'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d6f)), "m", "This is function is expected to escape the unicode sequence '\\u1D6F' to 'm'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d86)), "m", "This is function is expected to escape the unicode sequence '\\u1D86' to 'm'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e3f)), "m", "This is function is expected to escape the unicode sequence '\\u1E3F' to 'm'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e41)), "m", "This is function is expected to escape the unicode sequence '\\u1E41' to 'm'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e43)), "m", "This is function is expected to escape the unicode sequence '\\u1E43' to 'm'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24dc)), "m", "This is function is expected to escape the unicode sequence '\\u24DC' to 'm'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff4d)), "m", "This is function is expected to escape the unicode sequence '\\uFF4D' to 'm'")


    # LeftParenthesisLatinSmallLetterMRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a8)), "(m)", "This is function is expected to escape the unicode sequence '\\u24A8' to '(m)'")


    # NTest
    self.assertEqual(fold_to_ascii.fold(chr(0xd1)), "N", "This is function is expected to escape the unicode sequence '\\u00D1' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x143)), "N", "This is function is expected to escape the unicode sequence '\\u0143' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x145)), "N", "This is function is expected to escape the unicode sequence '\\u0145' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x147)), "N", "This is function is expected to escape the unicode sequence '\\u0147' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x14a)), "N", "This is function is expected to escape the unicode sequence '\\u014A' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x19d)), "N", "This is function is expected to escape the unicode sequence '\\u019D' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1f8)), "N", "This is function is expected to escape the unicode sequence '\\u01F8' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x220)), "N", "This is function is expected to escape the unicode sequence '\\u0220' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x274)), "N", "This is function is expected to escape the unicode sequence '\\u0274' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d0e)), "N", "This is function is expected to escape the unicode sequence '\\u1D0E' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e44)), "N", "This is function is expected to escape the unicode sequence '\\u1E44' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e46)), "N", "This is function is expected to escape the unicode sequence '\\u1E46' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e48)), "N", "This is function is expected to escape the unicode sequence '\\u1E48' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e4a)), "N", "This is function is expected to escape the unicode sequence '\\u1E4A' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c3)), "N", "This is function is expected to escape the unicode sequence '\\u24C3' to 'N'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff2e)), "N", "This is function is expected to escape the unicode sequence '\\uFF2E' to 'N'")


    # nTest
    self.assertEqual(fold_to_ascii.fold(chr(0xf1)), "n", "This is function is expected to escape the unicode sequence '\\u00F1' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x144)), "n", "This is function is expected to escape the unicode sequence '\\u0144' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x146)), "n", "This is function is expected to escape the unicode sequence '\\u0146' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x148)), "n", "This is function is expected to escape the unicode sequence '\\u0148' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x149)), "n", "This is function is expected to escape the unicode sequence '\\u0149' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x14b)), "n", "This is function is expected to escape the unicode sequence '\\u014B' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x19e)), "n", "This is function is expected to escape the unicode sequence '\\u019E' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1f9)), "n", "This is function is expected to escape the unicode sequence '\\u01F9' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x235)), "n", "This is function is expected to escape the unicode sequence '\\u0235' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x272)), "n", "This is function is expected to escape the unicode sequence '\\u0272' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x273)), "n", "This is function is expected to escape the unicode sequence '\\u0273' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d70)), "n", "This is function is expected to escape the unicode sequence '\\u1D70' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d87)), "n", "This is function is expected to escape the unicode sequence '\\u1D87' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e45)), "n", "This is function is expected to escape the unicode sequence '\\u1E45' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e47)), "n", "This is function is expected to escape the unicode sequence '\\u1E47' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e49)), "n", "This is function is expected to escape the unicode sequence '\\u1E49' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e4b)), "n", "This is function is expected to escape the unicode sequence '\\u1E4B' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x207f)), "n", "This is function is expected to escape the unicode sequence '\\u207F' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24dd)), "n", "This is function is expected to escape the unicode sequence '\\u24DD' to 'n'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff4e)), "n", "This is function is expected to escape the unicode sequence '\\uFF4E' to 'n'")


    # NJTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1ca)), "NJ", "This is function is expected to escape the unicode sequence '\\u01CA' to 'NJ'")


    # NjTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1cb)), "Nj", "This is function is expected to escape the unicode sequence '\\u01CB' to 'Nj'")


    # LeftParenthesisLatinSmallLetterNRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a9)), "(n)", "This is function is expected to escape the unicode sequence '\\u24A9' to '(n)'")


    # njTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1cc)), "nj", "This is function is expected to escape the unicode sequence '\\u01CC' to 'nj'")


    # OTest
    self.assertEqual(fold_to_ascii.fold(chr(0xd2)), "O", "This is function is expected to escape the unicode sequence '\\u00D2' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0xd3)), "O", "This is function is expected to escape the unicode sequence '\\u00D3' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0xd4)), "O", "This is function is expected to escape the unicode sequence '\\u00D4' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0xd5)), "O", "This is function is expected to escape the unicode sequence '\\u00D5' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0xd6)), "O", "This is function is expected to escape the unicode sequence '\\u00D6' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0xd8)), "O", "This is function is expected to escape the unicode sequence '\\u00D8' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x14c)), "O", "This is function is expected to escape the unicode sequence '\\u014C' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x14e)), "O", "This is function is expected to escape the unicode sequence '\\u014E' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x150)), "O", "This is function is expected to escape the unicode sequence '\\u0150' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x186)), "O", "This is function is expected to escape the unicode sequence '\\u0186' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x19f)), "O", "This is function is expected to escape the unicode sequence '\\u019F' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1a0)), "O", "This is function is expected to escape the unicode sequence '\\u01A0' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d1)), "O", "This is function is expected to escape the unicode sequence '\\u01D1' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ea)), "O", "This is function is expected to escape the unicode sequence '\\u01EA' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ec)), "O", "This is function is expected to escape the unicode sequence '\\u01EC' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1fe)), "O", "This is function is expected to escape the unicode sequence '\\u01FE' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x20c)), "O", "This is function is expected to escape the unicode sequence '\\u020C' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x20e)), "O", "This is function is expected to escape the unicode sequence '\\u020E' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x22a)), "O", "This is function is expected to escape the unicode sequence '\\u022A' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x22c)), "O", "This is function is expected to escape the unicode sequence '\\u022C' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x22e)), "O", "This is function is expected to escape the unicode sequence '\\u022E' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x230)), "O", "This is function is expected to escape the unicode sequence '\\u0230' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d0f)), "O", "This is function is expected to escape the unicode sequence '\\u1D0F' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d10)), "O", "This is function is expected to escape the unicode sequence '\\u1D10' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e4c)), "O", "This is function is expected to escape the unicode sequence '\\u1E4C' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e4e)), "O", "This is function is expected to escape the unicode sequence '\\u1E4E' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e50)), "O", "This is function is expected to escape the unicode sequence '\\u1E50' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e52)), "O", "This is function is expected to escape the unicode sequence '\\u1E52' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ecc)), "O", "This is function is expected to escape the unicode sequence '\\u1ECC' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ece)), "O", "This is function is expected to escape the unicode sequence '\\u1ECE' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed0)), "O", "This is function is expected to escape the unicode sequence '\\u1ED0' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed2)), "O", "This is function is expected to escape the unicode sequence '\\u1ED2' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed4)), "O", "This is function is expected to escape the unicode sequence '\\u1ED4' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed6)), "O", "This is function is expected to escape the unicode sequence '\\u1ED6' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed8)), "O", "This is function is expected to escape the unicode sequence '\\u1ED8' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eda)), "O", "This is function is expected to escape the unicode sequence '\\u1EDA' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1edc)), "O", "This is function is expected to escape the unicode sequence '\\u1EDC' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ede)), "O", "This is function is expected to escape the unicode sequence '\\u1EDE' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee0)), "O", "This is function is expected to escape the unicode sequence '\\u1EE0' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee2)), "O", "This is function is expected to escape the unicode sequence '\\u1EE2' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c4)), "O", "This is function is expected to escape the unicode sequence '\\u24C4' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa74a)), "O", "This is function is expected to escape the unicode sequence '\\uA74A' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa74c)), "O", "This is function is expected to escape the unicode sequence '\\uA74C' to 'O'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff2f)), "O", "This is function is expected to escape the unicode sequence '\\uFF2F' to 'O'")


    # oTest
    self.assertEqual(fold_to_ascii.fold(chr(0xf2)), "o", "This is function is expected to escape the unicode sequence '\\u00F2' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0xf3)), "o", "This is function is expected to escape the unicode sequence '\\u00F3' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0xf4)), "o", "This is function is expected to escape the unicode sequence '\\u00F4' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0xf5)), "o", "This is function is expected to escape the unicode sequence '\\u00F5' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0xf6)), "o", "This is function is expected to escape the unicode sequence '\\u00F6' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0xf8)), "o", "This is function is expected to escape the unicode sequence '\\u00F8' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x14d)), "o", "This is function is expected to escape the unicode sequence '\\u014D' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x14f)), "o", "This is function is expected to escape the unicode sequence '\\u014F' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x151)), "o", "This is function is expected to escape the unicode sequence '\\u0151' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1a1)), "o", "This is function is expected to escape the unicode sequence '\\u01A1' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d2)), "o", "This is function is expected to escape the unicode sequence '\\u01D2' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eb)), "o", "This is function is expected to escape the unicode sequence '\\u01EB' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed)), "o", "This is function is expected to escape the unicode sequence '\\u01ED' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ff)), "o", "This is function is expected to escape the unicode sequence '\\u01FF' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x20d)), "o", "This is function is expected to escape the unicode sequence '\\u020D' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x20f)), "o", "This is function is expected to escape the unicode sequence '\\u020F' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x22b)), "o", "This is function is expected to escape the unicode sequence '\\u022B' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x22d)), "o", "This is function is expected to escape the unicode sequence '\\u022D' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x22f)), "o", "This is function is expected to escape the unicode sequence '\\u022F' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x231)), "o", "This is function is expected to escape the unicode sequence '\\u0231' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x254)), "o", "This is function is expected to escape the unicode sequence '\\u0254' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x275)), "o", "This is function is expected to escape the unicode sequence '\\u0275' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d16)), "o", "This is function is expected to escape the unicode sequence '\\u1D16' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d17)), "o", "This is function is expected to escape the unicode sequence '\\u1D17' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d97)), "o", "This is function is expected to escape the unicode sequence '\\u1D97' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e4d)), "o", "This is function is expected to escape the unicode sequence '\\u1E4D' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e4f)), "o", "This is function is expected to escape the unicode sequence '\\u1E4F' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e51)), "o", "This is function is expected to escape the unicode sequence '\\u1E51' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e53)), "o", "This is function is expected to escape the unicode sequence '\\u1E53' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ecd)), "o", "This is function is expected to escape the unicode sequence '\\u1ECD' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ecf)), "o", "This is function is expected to escape the unicode sequence '\\u1ECF' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed1)), "o", "This is function is expected to escape the unicode sequence '\\u1ED1' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed3)), "o", "This is function is expected to escape the unicode sequence '\\u1ED3' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed5)), "o", "This is function is expected to escape the unicode sequence '\\u1ED5' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed7)), "o", "This is function is expected to escape the unicode sequence '\\u1ED7' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ed9)), "o", "This is function is expected to escape the unicode sequence '\\u1ED9' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1edb)), "o", "This is function is expected to escape the unicode sequence '\\u1EDB' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1edd)), "o", "This is function is expected to escape the unicode sequence '\\u1EDD' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1edf)), "o", "This is function is expected to escape the unicode sequence '\\u1EDF' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee1)), "o", "This is function is expected to escape the unicode sequence '\\u1EE1' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee3)), "o", "This is function is expected to escape the unicode sequence '\\u1EE3' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2092)), "o", "This is function is expected to escape the unicode sequence '\\u2092' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24de)), "o", "This is function is expected to escape the unicode sequence '\\u24DE' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c7a)), "o", "This is function is expected to escape the unicode sequence '\\u2C7A' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa74b)), "o", "This is function is expected to escape the unicode sequence '\\uA74B' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa74d)), "o", "This is function is expected to escape the unicode sequence '\\uA74D' to 'o'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff4f)), "o", "This is function is expected to escape the unicode sequence '\\uFF4F' to 'o'")


    # OETest
    self.assertEqual(fold_to_ascii.fold(chr(0x152)), "OE", "This is function is expected to escape the unicode sequence '\\u0152' to 'OE'")
    self.assertEqual(fold_to_ascii.fold(chr(0x276)), "OE", "This is function is expected to escape the unicode sequence '\\u0276' to 'OE'")


    # OOTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa74e)), "OO", "This is function is expected to escape the unicode sequence '\\uA74E' to 'OO'")


    # OUTest
    self.assertEqual(fold_to_ascii.fold(chr(0x222)), "OU", "This is function is expected to escape the unicode sequence '\\u0222' to 'OU'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d15)), "OU", "This is function is expected to escape the unicode sequence '\\u1D15' to 'OU'")


    # LeftParenthesisLatinSmallLetterORightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24aa)), "(o)", "This is function is expected to escape the unicode sequence '\\u24AA' to '(o)'")


    # oeTest
    self.assertEqual(fold_to_ascii.fold(chr(0x153)), "oe", "This is function is expected to escape the unicode sequence '\\u0153' to 'oe'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d14)), "oe", "This is function is expected to escape the unicode sequence '\\u1D14' to 'oe'")


    # ooTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa74f)), "oo", "This is function is expected to escape the unicode sequence '\\uA74F' to 'oo'")


    # ouTest
    self.assertEqual(fold_to_ascii.fold(chr(0x223)), "ou", "This is function is expected to escape the unicode sequence '\\u0223' to 'ou'")


    # PTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1a4)), "P", "This is function is expected to escape the unicode sequence '\\u01A4' to 'P'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d18)), "P", "This is function is expected to escape the unicode sequence '\\u1D18' to 'P'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e54)), "P", "This is function is expected to escape the unicode sequence '\\u1E54' to 'P'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e56)), "P", "This is function is expected to escape the unicode sequence '\\u1E56' to 'P'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c5)), "P", "This is function is expected to escape the unicode sequence '\\u24C5' to 'P'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c63)), "P", "This is function is expected to escape the unicode sequence '\\u2C63' to 'P'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa750)), "P", "This is function is expected to escape the unicode sequence '\\uA750' to 'P'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa752)), "P", "This is function is expected to escape the unicode sequence '\\uA752' to 'P'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa754)), "P", "This is function is expected to escape the unicode sequence '\\uA754' to 'P'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff30)), "P", "This is function is expected to escape the unicode sequence '\\uFF30' to 'P'")


    # pTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1a5)), "p", "This is function is expected to escape the unicode sequence '\\u01A5' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d71)), "p", "This is function is expected to escape the unicode sequence '\\u1D71' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d7d)), "p", "This is function is expected to escape the unicode sequence '\\u1D7D' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d88)), "p", "This is function is expected to escape the unicode sequence '\\u1D88' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e55)), "p", "This is function is expected to escape the unicode sequence '\\u1E55' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e57)), "p", "This is function is expected to escape the unicode sequence '\\u1E57' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24df)), "p", "This is function is expected to escape the unicode sequence '\\u24DF' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa751)), "p", "This is function is expected to escape the unicode sequence '\\uA751' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa753)), "p", "This is function is expected to escape the unicode sequence '\\uA753' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa755)), "p", "This is function is expected to escape the unicode sequence '\\uA755' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa7fc)), "p", "This is function is expected to escape the unicode sequence '\\uA7FC' to 'p'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff50)), "p", "This is function is expected to escape the unicode sequence '\\uFF50' to 'p'")


    # LeftParenthesisLatinSmallLetterPRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24ab)), "(p)", "This is function is expected to escape the unicode sequence '\\u24AB' to '(p)'")


    # QTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24a)), "Q", "This is function is expected to escape the unicode sequence '\\u024A' to 'Q'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c6)), "Q", "This is function is expected to escape the unicode sequence '\\u24C6' to 'Q'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa756)), "Q", "This is function is expected to escape the unicode sequence '\\uA756' to 'Q'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa758)), "Q", "This is function is expected to escape the unicode sequence '\\uA758' to 'Q'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff31)), "Q", "This is function is expected to escape the unicode sequence '\\uFF31' to 'Q'")


    # qTest
    self.assertEqual(fold_to_ascii.fold(chr(0x138)), "q", "This is function is expected to escape the unicode sequence '\\u0138' to 'q'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24b)), "q", "This is function is expected to escape the unicode sequence '\\u024B' to 'q'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2a0)), "q", "This is function is expected to escape the unicode sequence '\\u02A0' to 'q'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e0)), "q", "This is function is expected to escape the unicode sequence '\\u24E0' to 'q'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa757)), "q", "This is function is expected to escape the unicode sequence '\\uA757' to 'q'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa759)), "q", "This is function is expected to escape the unicode sequence '\\uA759' to 'q'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff51)), "q", "This is function is expected to escape the unicode sequence '\\uFF51' to 'q'")


    # LeftParenthesisLatinSmallLetterQRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24ac)), "(q)", "This is function is expected to escape the unicode sequence '\\u24AC' to '(q)'")


    # qpTest
    self.assertEqual(fold_to_ascii.fold(chr(0x239)), "qp", "This is function is expected to escape the unicode sequence '\\u0239' to 'qp'")


    # RTest
    self.assertEqual(fold_to_ascii.fold(chr(0x154)), "R", "This is function is expected to escape the unicode sequence '\\u0154' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x156)), "R", "This is function is expected to escape the unicode sequence '\\u0156' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x158)), "R", "This is function is expected to escape the unicode sequence '\\u0158' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x210)), "R", "This is function is expected to escape the unicode sequence '\\u0210' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x212)), "R", "This is function is expected to escape the unicode sequence '\\u0212' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c)), "R", "This is function is expected to escape the unicode sequence '\\u024C' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x280)), "R", "This is function is expected to escape the unicode sequence '\\u0280' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x281)), "R", "This is function is expected to escape the unicode sequence '\\u0281' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d19)), "R", "This is function is expected to escape the unicode sequence '\\u1D19' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d1a)), "R", "This is function is expected to escape the unicode sequence '\\u1D1A' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e58)), "R", "This is function is expected to escape the unicode sequence '\\u1E58' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e5a)), "R", "This is function is expected to escape the unicode sequence '\\u1E5A' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e5c)), "R", "This is function is expected to escape the unicode sequence '\\u1E5C' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e5e)), "R", "This is function is expected to escape the unicode sequence '\\u1E5E' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c7)), "R", "This is function is expected to escape the unicode sequence '\\u24C7' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c64)), "R", "This is function is expected to escape the unicode sequence '\\u2C64' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa75a)), "R", "This is function is expected to escape the unicode sequence '\\uA75A' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa782)), "R", "This is function is expected to escape the unicode sequence '\\uA782' to 'R'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff32)), "R", "This is function is expected to escape the unicode sequence '\\uFF32' to 'R'")


    # rTest
    self.assertEqual(fold_to_ascii.fold(chr(0x155)), "r", "This is function is expected to escape the unicode sequence '\\u0155' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x157)), "r", "This is function is expected to escape the unicode sequence '\\u0157' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x159)), "r", "This is function is expected to escape the unicode sequence '\\u0159' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x211)), "r", "This is function is expected to escape the unicode sequence '\\u0211' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x213)), "r", "This is function is expected to escape the unicode sequence '\\u0213' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24d)), "r", "This is function is expected to escape the unicode sequence '\\u024D' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x27c)), "r", "This is function is expected to escape the unicode sequence '\\u027C' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x27d)), "r", "This is function is expected to escape the unicode sequence '\\u027D' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x27e)), "r", "This is function is expected to escape the unicode sequence '\\u027E' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x27f)), "r", "This is function is expected to escape the unicode sequence '\\u027F' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d63)), "r", "This is function is expected to escape the unicode sequence '\\u1D63' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d72)), "r", "This is function is expected to escape the unicode sequence '\\u1D72' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d73)), "r", "This is function is expected to escape the unicode sequence '\\u1D73' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d89)), "r", "This is function is expected to escape the unicode sequence '\\u1D89' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e59)), "r", "This is function is expected to escape the unicode sequence '\\u1E59' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e5b)), "r", "This is function is expected to escape the unicode sequence '\\u1E5B' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e5d)), "r", "This is function is expected to escape the unicode sequence '\\u1E5D' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e5f)), "r", "This is function is expected to escape the unicode sequence '\\u1E5F' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e1)), "r", "This is function is expected to escape the unicode sequence '\\u24E1' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa75b)), "r", "This is function is expected to escape the unicode sequence '\\uA75B' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa783)), "r", "This is function is expected to escape the unicode sequence '\\uA783' to 'r'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff52)), "r", "This is function is expected to escape the unicode sequence '\\uFF52' to 'r'")


    # LeftParenthesisLatinSmallLetterRRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24ad)), "(r)", "This is function is expected to escape the unicode sequence '\\u24AD' to '(r)'")


    # STest
    self.assertEqual(fold_to_ascii.fold(chr(0x15a)), "S", "This is function is expected to escape the unicode sequence '\\u015A' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x15c)), "S", "This is function is expected to escape the unicode sequence '\\u015C' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x15e)), "S", "This is function is expected to escape the unicode sequence '\\u015E' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x160)), "S", "This is function is expected to escape the unicode sequence '\\u0160' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x218)), "S", "This is function is expected to escape the unicode sequence '\\u0218' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e60)), "S", "This is function is expected to escape the unicode sequence '\\u1E60' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e62)), "S", "This is function is expected to escape the unicode sequence '\\u1E62' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e64)), "S", "This is function is expected to escape the unicode sequence '\\u1E64' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e66)), "S", "This is function is expected to escape the unicode sequence '\\u1E66' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e68)), "S", "This is function is expected to escape the unicode sequence '\\u1E68' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c8)), "S", "This is function is expected to escape the unicode sequence '\\u24C8' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa731)), "S", "This is function is expected to escape the unicode sequence '\\uA731' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa785)), "S", "This is function is expected to escape the unicode sequence '\\uA785' to 'S'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff33)), "S", "This is function is expected to escape the unicode sequence '\\uFF33' to 'S'")


    # sTest
    self.assertEqual(fold_to_ascii.fold(chr(0x15b)), "s", "This is function is expected to escape the unicode sequence '\\u015B' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x15d)), "s", "This is function is expected to escape the unicode sequence '\\u015D' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x15f)), "s", "This is function is expected to escape the unicode sequence '\\u015F' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x161)), "s", "This is function is expected to escape the unicode sequence '\\u0161' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x17f)), "s", "This is function is expected to escape the unicode sequence '\\u017F' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x219)), "s", "This is function is expected to escape the unicode sequence '\\u0219' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x23f)), "s", "This is function is expected to escape the unicode sequence '\\u023F' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x282)), "s", "This is function is expected to escape the unicode sequence '\\u0282' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d74)), "s", "This is function is expected to escape the unicode sequence '\\u1D74' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d8a)), "s", "This is function is expected to escape the unicode sequence '\\u1D8A' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e61)), "s", "This is function is expected to escape the unicode sequence '\\u1E61' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e63)), "s", "This is function is expected to escape the unicode sequence '\\u1E63' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e65)), "s", "This is function is expected to escape the unicode sequence '\\u1E65' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e67)), "s", "This is function is expected to escape the unicode sequence '\\u1E67' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e69)), "s", "This is function is expected to escape the unicode sequence '\\u1E69' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e9c)), "s", "This is function is expected to escape the unicode sequence '\\u1E9C' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e9d)), "s", "This is function is expected to escape the unicode sequence '\\u1E9D' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e2)), "s", "This is function is expected to escape the unicode sequence '\\u24E2' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa784)), "s", "This is function is expected to escape the unicode sequence '\\uA784' to 's'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff53)), "s", "This is function is expected to escape the unicode sequence '\\uFF53' to 's'")


    # SSTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1e9e)), "SS", "This is function is expected to escape the unicode sequence '\\u1E9E' to 'SS'")


    # LeftParenthesisLatinSmallLetterSRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24ae)), "(s)", "This is function is expected to escape the unicode sequence '\\u24AE' to '(s)'")


    # ssTest
    self.assertEqual(fold_to_ascii.fold(chr(0xdf)), "ss", "This is function is expected to escape the unicode sequence '\\u00DF' to 'ss'")


    # stTest
    self.assertEqual(fold_to_ascii.fold(chr(0xfb06)), "st", "This is function is expected to escape the unicode sequence '\\uFB06' to 'st'")


    # TTest
    self.assertEqual(fold_to_ascii.fold(chr(0x162)), "T", "This is function is expected to escape the unicode sequence '\\u0162' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x164)), "T", "This is function is expected to escape the unicode sequence '\\u0164' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x166)), "T", "This is function is expected to escape the unicode sequence '\\u0166' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ac)), "T", "This is function is expected to escape the unicode sequence '\\u01AC' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ae)), "T", "This is function is expected to escape the unicode sequence '\\u01AE' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x21a)), "T", "This is function is expected to escape the unicode sequence '\\u021A' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x23e)), "T", "This is function is expected to escape the unicode sequence '\\u023E' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d1b)), "T", "This is function is expected to escape the unicode sequence '\\u1D1B' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e6a)), "T", "This is function is expected to escape the unicode sequence '\\u1E6A' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e6c)), "T", "This is function is expected to escape the unicode sequence '\\u1E6C' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e6e)), "T", "This is function is expected to escape the unicode sequence '\\u1E6E' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e70)), "T", "This is function is expected to escape the unicode sequence '\\u1E70' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24c9)), "T", "This is function is expected to escape the unicode sequence '\\u24C9' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa786)), "T", "This is function is expected to escape the unicode sequence '\\uA786' to 'T'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff34)), "T", "This is function is expected to escape the unicode sequence '\\uFF34' to 'T'")


    # tTest
    self.assertEqual(fold_to_ascii.fold(chr(0x163)), "t", "This is function is expected to escape the unicode sequence '\\u0163' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x165)), "t", "This is function is expected to escape the unicode sequence '\\u0165' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x167)), "t", "This is function is expected to escape the unicode sequence '\\u0167' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ab)), "t", "This is function is expected to escape the unicode sequence '\\u01AB' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ad)), "t", "This is function is expected to escape the unicode sequence '\\u01AD' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x21b)), "t", "This is function is expected to escape the unicode sequence '\\u021B' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x236)), "t", "This is function is expected to escape the unicode sequence '\\u0236' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x287)), "t", "This is function is expected to escape the unicode sequence '\\u0287' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x288)), "t", "This is function is expected to escape the unicode sequence '\\u0288' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d75)), "t", "This is function is expected to escape the unicode sequence '\\u1D75' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e6b)), "t", "This is function is expected to escape the unicode sequence '\\u1E6B' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e6d)), "t", "This is function is expected to escape the unicode sequence '\\u1E6D' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e6f)), "t", "This is function is expected to escape the unicode sequence '\\u1E6F' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e71)), "t", "This is function is expected to escape the unicode sequence '\\u1E71' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e97)), "t", "This is function is expected to escape the unicode sequence '\\u1E97' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e3)), "t", "This is function is expected to escape the unicode sequence '\\u24E3' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c66)), "t", "This is function is expected to escape the unicode sequence '\\u2C66' to 't'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff54)), "t", "This is function is expected to escape the unicode sequence '\\uFF54' to 't'")


    # THTest
    self.assertEqual(fold_to_ascii.fold(chr(0xde)), "TH", "This is function is expected to escape the unicode sequence '\\u00DE' to 'TH'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa766)), "TH", "This is function is expected to escape the unicode sequence '\\uA766' to 'TH'")


    # TZTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa728)), "TZ", "This is function is expected to escape the unicode sequence '\\uA728' to 'TZ'")


    # LeftParenthesisLatinSmallLetterTRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24af)), "(t)", "This is function is expected to escape the unicode sequence '\\u24AF' to '(t)'")


    # tcTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2a8)), "tc", "This is function is expected to escape the unicode sequence '\\u02A8' to 'tc'")


    # thTest
    self.assertEqual(fold_to_ascii.fold(chr(0xfe)), "th", "This is function is expected to escape the unicode sequence '\\u00FE' to 'th'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d7a)), "th", "This is function is expected to escape the unicode sequence '\\u1D7A' to 'th'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa767)), "th", "This is function is expected to escape the unicode sequence '\\uA767' to 'th'")


    # tsTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2a6)), "ts", "This is function is expected to escape the unicode sequence '\\u02A6' to 'ts'")


    # tzTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa729)), "tz", "This is function is expected to escape the unicode sequence '\\uA729' to 'tz'")


    # UTest
    self.assertEqual(fold_to_ascii.fold(chr(0xd9)), "U", "This is function is expected to escape the unicode sequence '\\u00D9' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0xda)), "U", "This is function is expected to escape the unicode sequence '\\u00DA' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0xdb)), "U", "This is function is expected to escape the unicode sequence '\\u00DB' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0xdc)), "U", "This is function is expected to escape the unicode sequence '\\u00DC' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x168)), "U", "This is function is expected to escape the unicode sequence '\\u0168' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x16a)), "U", "This is function is expected to escape the unicode sequence '\\u016A' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x16c)), "U", "This is function is expected to escape the unicode sequence '\\u016C' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x16e)), "U", "This is function is expected to escape the unicode sequence '\\u016E' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x170)), "U", "This is function is expected to escape the unicode sequence '\\u0170' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x172)), "U", "This is function is expected to escape the unicode sequence '\\u0172' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1af)), "U", "This is function is expected to escape the unicode sequence '\\u01AF' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d3)), "U", "This is function is expected to escape the unicode sequence '\\u01D3' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d5)), "U", "This is function is expected to escape the unicode sequence '\\u01D5' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d7)), "U", "This is function is expected to escape the unicode sequence '\\u01D7' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d9)), "U", "This is function is expected to escape the unicode sequence '\\u01D9' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1db)), "U", "This is function is expected to escape the unicode sequence '\\u01DB' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x214)), "U", "This is function is expected to escape the unicode sequence '\\u0214' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x216)), "U", "This is function is expected to escape the unicode sequence '\\u0216' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x244)), "U", "This is function is expected to escape the unicode sequence '\\u0244' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d1c)), "U", "This is function is expected to escape the unicode sequence '\\u1D1C' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d7e)), "U", "This is function is expected to escape the unicode sequence '\\u1D7E' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e72)), "U", "This is function is expected to escape the unicode sequence '\\u1E72' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e74)), "U", "This is function is expected to escape the unicode sequence '\\u1E74' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e76)), "U", "This is function is expected to escape the unicode sequence '\\u1E76' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e78)), "U", "This is function is expected to escape the unicode sequence '\\u1E78' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e7a)), "U", "This is function is expected to escape the unicode sequence '\\u1E7A' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee4)), "U", "This is function is expected to escape the unicode sequence '\\u1EE4' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee6)), "U", "This is function is expected to escape the unicode sequence '\\u1EE6' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee8)), "U", "This is function is expected to escape the unicode sequence '\\u1EE8' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eea)), "U", "This is function is expected to escape the unicode sequence '\\u1EEA' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eec)), "U", "This is function is expected to escape the unicode sequence '\\u1EEC' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eee)), "U", "This is function is expected to escape the unicode sequence '\\u1EEE' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef0)), "U", "This is function is expected to escape the unicode sequence '\\u1EF0' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24ca)), "U", "This is function is expected to escape the unicode sequence '\\u24CA' to 'U'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff35)), "U", "This is function is expected to escape the unicode sequence '\\uFF35' to 'U'")


    # uTest
    self.assertEqual(fold_to_ascii.fold(chr(0xf9)), "u", "This is function is expected to escape the unicode sequence '\\u00F9' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0xfa)), "u", "This is function is expected to escape the unicode sequence '\\u00FA' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0xfb)), "u", "This is function is expected to escape the unicode sequence '\\u00FB' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0xfc)), "u", "This is function is expected to escape the unicode sequence '\\u00FC' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x169)), "u", "This is function is expected to escape the unicode sequence '\\u0169' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x16b)), "u", "This is function is expected to escape the unicode sequence '\\u016B' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x16d)), "u", "This is function is expected to escape the unicode sequence '\\u016D' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x16f)), "u", "This is function is expected to escape the unicode sequence '\\u016F' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x171)), "u", "This is function is expected to escape the unicode sequence '\\u0171' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x173)), "u", "This is function is expected to escape the unicode sequence '\\u0173' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1b0)), "u", "This is function is expected to escape the unicode sequence '\\u01B0' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d4)), "u", "This is function is expected to escape the unicode sequence '\\u01D4' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d6)), "u", "This is function is expected to escape the unicode sequence '\\u01D6' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d8)), "u", "This is function is expected to escape the unicode sequence '\\u01D8' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1da)), "u", "This is function is expected to escape the unicode sequence '\\u01DA' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1dc)), "u", "This is function is expected to escape the unicode sequence '\\u01DC' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x215)), "u", "This is function is expected to escape the unicode sequence '\\u0215' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x217)), "u", "This is function is expected to escape the unicode sequence '\\u0217' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x289)), "u", "This is function is expected to escape the unicode sequence '\\u0289' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d64)), "u", "This is function is expected to escape the unicode sequence '\\u1D64' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d99)), "u", "This is function is expected to escape the unicode sequence '\\u1D99' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e73)), "u", "This is function is expected to escape the unicode sequence '\\u1E73' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e75)), "u", "This is function is expected to escape the unicode sequence '\\u1E75' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e77)), "u", "This is function is expected to escape the unicode sequence '\\u1E77' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e79)), "u", "This is function is expected to escape the unicode sequence '\\u1E79' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e7b)), "u", "This is function is expected to escape the unicode sequence '\\u1E7B' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee5)), "u", "This is function is expected to escape the unicode sequence '\\u1EE5' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee7)), "u", "This is function is expected to escape the unicode sequence '\\u1EE7' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ee9)), "u", "This is function is expected to escape the unicode sequence '\\u1EE9' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eeb)), "u", "This is function is expected to escape the unicode sequence '\\u1EEB' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eed)), "u", "This is function is expected to escape the unicode sequence '\\u1EED' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eef)), "u", "This is function is expected to escape the unicode sequence '\\u1EEF' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef1)), "u", "This is function is expected to escape the unicode sequence '\\u1EF1' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e4)), "u", "This is function is expected to escape the unicode sequence '\\u24E4' to 'u'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff55)), "u", "This is function is expected to escape the unicode sequence '\\uFF55' to 'u'")


    # LeftParenthesisLatinSmallLetterURightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24b0)), "(u)", "This is function is expected to escape the unicode sequence '\\u24B0' to '(u)'")


    # ueTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1d6b)), "ue", "This is function is expected to escape the unicode sequence '\\u1D6B' to 'ue'")


    # VTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1b2)), "V", "This is function is expected to escape the unicode sequence '\\u01B2' to 'V'")
    self.assertEqual(fold_to_ascii.fold(chr(0x245)), "V", "This is function is expected to escape the unicode sequence '\\u0245' to 'V'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d20)), "V", "This is function is expected to escape the unicode sequence '\\u1D20' to 'V'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e7c)), "V", "This is function is expected to escape the unicode sequence '\\u1E7C' to 'V'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e7e)), "V", "This is function is expected to escape the unicode sequence '\\u1E7E' to 'V'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1efc)), "V", "This is function is expected to escape the unicode sequence '\\u1EFC' to 'V'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24cb)), "V", "This is function is expected to escape the unicode sequence '\\u24CB' to 'V'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa75e)), "V", "This is function is expected to escape the unicode sequence '\\uA75E' to 'V'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa768)), "V", "This is function is expected to escape the unicode sequence '\\uA768' to 'V'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff36)), "V", "This is function is expected to escape the unicode sequence '\\uFF36' to 'V'")


    # vTest
    self.assertEqual(fold_to_ascii.fold(chr(0x28b)), "v", "This is function is expected to escape the unicode sequence '\\u028B' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0x28c)), "v", "This is function is expected to escape the unicode sequence '\\u028C' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d65)), "v", "This is function is expected to escape the unicode sequence '\\u1D65' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d8c)), "v", "This is function is expected to escape the unicode sequence '\\u1D8C' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e7d)), "v", "This is function is expected to escape the unicode sequence '\\u1E7D' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e7f)), "v", "This is function is expected to escape the unicode sequence '\\u1E7F' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e5)), "v", "This is function is expected to escape the unicode sequence '\\u24E5' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c71)), "v", "This is function is expected to escape the unicode sequence '\\u2C71' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c74)), "v", "This is function is expected to escape the unicode sequence '\\u2C74' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa75f)), "v", "This is function is expected to escape the unicode sequence '\\uA75F' to 'v'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff56)), "v", "This is function is expected to escape the unicode sequence '\\uFF56' to 'v'")


    # VYTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa760)), "VY", "This is function is expected to escape the unicode sequence '\\uA760' to 'VY'")


    # LeftParenthesisLatinSmallLetterVRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24b1)), "(v)", "This is function is expected to escape the unicode sequence '\\u24B1' to '(v)'")


    # vyTest
    self.assertEqual(fold_to_ascii.fold(chr(0xa761)), "vy", "This is function is expected to escape the unicode sequence '\\uA761' to 'vy'")


    # WTest
    self.assertEqual(fold_to_ascii.fold(chr(0x174)), "W", "This is function is expected to escape the unicode sequence '\\u0174' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1f7)), "W", "This is function is expected to escape the unicode sequence '\\u01F7' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d21)), "W", "This is function is expected to escape the unicode sequence '\\u1D21' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e80)), "W", "This is function is expected to escape the unicode sequence '\\u1E80' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e82)), "W", "This is function is expected to escape the unicode sequence '\\u1E82' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e84)), "W", "This is function is expected to escape the unicode sequence '\\u1E84' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e86)), "W", "This is function is expected to escape the unicode sequence '\\u1E86' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e88)), "W", "This is function is expected to escape the unicode sequence '\\u1E88' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24cc)), "W", "This is function is expected to escape the unicode sequence '\\u24CC' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c72)), "W", "This is function is expected to escape the unicode sequence '\\u2C72' to 'W'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff37)), "W", "This is function is expected to escape the unicode sequence '\\uFF37' to 'W'")


    # wTest
    self.assertEqual(fold_to_ascii.fold(chr(0x175)), "w", "This is function is expected to escape the unicode sequence '\\u0175' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1bf)), "w", "This is function is expected to escape the unicode sequence '\\u01BF' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x28d)), "w", "This is function is expected to escape the unicode sequence '\\u028D' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e81)), "w", "This is function is expected to escape the unicode sequence '\\u1E81' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e83)), "w", "This is function is expected to escape the unicode sequence '\\u1E83' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e85)), "w", "This is function is expected to escape the unicode sequence '\\u1E85' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e87)), "w", "This is function is expected to escape the unicode sequence '\\u1E87' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e89)), "w", "This is function is expected to escape the unicode sequence '\\u1E89' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e98)), "w", "This is function is expected to escape the unicode sequence '\\u1E98' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e6)), "w", "This is function is expected to escape the unicode sequence '\\u24E6' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c73)), "w", "This is function is expected to escape the unicode sequence '\\u2C73' to 'w'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff57)), "w", "This is function is expected to escape the unicode sequence '\\uFF57' to 'w'")


    # LeftParenthesisLatinSmallLetterWRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24b2)), "(w)", "This is function is expected to escape the unicode sequence '\\u24B2' to '(w)'")


    # XTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1e8a)), "X", "This is function is expected to escape the unicode sequence '\\u1E8A' to 'X'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e8c)), "X", "This is function is expected to escape the unicode sequence '\\u1E8C' to 'X'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24cd)), "X", "This is function is expected to escape the unicode sequence '\\u24CD' to 'X'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff38)), "X", "This is function is expected to escape the unicode sequence '\\uFF38' to 'X'")


    # xTest
    self.assertEqual(fold_to_ascii.fold(chr(0x1d8d)), "x", "This is function is expected to escape the unicode sequence '\\u1D8D' to 'x'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e8b)), "x", "This is function is expected to escape the unicode sequence '\\u1E8B' to 'x'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e8d)), "x", "This is function is expected to escape the unicode sequence '\\u1E8D' to 'x'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2093)), "x", "This is function is expected to escape the unicode sequence '\\u2093' to 'x'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e7)), "x", "This is function is expected to escape the unicode sequence '\\u24E7' to 'x'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff58)), "x", "This is function is expected to escape the unicode sequence '\\uFF58' to 'x'")


    # LeftParenthesisLatinSmallLetterXRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24b3)), "(x)", "This is function is expected to escape the unicode sequence '\\u24B3' to '(x)'")


    # YTest
    self.assertEqual(fold_to_ascii.fold(chr(0xdd)), "Y", "This is function is expected to escape the unicode sequence '\\u00DD' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x176)), "Y", "This is function is expected to escape the unicode sequence '\\u0176' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x178)), "Y", "This is function is expected to escape the unicode sequence '\\u0178' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1b3)), "Y", "This is function is expected to escape the unicode sequence '\\u01B3' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x232)), "Y", "This is function is expected to escape the unicode sequence '\\u0232' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e)), "Y", "This is function is expected to escape the unicode sequence '\\u024E' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x28f)), "Y", "This is function is expected to escape the unicode sequence '\\u028F' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e8e)), "Y", "This is function is expected to escape the unicode sequence '\\u1E8E' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef2)), "Y", "This is function is expected to escape the unicode sequence '\\u1EF2' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef4)), "Y", "This is function is expected to escape the unicode sequence '\\u1EF4' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef6)), "Y", "This is function is expected to escape the unicode sequence '\\u1EF6' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef8)), "Y", "This is function is expected to escape the unicode sequence '\\u1EF8' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1efe)), "Y", "This is function is expected to escape the unicode sequence '\\u1EFE' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24ce)), "Y", "This is function is expected to escape the unicode sequence '\\u24CE' to 'Y'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff39)), "Y", "This is function is expected to escape the unicode sequence '\\uFF39' to 'Y'")


    # yTest
    self.assertEqual(fold_to_ascii.fold(chr(0xfd)), "y", "This is function is expected to escape the unicode sequence '\\u00FD' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff)), "y", "This is function is expected to escape the unicode sequence '\\u00FF' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x177)), "y", "This is function is expected to escape the unicode sequence '\\u0177' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1b4)), "y", "This is function is expected to escape the unicode sequence '\\u01B4' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x233)), "y", "This is function is expected to escape the unicode sequence '\\u0233' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f)), "y", "This is function is expected to escape the unicode sequence '\\u024F' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x28e)), "y", "This is function is expected to escape the unicode sequence '\\u028E' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e8f)), "y", "This is function is expected to escape the unicode sequence '\\u1E8F' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e99)), "y", "This is function is expected to escape the unicode sequence '\\u1E99' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef3)), "y", "This is function is expected to escape the unicode sequence '\\u1EF3' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef5)), "y", "This is function is expected to escape the unicode sequence '\\u1EF5' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef7)), "y", "This is function is expected to escape the unicode sequence '\\u1EF7' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1ef9)), "y", "This is function is expected to escape the unicode sequence '\\u1EF9' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1eff)), "y", "This is function is expected to escape the unicode sequence '\\u1EFF' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e8)), "y", "This is function is expected to escape the unicode sequence '\\u24E8' to 'y'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff59)), "y", "This is function is expected to escape the unicode sequence '\\uFF59' to 'y'")


    # LeftParenthesisLatinSmallLetterYRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24b4)), "(y)", "This is function is expected to escape the unicode sequence '\\u24B4' to '(y)'")


    # ZTest
    self.assertEqual(fold_to_ascii.fold(chr(0x179)), "Z", "This is function is expected to escape the unicode sequence '\\u0179' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x17b)), "Z", "This is function is expected to escape the unicode sequence '\\u017B' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x17d)), "Z", "This is function is expected to escape the unicode sequence '\\u017D' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1b5)), "Z", "This is function is expected to escape the unicode sequence '\\u01B5' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x21c)), "Z", "This is function is expected to escape the unicode sequence '\\u021C' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x224)), "Z", "This is function is expected to escape the unicode sequence '\\u0224' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d22)), "Z", "This is function is expected to escape the unicode sequence '\\u1D22' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e90)), "Z", "This is function is expected to escape the unicode sequence '\\u1E90' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e92)), "Z", "This is function is expected to escape the unicode sequence '\\u1E92' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e94)), "Z", "This is function is expected to escape the unicode sequence '\\u1E94' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24cf)), "Z", "This is function is expected to escape the unicode sequence '\\u24CF' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c6b)), "Z", "This is function is expected to escape the unicode sequence '\\u2C6B' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa762)), "Z", "This is function is expected to escape the unicode sequence '\\uA762' to 'Z'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff3a)), "Z", "This is function is expected to escape the unicode sequence '\\uFF3A' to 'Z'")


    # zTest
    self.assertEqual(fold_to_ascii.fold(chr(0x17a)), "z", "This is function is expected to escape the unicode sequence '\\u017A' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x17c)), "z", "This is function is expected to escape the unicode sequence '\\u017C' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x17e)), "z", "This is function is expected to escape the unicode sequence '\\u017E' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1b6)), "z", "This is function is expected to escape the unicode sequence '\\u01B6' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x21d)), "z", "This is function is expected to escape the unicode sequence '\\u021D' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x225)), "z", "This is function is expected to escape the unicode sequence '\\u0225' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x240)), "z", "This is function is expected to escape the unicode sequence '\\u0240' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x290)), "z", "This is function is expected to escape the unicode sequence '\\u0290' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x291)), "z", "This is function is expected to escape the unicode sequence '\\u0291' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d76)), "z", "This is function is expected to escape the unicode sequence '\\u1D76' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1d8e)), "z", "This is function is expected to escape the unicode sequence '\\u1D8E' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e91)), "z", "This is function is expected to escape the unicode sequence '\\u1E91' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e93)), "z", "This is function is expected to escape the unicode sequence '\\u1E93' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x1e95)), "z", "This is function is expected to escape the unicode sequence '\\u1E95' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24e9)), "z", "This is function is expected to escape the unicode sequence '\\u24E9' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2c6c)), "z", "This is function is expected to escape the unicode sequence '\\u2C6C' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0xa763)), "z", "This is function is expected to escape the unicode sequence '\\uA763' to 'z'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff5a)), "z", "This is function is expected to escape the unicode sequence '\\uFF5A' to 'z'")


    # LeftParenthesisLatinSmallLetterZRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x24b5)), "(z)", "This is function is expected to escape the unicode sequence '\\u24B5' to '(z)'")


    # 0Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2070)), "0", "This is function is expected to escape the unicode sequence '\\u2070' to '0'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2080)), "0", "This is function is expected to escape the unicode sequence '\\u2080' to '0'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24ea)), "0", "This is function is expected to escape the unicode sequence '\\u24EA' to '0'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24ff)), "0", "This is function is expected to escape the unicode sequence '\\u24FF' to '0'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff10)), "0", "This is function is expected to escape the unicode sequence '\\uFF10' to '0'")


    # 1Test
    self.assertEqual(fold_to_ascii.fold(chr(0xb9)), "1", "This is function is expected to escape the unicode sequence '\\u00B9' to '1'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2081)), "1", "This is function is expected to escape the unicode sequence '\\u2081' to '1'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2460)), "1", "This is function is expected to escape the unicode sequence '\\u2460' to '1'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f5)), "1", "This is function is expected to escape the unicode sequence '\\u24F5' to '1'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2776)), "1", "This is function is expected to escape the unicode sequence '\\u2776' to '1'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2780)), "1", "This is function is expected to escape the unicode sequence '\\u2780' to '1'")
    self.assertEqual(fold_to_ascii.fold(chr(0x278a)), "1", "This is function is expected to escape the unicode sequence '\\u278A' to '1'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff11)), "1", "This is function is expected to escape the unicode sequence '\\uFF11' to '1'")


    # DigitOneFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2488)), "1.", "This is function is expected to escape the unicode sequence '\\u2488' to '1.'")


    # LeftParenthesisDigitOneRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2474)), "(1)", "This is function is expected to escape the unicode sequence '\\u2474' to '(1)'")


    # 2Test
    self.assertEqual(fold_to_ascii.fold(chr(0xb2)), "2", "This is function is expected to escape the unicode sequence '\\u00B2' to '2'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2082)), "2", "This is function is expected to escape the unicode sequence '\\u2082' to '2'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2461)), "2", "This is function is expected to escape the unicode sequence '\\u2461' to '2'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f6)), "2", "This is function is expected to escape the unicode sequence '\\u24F6' to '2'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2777)), "2", "This is function is expected to escape the unicode sequence '\\u2777' to '2'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2781)), "2", "This is function is expected to escape the unicode sequence '\\u2781' to '2'")
    self.assertEqual(fold_to_ascii.fold(chr(0x278b)), "2", "This is function is expected to escape the unicode sequence '\\u278B' to '2'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff12)), "2", "This is function is expected to escape the unicode sequence '\\uFF12' to '2'")


    # DigitTwoFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2489)), "2.", "This is function is expected to escape the unicode sequence '\\u2489' to '2.'")


    # LeftParenthesisDigitTwoRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2475)), "(2)", "This is function is expected to escape the unicode sequence '\\u2475' to '(2)'")


    # 3Test
    self.assertEqual(fold_to_ascii.fold(chr(0xb3)), "3", "This is function is expected to escape the unicode sequence '\\u00B3' to '3'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2083)), "3", "This is function is expected to escape the unicode sequence '\\u2083' to '3'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2462)), "3", "This is function is expected to escape the unicode sequence '\\u2462' to '3'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f7)), "3", "This is function is expected to escape the unicode sequence '\\u24F7' to '3'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2778)), "3", "This is function is expected to escape the unicode sequence '\\u2778' to '3'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2782)), "3", "This is function is expected to escape the unicode sequence '\\u2782' to '3'")
    self.assertEqual(fold_to_ascii.fold(chr(0x278c)), "3", "This is function is expected to escape the unicode sequence '\\u278C' to '3'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff13)), "3", "This is function is expected to escape the unicode sequence '\\uFF13' to '3'")


    # DigitThreeFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x248a)), "3.", "This is function is expected to escape the unicode sequence '\\u248A' to '3.'")


    # LeftParenthesisDigitThreeRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2476)), "(3)", "This is function is expected to escape the unicode sequence '\\u2476' to '(3)'")


    # 4Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2074)), "4", "This is function is expected to escape the unicode sequence '\\u2074' to '4'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2084)), "4", "This is function is expected to escape the unicode sequence '\\u2084' to '4'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2463)), "4", "This is function is expected to escape the unicode sequence '\\u2463' to '4'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f8)), "4", "This is function is expected to escape the unicode sequence '\\u24F8' to '4'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2779)), "4", "This is function is expected to escape the unicode sequence '\\u2779' to '4'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2783)), "4", "This is function is expected to escape the unicode sequence '\\u2783' to '4'")
    self.assertEqual(fold_to_ascii.fold(chr(0x278d)), "4", "This is function is expected to escape the unicode sequence '\\u278D' to '4'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff14)), "4", "This is function is expected to escape the unicode sequence '\\uFF14' to '4'")


    # DigitFourFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x248b)), "4.", "This is function is expected to escape the unicode sequence '\\u248B' to '4.'")


    # LeftParenthesisDigitFourRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2477)), "(4)", "This is function is expected to escape the unicode sequence '\\u2477' to '(4)'")


    # 5Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2075)), "5", "This is function is expected to escape the unicode sequence '\\u2075' to '5'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2085)), "5", "This is function is expected to escape the unicode sequence '\\u2085' to '5'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2464)), "5", "This is function is expected to escape the unicode sequence '\\u2464' to '5'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f9)), "5", "This is function is expected to escape the unicode sequence '\\u24F9' to '5'")
    self.assertEqual(fold_to_ascii.fold(chr(0x277a)), "5", "This is function is expected to escape the unicode sequence '\\u277A' to '5'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2784)), "5", "This is function is expected to escape the unicode sequence '\\u2784' to '5'")
    self.assertEqual(fold_to_ascii.fold(chr(0x278e)), "5", "This is function is expected to escape the unicode sequence '\\u278E' to '5'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff15)), "5", "This is function is expected to escape the unicode sequence '\\uFF15' to '5'")


    # DigitFiveFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x248c)), "5.", "This is function is expected to escape the unicode sequence '\\u248C' to '5.'")


    # LeftParenthesisDigitFiveRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2478)), "(5)", "This is function is expected to escape the unicode sequence '\\u2478' to '(5)'")


    # 6Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2076)), "6", "This is function is expected to escape the unicode sequence '\\u2076' to '6'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2086)), "6", "This is function is expected to escape the unicode sequence '\\u2086' to '6'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2465)), "6", "This is function is expected to escape the unicode sequence '\\u2465' to '6'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24fa)), "6", "This is function is expected to escape the unicode sequence '\\u24FA' to '6'")
    self.assertEqual(fold_to_ascii.fold(chr(0x277b)), "6", "This is function is expected to escape the unicode sequence '\\u277B' to '6'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2785)), "6", "This is function is expected to escape the unicode sequence '\\u2785' to '6'")
    self.assertEqual(fold_to_ascii.fold(chr(0x278f)), "6", "This is function is expected to escape the unicode sequence '\\u278F' to '6'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff16)), "6", "This is function is expected to escape the unicode sequence '\\uFF16' to '6'")


    # DigitSixFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x248d)), "6.", "This is function is expected to escape the unicode sequence '\\u248D' to '6.'")


    # LeftParenthesisDigitSixRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2479)), "(6)", "This is function is expected to escape the unicode sequence '\\u2479' to '(6)'")


    # 7Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2077)), "7", "This is function is expected to escape the unicode sequence '\\u2077' to '7'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2087)), "7", "This is function is expected to escape the unicode sequence '\\u2087' to '7'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2466)), "7", "This is function is expected to escape the unicode sequence '\\u2466' to '7'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24fb)), "7", "This is function is expected to escape the unicode sequence '\\u24FB' to '7'")
    self.assertEqual(fold_to_ascii.fold(chr(0x277c)), "7", "This is function is expected to escape the unicode sequence '\\u277C' to '7'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2786)), "7", "This is function is expected to escape the unicode sequence '\\u2786' to '7'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2790)), "7", "This is function is expected to escape the unicode sequence '\\u2790' to '7'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff17)), "7", "This is function is expected to escape the unicode sequence '\\uFF17' to '7'")


    # DigitSevenFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x248e)), "7.", "This is function is expected to escape the unicode sequence '\\u248E' to '7.'")


    # LeftParenthesisDigitSevenRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x247a)), "(7)", "This is function is expected to escape the unicode sequence '\\u247A' to '(7)'")


    # 8Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2078)), "8", "This is function is expected to escape the unicode sequence '\\u2078' to '8'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2088)), "8", "This is function is expected to escape the unicode sequence '\\u2088' to '8'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2467)), "8", "This is function is expected to escape the unicode sequence '\\u2467' to '8'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24fc)), "8", "This is function is expected to escape the unicode sequence '\\u24FC' to '8'")
    self.assertEqual(fold_to_ascii.fold(chr(0x277d)), "8", "This is function is expected to escape the unicode sequence '\\u277D' to '8'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2787)), "8", "This is function is expected to escape the unicode sequence '\\u2787' to '8'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2791)), "8", "This is function is expected to escape the unicode sequence '\\u2791' to '8'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff18)), "8", "This is function is expected to escape the unicode sequence '\\uFF18' to '8'")


    # DigitEightFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x248f)), "8.", "This is function is expected to escape the unicode sequence '\\u248F' to '8.'")


    # LeftParenthesisDigitEightRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x247b)), "(8)", "This is function is expected to escape the unicode sequence '\\u247B' to '(8)'")


    # 9Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2079)), "9", "This is function is expected to escape the unicode sequence '\\u2079' to '9'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2089)), "9", "This is function is expected to escape the unicode sequence '\\u2089' to '9'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2468)), "9", "This is function is expected to escape the unicode sequence '\\u2468' to '9'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24fd)), "9", "This is function is expected to escape the unicode sequence '\\u24FD' to '9'")
    self.assertEqual(fold_to_ascii.fold(chr(0x277e)), "9", "This is function is expected to escape the unicode sequence '\\u277E' to '9'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2788)), "9", "This is function is expected to escape the unicode sequence '\\u2788' to '9'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2792)), "9", "This is function is expected to escape the unicode sequence '\\u2792' to '9'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff19)), "9", "This is function is expected to escape the unicode sequence '\\uFF19' to '9'")


    # DigitNineFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2490)), "9.", "This is function is expected to escape the unicode sequence '\\u2490' to '9.'")


    # LeftParenthesisDigitNineRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x247c)), "(9)", "This is function is expected to escape the unicode sequence '\\u247C' to '(9)'")


    # 10Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2469)), "10", "This is function is expected to escape the unicode sequence '\\u2469' to '10'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24fe)), "10", "This is function is expected to escape the unicode sequence '\\u24FE' to '10'")
    self.assertEqual(fold_to_ascii.fold(chr(0x277f)), "10", "This is function is expected to escape the unicode sequence '\\u277F' to '10'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2789)), "10", "This is function is expected to escape the unicode sequence '\\u2789' to '10'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2793)), "10", "This is function is expected to escape the unicode sequence '\\u2793' to '10'")


    # DigitOneDigitZeroFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2491)), "10.", "This is function is expected to escape the unicode sequence '\\u2491' to '10.'")


    # LeftParenthesisDigitOneDigitZeroRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x247d)), "(10)", "This is function is expected to escape the unicode sequence '\\u247D' to '(10)'")


    # 11Test
    self.assertEqual(fold_to_ascii.fold(chr(0x246a)), "11", "This is function is expected to escape the unicode sequence '\\u246A' to '11'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24eb)), "11", "This is function is expected to escape the unicode sequence '\\u24EB' to '11'")


    # DigitOneDigitOneFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2492)), "11.", "This is function is expected to escape the unicode sequence '\\u2492' to '11.'")


    # LeftParenthesisDigitOneDigitOneRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x247e)), "(11)", "This is function is expected to escape the unicode sequence '\\u247E' to '(11)'")


    # 12Test
    self.assertEqual(fold_to_ascii.fold(chr(0x246b)), "12", "This is function is expected to escape the unicode sequence '\\u246B' to '12'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24ec)), "12", "This is function is expected to escape the unicode sequence '\\u24EC' to '12'")


    # DigitOneDigitTwoFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2493)), "12.", "This is function is expected to escape the unicode sequence '\\u2493' to '12.'")


    # LeftParenthesisDigitOneDigitTwoRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x247f)), "(12)", "This is function is expected to escape the unicode sequence '\\u247F' to '(12)'")


    # 13Test
    self.assertEqual(fold_to_ascii.fold(chr(0x246c)), "13", "This is function is expected to escape the unicode sequence '\\u246C' to '13'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24ed)), "13", "This is function is expected to escape the unicode sequence '\\u24ED' to '13'")


    # DigitOneDigitThreeFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2494)), "13.", "This is function is expected to escape the unicode sequence '\\u2494' to '13.'")


    # LeftParenthesisDigitOneDigitThreeRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2480)), "(13)", "This is function is expected to escape the unicode sequence '\\u2480' to '(13)'")


    # 14Test
    self.assertEqual(fold_to_ascii.fold(chr(0x246d)), "14", "This is function is expected to escape the unicode sequence '\\u246D' to '14'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24ee)), "14", "This is function is expected to escape the unicode sequence '\\u24EE' to '14'")


    # DigitOneDigitFourFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2495)), "14.", "This is function is expected to escape the unicode sequence '\\u2495' to '14.'")


    # LeftParenthesisDigitOneDigitFourRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2481)), "(14)", "This is function is expected to escape the unicode sequence '\\u2481' to '(14)'")


    # 15Test
    self.assertEqual(fold_to_ascii.fold(chr(0x246e)), "15", "This is function is expected to escape the unicode sequence '\\u246E' to '15'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24ef)), "15", "This is function is expected to escape the unicode sequence '\\u24EF' to '15'")


    # DigitOneDigitFiveFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2496)), "15.", "This is function is expected to escape the unicode sequence '\\u2496' to '15.'")


    # LeftParenthesisDigitOneDigitFiveRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2482)), "(15)", "This is function is expected to escape the unicode sequence '\\u2482' to '(15)'")


    # 16Test
    self.assertEqual(fold_to_ascii.fold(chr(0x246f)), "16", "This is function is expected to escape the unicode sequence '\\u246F' to '16'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f0)), "16", "This is function is expected to escape the unicode sequence '\\u24F0' to '16'")


    # DigitOneDigitSixFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2497)), "16.", "This is function is expected to escape the unicode sequence '\\u2497' to '16.'")


    # LeftParenthesisDigitOneDigitSixRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2483)), "(16)", "This is function is expected to escape the unicode sequence '\\u2483' to '(16)'")


    # 17Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2470)), "17", "This is function is expected to escape the unicode sequence '\\u2470' to '17'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f1)), "17", "This is function is expected to escape the unicode sequence '\\u24F1' to '17'")


    # DigitOneDigitSevenFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2498)), "17.", "This is function is expected to escape the unicode sequence '\\u2498' to '17.'")


    # LeftParenthesisDigitOneDigitSevenRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2484)), "(17)", "This is function is expected to escape the unicode sequence '\\u2484' to '(17)'")


    # 18Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2471)), "18", "This is function is expected to escape the unicode sequence '\\u2471' to '18'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f2)), "18", "This is function is expected to escape the unicode sequence '\\u24F2' to '18'")


    # DigitOneDigitEightFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2499)), "18.", "This is function is expected to escape the unicode sequence '\\u2499' to '18.'")


    # LeftParenthesisDigitOneDigitEightRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2485)), "(18)", "This is function is expected to escape the unicode sequence '\\u2485' to '(18)'")


    # 19Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2472)), "19", "This is function is expected to escape the unicode sequence '\\u2472' to '19'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f3)), "19", "This is function is expected to escape the unicode sequence '\\u24F3' to '19'")


    # DigitOneDigitNineFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x249a)), "19.", "This is function is expected to escape the unicode sequence '\\u249A' to '19.'")


    # LeftParenthesisDigitOneDigitNineRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2486)), "(19)", "This is function is expected to escape the unicode sequence '\\u2486' to '(19)'")


    # 20Test
    self.assertEqual(fold_to_ascii.fold(chr(0x2473)), "20", "This is function is expected to escape the unicode sequence '\\u2473' to '20'")
    self.assertEqual(fold_to_ascii.fold(chr(0x24f4)), "20", "This is function is expected to escape the unicode sequence '\\u24F4' to '20'")


    # DigitTwoDigitZeroFullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0x249b)), "20.", "This is function is expected to escape the unicode sequence '\\u249B' to '20.'")


    # LeftParenthesisDigitTwoDigitZeroRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2487)), "(20)", "This is function is expected to escape the unicode sequence '\\u2487' to '(20)'")


    # QuotationMarkTest
    self.assertEqual(fold_to_ascii.fold(chr(0xab)), "\"", "This is function is expected to escape the unicode sequence '\\u00AB' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0xbb)), "\"", "This is function is expected to escape the unicode sequence '\\u00BB' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0x201c)), "\"", "This is function is expected to escape the unicode sequence '\\u201C' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0x201d)), "\"", "This is function is expected to escape the unicode sequence '\\u201D' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0x201e)), "\"", "This is function is expected to escape the unicode sequence '\\u201E' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2033)), "\"", "This is function is expected to escape the unicode sequence '\\u2033' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2036)), "\"", "This is function is expected to escape the unicode sequence '\\u2036' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0x275d)), "\"", "This is function is expected to escape the unicode sequence '\\u275D' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0x275e)), "\"", "This is function is expected to escape the unicode sequence '\\u275E' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0x276e)), "\"", "This is function is expected to escape the unicode sequence '\\u276E' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0x276f)), "\"", "This is function is expected to escape the unicode sequence '\\u276F' to '\"'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff02)), "\"", "This is function is expected to escape the unicode sequence '\\uFF02' to '\"'")


    # ApostropheTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2018)), "'", "This is function is expected to escape the unicode sequence '\\u2018' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0x2019)), "'", "This is function is expected to escape the unicode sequence '\\u2019' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0x201a)), "'", "This is function is expected to escape the unicode sequence '\\u201A' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0x201b)), "'", "This is function is expected to escape the unicode sequence '\\u201B' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0x2032)), "'", "This is function is expected to escape the unicode sequence '\\u2032' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0x2035)), "'", "This is function is expected to escape the unicode sequence '\\u2035' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0x2039)), "'", "This is function is expected to escape the unicode sequence '\\u2039' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0x203a)), "'", "This is function is expected to escape the unicode sequence '\\u203A' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0x275b)), "'", "This is function is expected to escape the unicode sequence '\\u275B' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0x275c)), "'", "This is function is expected to escape the unicode sequence '\\u275C' to '''")
    self.assertEqual(fold_to_ascii.fold(chr(0xff07)), "'", "This is function is expected to escape the unicode sequence '\\uFF07' to '''")


    # Hyphen-minusTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2010)), "-", "This is function is expected to escape the unicode sequence '\\u2010' to '-'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2011)), "-", "This is function is expected to escape the unicode sequence '\\u2011' to '-'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2012)), "-", "This is function is expected to escape the unicode sequence '\\u2012' to '-'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2013)), "-", "This is function is expected to escape the unicode sequence '\\u2013' to '-'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2014)), "-", "This is function is expected to escape the unicode sequence '\\u2014' to '-'")
    self.assertEqual(fold_to_ascii.fold(chr(0x207b)), "-", "This is function is expected to escape the unicode sequence '\\u207B' to '-'")
    self.assertEqual(fold_to_ascii.fold(chr(0x208b)), "-", "This is function is expected to escape the unicode sequence '\\u208B' to '-'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff0d)), "-", "This is function is expected to escape the unicode sequence '\\uFF0D' to '-'")


    # LeftSquareBracketTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2045)), "[", "This is function is expected to escape the unicode sequence '\\u2045' to '['")
    self.assertEqual(fold_to_ascii.fold(chr(0x2772)), "[", "This is function is expected to escape the unicode sequence '\\u2772' to '['")
    self.assertEqual(fold_to_ascii.fold(chr(0xff3b)), "[", "This is function is expected to escape the unicode sequence '\\uFF3B' to '['")


    # RightSquareBracketTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2046)), "]", "This is function is expected to escape the unicode sequence '\\u2046' to ']'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2773)), "]", "This is function is expected to escape the unicode sequence '\\u2773' to ']'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff3d)), "]", "This is function is expected to escape the unicode sequence '\\uFF3D' to ']'")


    # LeftParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x207d)), "(", "This is function is expected to escape the unicode sequence '\\u207D' to '('")
    self.assertEqual(fold_to_ascii.fold(chr(0x208d)), "(", "This is function is expected to escape the unicode sequence '\\u208D' to '('")
    self.assertEqual(fold_to_ascii.fold(chr(0x2768)), "(", "This is function is expected to escape the unicode sequence '\\u2768' to '('")
    self.assertEqual(fold_to_ascii.fold(chr(0x276a)), "(", "This is function is expected to escape the unicode sequence '\\u276A' to '('")
    self.assertEqual(fold_to_ascii.fold(chr(0xff08)), "(", "This is function is expected to escape the unicode sequence '\\uFF08' to '('")


    # LeftParenthesisLeftParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2e28)), "((", "This is function is expected to escape the unicode sequence '\\u2E28' to '(('")


    # RightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x207e)), ")", "This is function is expected to escape the unicode sequence '\\u207E' to ')'")
    self.assertEqual(fold_to_ascii.fold(chr(0x208e)), ")", "This is function is expected to escape the unicode sequence '\\u208E' to ')'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2769)), ")", "This is function is expected to escape the unicode sequence '\\u2769' to ')'")
    self.assertEqual(fold_to_ascii.fold(chr(0x276b)), ")", "This is function is expected to escape the unicode sequence '\\u276B' to ')'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff09)), ")", "This is function is expected to escape the unicode sequence '\\uFF09' to ')'")


    # RightParenthesisRightParenthesisTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2e29)), "))", "This is function is expected to escape the unicode sequence '\\u2E29' to '))'")


    # Less-thanSignTest
    self.assertEqual(fold_to_ascii.fold(chr(0x276c)), "<", "This is function is expected to escape the unicode sequence '\\u276C' to '<'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2770)), "<", "This is function is expected to escape the unicode sequence '\\u2770' to '<'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff1c)), "<", "This is function is expected to escape the unicode sequence '\\uFF1C' to '<'")


    # Greater-thanSignTest
    self.assertEqual(fold_to_ascii.fold(chr(0x276d)), ">", "This is function is expected to escape the unicode sequence '\\u276D' to '>'")
    self.assertEqual(fold_to_ascii.fold(chr(0x2771)), ">", "This is function is expected to escape the unicode sequence '\\u2771' to '>'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff1e)), ">", "This is function is expected to escape the unicode sequence '\\uFF1E' to '>'")


    # LeftCurlyBracketTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2774)), "{", "This is function is expected to escape the unicode sequence '\\u2774' to '{'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff5b)), "{", "This is function is expected to escape the unicode sequence '\\uFF5B' to '{'")


    # RightCurlyBracketTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2775)), "}", "This is function is expected to escape the unicode sequence '\\u2775' to '}'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff5d)), "}", "This is function is expected to escape the unicode sequence '\\uFF5D' to '}'")


    # PlusSignTest
    self.assertEqual(fold_to_ascii.fold(chr(0x207a)), "+", "This is function is expected to escape the unicode sequence '\\u207A' to '+'")
    self.assertEqual(fold_to_ascii.fold(chr(0x208a)), "+", "This is function is expected to escape the unicode sequence '\\u208A' to '+'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff0b)), "+", "This is function is expected to escape the unicode sequence '\\uFF0B' to '+'")


    # Self.AssertEqualsSignTest
    self.assertEqual(fold_to_ascii.fold(chr(0x207c)), "=", "This is function is expected to escape the unicode sequence '\\u207C' to '='")
    self.assertEqual(fold_to_ascii.fold(chr(0x208c)), "=", "This is function is expected to escape the unicode sequence '\\u208C' to '='")
    self.assertEqual(fold_to_ascii.fold(chr(0xff1d)), "=", "This is function is expected to escape the unicode sequence '\\uFF1D' to '='")


    # ExclamationMarkTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff01)), "!", "This is function is expected to escape the unicode sequence '\\uFF01' to '!'")


    # ExclamationMarkExclamationMarkTest
    self.assertEqual(fold_to_ascii.fold(chr(0x203c)), "!!", "This is function is expected to escape the unicode sequence '\\u203C' to '!!'")


    # ExclamationMarkQuestionMarkTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2049)), "!?", "This is function is expected to escape the unicode sequence '\\u2049' to '!?'")


    # NumberSignTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff03)), "#", "This is function is expected to escape the unicode sequence '\\uFF03' to '#'")


    # DollarSignTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff04)), "$", "This is function is expected to escape the unicode sequence '\\uFF04' to '$'")


    # PercentSignTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2052)), "%", "This is function is expected to escape the unicode sequence '\\u2052' to '%'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff05)), "%", "This is function is expected to escape the unicode sequence '\\uFF05' to '%'")


    # AmpersandTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff06)), "&", "This is function is expected to escape the unicode sequence '\\uFF06' to '&'")


    # AsteriskTest
    self.assertEqual(fold_to_ascii.fold(chr(0x204e)), "*", "This is function is expected to escape the unicode sequence '\\u204E' to '*'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff0a)), "*", "This is function is expected to escape the unicode sequence '\\uFF0A' to '*'")


    # CommaTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff0c)), ",", "This is function is expected to escape the unicode sequence '\\uFF0C' to ','")


    # FullStopTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff0e)), ".", "This is function is expected to escape the unicode sequence '\\uFF0E' to '.'")


    # SolidusTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2044)), "/", "This is function is expected to escape the unicode sequence '\\u2044' to '\/'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff0f)), "/", "This is function is expected to escape the unicode sequence '\\uFF0F' to '\/'")


    # ColonTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff1a)), ":", "This is function is expected to escape the unicode sequence '\\uFF1A' to ':'")


    # SemicolonTest
    self.assertEqual(fold_to_ascii.fold(chr(0x204f)), ";", "This is function is expected to escape the unicode sequence '\\u204F' to ';'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff1b)), ";", "This is function is expected to escape the unicode sequence '\\uFF1B' to ';'")


    # QuestionMarkTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff1f)), "?", "This is function is expected to escape the unicode sequence '\\uFF1F' to '?'")


    # QuestionMarkQuestionMarkTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2047)), "??", "This is function is expected to escape the unicode sequence '\\u2047' to '??'")


    # QuestionMarkExclamationMarkTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2048)), "?!", "This is function is expected to escape the unicode sequence '\\u2048' to '?!'")


    # CommercialAtTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff20)), "@", "This is function is expected to escape the unicode sequence '\\uFF20' to '@'")


    # ReverseSolidusReverseSolidusTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff3c)), "\\", "This is function is expected to escape the unicode sequence '\\uFF3C\" to '\\'")


    # CircumflexAccentTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2038)), "^", "This is function is expected to escape the unicode sequence '\\u2038' to '^'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff3e)), "^", "This is function is expected to escape the unicode sequence '\\uFF3E' to '^'")


    # LowLineTest
    self.assertEqual(fold_to_ascii.fold(chr(0xff3f)), "_", "This is function is expected to escape the unicode sequence '\\uFF3F' to '_'")


    # TildeTest
    self.assertEqual(fold_to_ascii.fold(chr(0x2053)), "~", "This is function is expected to escape the unicode sequence '\\u2053' to '~'")
    self.assertEqual(fold_to_ascii.fold(chr(0xff5e)), "~", "This is function is expected to escape the unicode sequence '\\uFF5E' to '~'")
