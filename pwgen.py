#!/usr/bin/env python3.7

import argparse
import sys
import random

from typing import List


PW_DIGITS = '0123456789'
PW_LOWERS = 'abcdefghijklmnopqrstuvwxyz'
PW_UPPERS = PW_LOWERS.upper()
PW_SYMBOLS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
PW_AMBIGUOUS = 'B8G6I1l0OQDS5Z2'
PW_VOWELS = '01aeiouyAEIOUY'


class PwGen(object):
    """Passwords generator"""

    SCREEN_WIDTH = 80

    def __init__(self, pw_length: int, num_pw: int,
                 no_numerals=False, one_line=False, no_capitalize=False, ambiguous=False, symbols=False, 
                 numerals=False, no_vowels=False, remove_chars=None):
        self.pw_length = pw_length
        self.num_pw = num_pw
        self._passwords = []
        # options
        self.no_numerals = no_numerals
        self.one_line = one_line
        self.no_capitalize = no_capitalize
        self.ambiguous = ambiguous
        self.symbols = symbols
        self.numerals = numerals
        self.no_vowels = no_vowels
        self.remove_chars = set(remove_chars) if remove_chars else set()

    def _pw_char(self, chars: list) -> str:
        """Generates password chars by required rules"""
        n = self.pw_length
        if self.symbols:
            # generate a special symbol
            c = random.choice(PW_SYMBOLS)
            n -= 1
            yield c

        if not self.no_numerals and self.numerals and n > 0:
            # generate a diginal symbol
            c = random.choice(PW_DIGITS)
            n -= 1
            yield c

        i = 0
        while i < n:
            c = random.choice(chars)
            # additional logic should be here
            if self.ambiguous and c in PW_AMBIGUOUS:
                continue
            if self.no_vowels and c in PW_VOWELS:
                continue
            i += 1 
            yield c

    def chars(self) -> List[str]:
        u"""Builds used chars list"""
        chars = ''
        if not self.no_numerals:
            chars += PW_DIGITS
        if not self.no_capitalize:
            chars += PW_UPPERS
        if self.symbols:
            chars += PW_SYMBOLS

        chars += PW_LOWERS
        if self.remove_chars:
            chars = set(chars) - self.remove_chars
            # to exclude infinite loop
            if not chars:
                raise ValueError('no symbols for passwords generation')
        return list(chars)

    def generate(self, chars: List[str]=None) -> str:
        """Generates a password"""
        chars = chars or self.chars()
        password = [c for c in self._pw_char(chars)]
        random.shuffle(password)
        return ''.join(password)

    @property
    def passwords(self) -> List[str]:
        """Returns all generated password"""
        if self._passwords:
            return self._passwords

        chars = self.chars()
        self._passwords = [self.generate(chars) for _ in range(self.num_pw)]
        return self._passwords

    def print(self) -> None:
        """Prints generated password in one line or by columns"""
        if self.one_line:
            print(' '.join(self.passwords))
            return

        columns = self.SCREEN_WIDTH // self.pw_length or 1

        start, stop = 0, columns
        while start <= self.num_pw:
            passwords = self.passwords[start:stop]
            print(' '.join(passwords))
            start, stop = stop, stop + columns


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate pronounceable passwords')
    parser.add_argument(
        '-0', '--no-numerals',
        dest='no_numerals',
        action='store_true',
        help='don\'t include numbers in the generated passwords.'
    )
    parser.add_argument(
        '-1', '--one-line',
        dest='one_line',
        action='store_true',
        help='print the generated passwords one per line.'
    )
    parser.add_argument(
        '-A', '--no-capitalize',
        dest='no_capitalize',
        action='store_true',
        help='don\'t bother to include any capital letters in the generated passwords.'
    )
    parser.add_argument(
        '-B', '--ambiguous',
        dest='ambiguous',
        action='store_true',
        help="don't use characters that could be confused by the user when printed, such as 'l' and '1', or '0' or 'O'.  This reduces the number of possible passwords significantly, and as such reduces the quality of the  passwords.It may be useful for users who have bad vision, but in general use of this option is not recommended."
    )
    parser.add_argument(
        '-y', '--symbols',
        dest='symbols',
        action='store_true',
        help='include at least one special character in the password.'
    )
    parser.add_argument(
        '-n', '--numerals',
        dest='numerals',
        default=True,
        action='store_true',
        help='include at least one number in the password.  This is the default option.'
    )
    parser.add_argument(
        '-v', '---no-vowels',
        dest='no_vowels',
        action='store_true',
        help='Generate random passwords that do not contain vowels or numbers that might be mistaken for vowels. It provides less secure passwords to allow system administrators to not have to worry with random passwords acciden‐tally contain offensive substrings.'
    )
    parser.add_argument(
        '-r', '--remove-chars',
        dest='remove_chars',
        type=str,
        help='don\'t use the specified characters in password.  This option will disable the phomeme-based generator and uses the random password generator.'
    )
    parser.add_argument('pw_length', type=int, nargs='?', help='password length', default=8)
    parser.add_argument('num_pw', type=int,  nargs='?', help='number of passwords', default=160)

    args, _ = parser.parse_known_args()

    pwgen = PwGen(
        args.pw_length, args.num_pw,
        no_numerals=args.no_numerals,
        one_line=args.one_line,
        no_capitalize=args.no_capitalize,
        ambiguous=args.ambiguous,
        symbols=args.symbols,
        numerals=args.numerals,
        no_vowels=args.no_vowels,
        remove_chars=args.remove_chars,
    )
    try:
        pwgen.print()
    except ValueError as err:
        print(f'ERROR: {err}', file=sys.stderr)
