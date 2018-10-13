#!/usr/bin/env python3.7
# coding: utf-8

import hashlib
import string
import sys

from random import Random, SystemRandom
from typing import BinaryIO, Generator, List, TextIO


PW_DIGITS = string.digits
PW_LOWERS = string.ascii_lowercase
PW_UPPERS = string.ascii_uppercase
PW_SYMBOLS = string.punctuation
PW_AMBIGUOUS = 'B8G6I1l0OQDS5Z2'
PW_VOWELS = '01aeiouyAEIOUY'


class PwGen(object):
    """Passwords generator"""

    SCREEN_WIDTH = 80

    def __init__(self, pw_length: int, num_pw: int,
                 no_numerals: bool=False, one_line: bool=False, no_capitalize: bool=False,
                 ambiguous: bool=False, symbols: bool=False, numerals: bool=False,
                 no_vowels: bool=False, secure: bool=False, remove_chars: str=None, sha1: BinaryIO=None):
        self.pw_length = pw_length
        self.num_pw = num_pw
        # options
        self.no_numerals = no_numerals
        self.one_line = one_line
        self.no_capitalize = no_capitalize
        self.ambiguous = ambiguous
        self.symbols = symbols
        self.numerals = numerals
        self.no_vowels = no_vowels

        seed = hashlib.sha1(sha1.read()).digest() if sha1 else None
        random = SystemRandom if secure else Random
        self.random = random(seed)
        self.remove_chars = set(remove_chars) if remove_chars else set()

    def __str__(self):
        return 'PwGen <{}, {}> from "{}"'.format(self.pw_length, self.num_pw, ''.join(self.chars()))

    def _char(self, chars: list) -> Generator[str, None, None]:
        """Generates password's chars by required rules"""
        n = self.pw_length
        if self.symbols:
            # generate at least one special symbol
            c = self.random.choice(PW_SYMBOLS)
            n -= 1
            yield c

        if not self.no_numerals and self.numerals and n > 0:
            # generate at least one digital symbol
            c = self.random.choice(PW_DIGITS)
            n -= 1
            yield c
        for _ in range(n):
            yield self.random.choice(chars)

    def chars(self) -> List[str]:
        u"""Builds password's chars list"""
        chars = PW_LOWERS
        if not self.no_numerals:
            chars += PW_DIGITS
        if not self.no_capitalize:
            chars += PW_UPPERS
        if self.symbols:
            chars += PW_SYMBOLS

        if self.ambiguous:
            self.remove_chars.update(PW_AMBIGUOUS)
        if self.no_vowels:
            self.remove_chars.update(PW_VOWELS)

        if self.remove_chars:
            chars = set(chars) - self.remove_chars
            # to exclude infinite loop
            if not chars:
                raise ValueError('no symbols for passwords generation')
        return list(chars)

    def generate(self, chars: List[str]=None) -> str:
        """Generates a password"""
        chars = chars or self.chars()
        password = [c for c in self._char(chars)]
        self.random.shuffle(password)
        return ''.join(password)

    @property
    def passwords(self) -> Generator[str, None, None]:
        """Generates passwords"""
        chars = self.chars()
        for _ in range(self.num_pw):
            yield self.generate(chars)

    def print(self, out: TextIO=sys.stdout) -> None:
        """Prints outputs passwords in one line or by columns"""
        if self.one_line:
            for i, password in enumerate(self.passwords, start=1):
                end = '\n' if i == self.num_pw else ' '
                print(password, end=end, file=out)
            return
        # print by columns
        columns = self.SCREEN_WIDTH // self.pw_length or 1
        for i, password in enumerate(self.passwords, start=1):
            end = '\n' if not (i % columns) or (i == self.num_pw) else ' '
            print(password, end=end, file=out)
