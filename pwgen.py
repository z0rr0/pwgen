#!/usr/bin/env python3.7

import argparse
import random


PW_DIGITS = '0123456789'
PW_LOWERS = 'abcdefghijklmnopqrstuvwxyz'
PW_UPPERS = PW_LOWERS.upper()
PW_SYMBOLS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
PW_AMBIGUOUS = 'B8G6I1l0OQDS5Z2'
PW_VOWELS = '01aeiouyAEIOUY'


class PwGen(object):

    SCREEN_WIDTH = 80

    def __init__(self, pw_length, num_pw,
                 no_numerals=False, one_line=False, no_capitalize=False):
        self.pw_length = pw_length
        self.num_pw = num_pw
        self._passwords = []
        # options
        self.no_numerals = no_numerals
        self.one_line = one_line
        self.no_capitalize = no_capitalize

    def _pw_char(self, chars: list):
        for _ in range(self.pw_length):
            # additional logic should be here
            yield random.choice(chars)

    def generate(self) -> str:
        """Generates a password"""
        chars = ''
        if not self.no_numerals:
            chars += PW_DIGITS
        if not self.no_capitalize:
            chars += PW_UPPERS

        chars += PW_LOWERS
        chars += PW_SYMBOLS

        chars = list(chars)
        random.shuffle(chars)
        return ''.join(c for c in self._pw_char(chars))

    @property
    def passwords(self) -> list:
        """Returns all generated password"""
        if self._passwords:
            return self._passwords
        i = 0
        while i < self.num_pw:
            self._passwords.append(self.generate())
            i += 1
        return self._passwords

    def print(self):
        """Print generated password in one line or by columns"""
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
    parser.add_argument('pw_length', type=int, nargs='?', help='password length', default=8)
    parser.add_argument('num_pw', type=int,  nargs='?', help='number of passwords', default=160)

    args, _ = parser.parse_known_args()

    pwgen = PwGen(
        args.pw_length, args.num_pw,
        no_numerals=args.no_numerals,
        one_line=args.one_line,
        no_capitalize=args.no_capitalize,
    )
    pwgen.print()
