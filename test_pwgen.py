#!/usr/bin/env python3.7

import unittest

from pwgen import PwGen, PW_SYMBOLS


class TestCase(unittest.TestCase):

    def test_numerals(self):
        pw_length = 5
        pwgen = PwGen(pw_length, 10000, numerals=True)
        chars = pwgen.chars()
        self.assertGreater(len(chars), 0)

        for password in pwgen.passwords:
            self.assertEqual(pw_length, len(password))
            self.assertTrue(any(c.isdigit() for c in password))

    def test_specials_symbols(self):
        pw_length = 5
        pwgen = PwGen(pw_length, 10000, symbols=True)
        chars = pwgen.chars()
        self.assertGreater(len(chars), 0)

        for password in pwgen.passwords:
            self.assertEqual(pw_length, len(password))
            self.assertTrue(any(c in PW_SYMBOLS for c in password))


if __name__ == '__main__':
    unittest.main()
