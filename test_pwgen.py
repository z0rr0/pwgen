#!/usr/bin/env python3.7

import unittest

from pwgen import PwGen


class TestCase(unittest.TestCase):

    def test_numerals(self):
        pwgen = PwGen(5, 10000, numerals=True)
        chars = pwgen.chars()
        self.assertGreater(len(chars), 0)

        for password in pwgen.passwords:
            self.assertTrue(any(c.isdigit() for c in password))


if __name__ == '__main__':
    unittest.main()
