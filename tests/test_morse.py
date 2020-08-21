#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# flake8: noqa
"""
Unit tests for Morse Code Decoder.

Students should not modify this file.
"""
__author__ = 'madarp'

import sys
import unittest
import importlib
import subprocess


# Kenzie devs: change this to 'soln.morse' to test solution
PKG_NAME = 'morse'

# some handy morse strings
# HEY JUDE
morse_hey_jude = '.... . -.--   .--- ..- -.. .'
# THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
morse_quick_fox = '- .... .  --.- ..- .. -.-. -.-  -... .-. --- .-- -.  ..-. --- -..-  .--- ..- -- .--. ...  --- ...- . .-.  - .... .  .-.. .- --.. -.--  -.. --- --. .-.-.-'


class TestDecodeMorse(unittest.TestCase):
    """Only tests the decode_morse() function"""

    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        cls.module = importlib.import_module(PKG_NAME)

    def test_hey_jude(self):
        """Check basic HEY JUDE"""
        actual = self.module.decode_morse(morse_hey_jude)
        self.assertEqual(actual, 'HEY JUDE')

    def test_basic_letters(self):
        """Check Basic Morse decoding"""
        self.assertEqual(self.module.decode_morse('.-'), 'A')
        self.assertEqual(self.module.decode_morse('.'), 'E')
        self.assertEqual(self.module.decode_morse('..'), 'I')
        self.assertEqual(self.module.decode_morse('. .'), 'EE')
        self.assertEqual(self.module.decode_morse('.   .'), 'E E')
        self.assertEqual(self.module.decode_morse('...---...'), 'SOS')
        self.assertEqual(self.module.decode_morse('... --- ...'), 'SOS')
        self.assertEqual(self.module.decode_morse('...   ---   ...'), 'S O S')

    def test_extra_spaces(self):
        """Check handling of spaces"""
        self.assertEqual(self.module.decode_morse(' . '), 'E')
        self.assertEqual(self.module.decode_morse('   .   . '), 'E E')

    def test_complex(self):
        """Check long message decoding"""
        morse = '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .  '            ' .-.. .- --.. -.--   -.. --- --. .-.-.-  '
        actual = self.module.decode_morse(morse)
        self.assertEqual(actual, 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)

    def test_author_string(self):
        """Checking for __author__ string"""
        self.assertNotEqual(self.module.__author__, '???')

    
