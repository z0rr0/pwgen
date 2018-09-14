#!/usr/bin/env python3.7

import argparse
import sys

from pwgen import PwGen

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
        help="don't use characters that could be confused by the user when printed, "
             "such as 'l' and '1', or '0' or 'O'.  This reduces the number of possible passwords significantly, "
             "and as such reduces the quality of the  passwords.It may be useful for users who have bad vision, "
             "but in general use of this option is not recommended."
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
        help='Generate random passwords that do not contain vowels or numbers that might be mistaken for vowels. '
             'It provides less secure passwords to allow system administrators to not have to worry '
             'with random passwords acciden‐tally contain offensive substrings.'
    )
    parser.add_argument(
        '-r', '--remove-chars',
        dest='remove_chars',
        type=str,
        help='don\'t use the specified characters in password.  '
             'This option will disable the phomeme-based generator and uses the random password generator.'
    )
    parser.add_argument(
        '-s', '--secure',
        dest='secure',
        action='store_true',
        help='generate completely random, hard-to-memorize passwords. These should only be used for machine '
             'passwords,  since otherwise  it\'s almost guaranteed that users will simply write the password on a '
             'piece of paper taped to the monitor...'
    )
    parser.add_argument(
        '-H', '--sha1',
        dest='sha1',
        type=argparse.FileType('rb'),
        help="will use the sha1's hash of given file and the optional seed to create password. It will allow you to "
             "compute the same password later, if you remember the file, seed, and pwgen's options used. "
             "ie: pwgen -H ~/your_favorite.mp3#your@email.com gives a list of possibles passwords for your "
             "pop3 account, and you can ask this list again and again.\n\nWARNING:  "
             "The  passwords  generated  using this option are not very random.  "
             "If you use this option, make sure the attacker can not obtain a copy of the file.  "
             "Also, note that the name of the file may be easily available from the ~/.history or ~/.bash_history file."
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
        secure=args.secure,
        remove_chars=args.remove_chars,
        sha1=args.sha1,
    )
    try:
        pwgen.print()
    except ValueError as err:
        print(f'ERROR: {err}', file=sys.stderr)
