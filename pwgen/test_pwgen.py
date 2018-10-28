#!/usr/bin/env python3.7
# coding: utf-8

import io
import unittest

from pwgen import PwGen, PW_SYMBOLS, PW_AMBIGUOUS, PW_VOWELS


class PwGenTestCase(unittest.TestCase):

    def test_numerals(self):
        pw_length = 5
        pwgen = PwGen(pw_length, 10000, numerals=True)
        chars = pwgen.chars()
        self.assertGreater(len(chars), 0)

        for password in pwgen.passwords:
            self.assertEqual(pw_length, len(password))
            self.assertTrue(any(c.isdigit() for c in password), f'password={password}')

    def test_no_numerals(self):
        pw_length = 10
        pwgen = PwGen(pw_length, 10000, no_numerals=True)

        for password in pwgen.passwords:
            self.assertEqual(pw_length, len(password))
            self.assertTrue(all(not c.isdigit() for c in password), f'password={password}')

    def test_no_capitalize(self):
        pw_length = 10
        pwgen = PwGen(pw_length, 10000, no_capitalize=True)

        for password in pwgen.passwords:
            self.assertEqual(pw_length, len(password))
            self.assertTrue(all(not c.istitle() for c in password), f'password={password}')

    def test_ambiguous(self):
        pw_length = 10
        pwgen = PwGen(pw_length, 10000, ambiguous=True)

        for password in pwgen.passwords:
            self.assertEqual(pw_length, len(password))
            self.assertTrue(all(c not in PW_AMBIGUOUS for c in password), f'password={password}')

    def test_no_vowels(self):
        pw_length = 10
        pwgen = PwGen(pw_length, 10000, no_vowels=True)

        for password in pwgen.passwords:
            self.assertEqual(pw_length, len(password))
            self.assertTrue(all(c not in PW_VOWELS for c in password), f'password={password}')

    def test_symbols(self):
        pw_length = 5
        pwgen = PwGen(pw_length, 10000, symbols=True)
        chars = pwgen.chars()
        self.assertGreater(len(chars), 0)

        for password in pwgen.passwords:
            self.assertEqual(pw_length, len(password))
            self.assertTrue(any(c in PW_SYMBOLS for c in password), f'password={password}')

    def test_secure(self):
        pw_length = 100
        pwgen = PwGen(pw_length, 100)

        pwgen.random.seed(123)
        passwords1 = list(pwgen.passwords)
        pwgen.random.seed(123)
        passwords2 = list(pwgen.passwords)
        self.assertEqual(passwords1, passwords2)

        pwgen = PwGen(pw_length, 100, secure=True)

        pwgen.random.seed(123)
        passwords1 = list(pwgen.passwords)
        pwgen.random.seed(123)
        passwords2 = list(pwgen.passwords)
        self.assertNotEqual(passwords1, passwords2)

    def test_sha1(self):
        pwgen = PwGen(5, 10000, sha1=io.BytesIO(b"abcdef"))
        passwords1 = list(pwgen.passwords)

        pwgen = PwGen(5, 10000, sha1=io.BytesIO(b"abcdef"))
        passwords2 = list(pwgen.passwords)

        self.assertEqual(passwords1, passwords2)

    def test_remove_chars(self):
        pw_length = 10
        remove_chars = 'abcdefghijklmnJKLMNOPQRSTUVWXYZ01234'
        pwgen = PwGen(pw_length, 10000, remove_chars=remove_chars)

        for password in pwgen.passwords:
            self.assertEqual(pw_length, len(password))
            self.assertTrue(all(c not in remove_chars for c in password), f'password={password}')

    def test_custom_output(self):
        num_pw = 32
        pwgen = PwGen(17, num_pw=num_pw, one_line=True)

        out = io.StringIO()
        pwgen.print(out=out)

        passwords = out.getvalue()
        self.assertEqual(len(passwords.split()), num_pw)


if __name__ == '__main__':
    unittest.main()