class TestDecodeBits(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        cls.module = importlib.import_module(PKG_NAME)
        
    def test_et_phone_home(self):
        """Check if ET PHONE HOME can be transcoded to Morse"""
        bits = '11000000111111000000000000001100111111001111110011000000110011001100110000001111110011111100111111000000111111001100000011000000000000001100110011001100000011111100111111001111110000001111110011111100000011'
        morse = self.module.decode_bits(bits)
        self.assertEqual(morse, '. -  .--. .... --- -. .  .... --- -- .')

    def test_hey_jude_2x(self):
        """Check if HEY JUDE can be transcoded to Morse"""
        bits = '11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
        morse = self.module.decode_bits(bits)
        self.assertEqual(morse, morse_hey_jude)

    def test_hey_jude_6x(self):
        bits = (
            '1111110000001111110000001111'
            '11000000111111000000000000000000111111000000000000000000111111111111'
            '11111100000011111100000011111111111111111100000011111111111111111100'
            '00000000000000000000000000000000000000001111110000001111111111111111'
            '110000001111111111111111110000001111111111111111110000000000000000001'
            '111110000001111110000001111111111111111110000000000000000001111111111'
            '11111111000000111111000000111111000000000000000000111111'
        )
        morse = self.module.decode_bits(bits)
        self.assertEqual(morse, '.... . -.--  .--- ..- -.. .')

    def test_basic_bits(self):
        """Check short letters transcoding to Morse"""
        self.assertEqual(self.module.decode_bits('1'), '.')  # E
        self.assertEqual(self.module.decode_bits('101'), '..')  # I
        self.assertEqual(self.module.decode_bits('10001'), '. .')  # E E
        self.assertEqual(self.module.decode_bits('10111'), '.-')  # A
        self.assertEqual(self.module.decode_bits('1110111'), '--')  # M

    def test_multiple_bits_per_dot(self):
        """Multiple bits per dot handling"""
        self.assertEqual(self.module.decode_bits('111'), '.')  # E
        self.assertEqual(self.module.decode_bits('1111111'), '.')  # E
        self.assertEqual(self.module.decode_bits('110011'), '..')  # I
        self.assertEqual(self.module.decode_bits('111000111'), '..')  # I
        self.assertEqual(self.module.decode_bits('111110000011111'), '..')  # I
        self.assertEqual(self.module.decode_bits('111000000000111'), '. .')  # EE
        self.assertEqual(self.module.decode_bits('11111100111111'), '--')  # M
        self.assertEqual(self.module.decode_bits('111000111000111'), '...')  # S

    def test_extra_zeroes(self):
        """Check handling of leading and trailing zeros"""
        self.assertEqual(self.module.decode_bits('01110'), '.')
        self.assertEqual(self.module.decode_bits('000000011100000'), '.')

    def test_long_message_1x(self):
        """Check long message at 1x time unit"""
        bits = (
            '0001110001010101000100000001110111010111000101011100010100011101'
            '0111010001110101110000000111010101000101110100011101110111000101'
            '1101110001110100000001010111010001110111011100011101010111000000'
            '01011101110111000101011100011101110001011101110100010101000000011'
            '10111011100010101011100010001011101000000011100010101010001000000'
            '01011101010001011100011101110101000111010111011100000001110101000'
            '11101110111000111011101000101110101110101110'
        )
        actual = self.module.decode_bits(bits)
        self.assertEqual(actual, morse_quick_fox)

    def test_long_message_5x(self):
        bits = (
            '1111111111111110000000000000001111100000111110000011111000001111'
            '1000000000000000111110000000000000000000000000000000000011111111'
            '1111111000001111111111111110000011111000001111111111111110000000'
            '0000000011111000001111100000111111111111111000000000000000111110'
            '0000111110000000000000001111111111111110000011111000001111111111'
            '1111100000111110000000000000001111111111111110000011111000001111'
            '1111111111100000000000000000000000000000000000111111111111111000'
            '00111110000011111000001111100000000000000011111000001111111111111'
            '11000001111100000000000000011111111111111100000111111111111111000'
            '00111111111111111000000000000000111110000011111111111111100000111'
            '11111111111100000000000000011111111111111100000111110000000000000'
            '00000000000000000000001111100000111110000011111111111111100000111'
            '11000000000000000111111111111111000001111111111111110000011111111'
            '111111100000000000000011111111111111100000111110000011111000001111'
            '11111111111000000000000000000000000000000000001111100000111111111'
            '11111100000111111111111111000001111111111111110000000000000001111'
            '10000011111000001111111111111110000000000000001111111111111110000'
            '011111111111111100000000000000011111000001111111111111110000011111'
            '111111111100000111110000000000000001111100000111110000011111000000'
            '000000000000000000000000000001111111111111110000011111111111111100'
            '000111111111111111000000000000000111110000011111000001111100000111'
            '111111111111000000000000000111110000000000000001111100000111111111'
            '111111000001111100000000000000000000000000000000000111111111111111'
            '0000000000000001111100000111110000011111000001111100000000000000011111000000000000000000000000000000000001111100000111111111111111000001111100000111110000000000000001111100000111111111111111000000000000000111111111111111000001111111111111110000011111000001111100000000000000011111111111111100000111110000011111111111111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111111111111110000011111111111111100000111110000000000000001111100000111111111111111000001111100000111111111111111000001111100000111111111111111'
        )
        actual = self.module.decode_bits(bits)
        self.assertEqual(actual, morse_quick_fox)


if __name__ == '__main__':
    unittest.main(verbosity=2)
