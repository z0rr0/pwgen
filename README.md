# PwGen

[![Build Status](https://travis-ci.com/z0rr0/pwgen.svg?branch=master)](https://travis-ci.com/z0rr0/pwgen)

PwGen - generate pronounceable passwords

It's a python clone of Linux tool [pwgen](https://linux.die.net/man/1/pwgen).

## Usage

```
python3.7 pwgen.py 10 20
xZF9LXajkT wZuylOIV4l bO5MK11qIs k7NrlPrIlr 575Wh7zZD4 SU7SBaXvil sUXQaCPa3G 6oLoQ6eMhi
SbA6xC2iWF sDRmv4r9gW FUMuGyHR9x s3KfNkz302 8ubu1peEII H7RN73SxpN T7KU5k2JwZ puxgUyK9Fe
o7xUDHMJNW AS3N1l9JEp v6GQ6fVltP EAFp9yce0D


python3.7 pwgen.py --help                                                    
usage: pwgen.py [-h] [-0] [-1] [-A] [-B] [-y] [-n] [-v] [-r REMOVE_CHARS] [-s]
                [-H SHA1]                                                    
                [pw_length] [num_pw]

generate pronounceable passwords

positional arguments:
  pw_length             password length
  num_pw                number of passwords

optional arguments:
  -h, --help            show this help message and exit
  -0, --no-numerals     don't include numbers in the generated passwords.
  -1, --one-line        print the generated passwords one per line.
  -A, --no-capitalize   don't bother to include any capital letters in the
                        generated passwords.
  -B, --ambiguous       don't use characters that could be confused by the
                        user when printed, such as 'l' and '1', or '0' or 'O'.
                        This reduces the number of possible passwords
                        significantly, and as such reduces the quality of the
                        passwords.It may be useful for users who have bad
                        vision, but in general use of this option is not
                        recommended.
  -y, --symbols         include at least one special character in the
                        password.
  -n, --numerals        include at least one number in the password. This is
                        the default option.
  -v, ---no-vowels      Generate random passwords that do not contain vowels
                        or numbers that might be mistaken for vowels. It
                        provides less secure passwords to allow system
                        administrators to not have to worry with random
                        passwords acciden‐tally contain offensive substrings.
  -r REMOVE_CHARS, --remove-chars REMOVE_CHARS
                        don't use the specified characters in password. This
                        option will disable the phomeme-based generator and
                        uses the random password generator.
  -s, --secure          generate completely random, hard-to-memorize
                        passwords. These should only be used for machine
                        passwords, since otherwise it's almost guaranteed that
                        users will simply write the password on a piece of
                        paper taped to the monitor...
  -H SHA1, --sha1 SHA1  will use the sha1's hash of given file and the
                        optional seed to create password. It will allow you to
                        compute the same password later, if you remember the
                        file, seed, and pwgen's options used. ie: pwgen -H
                        ~/your_favorite.mp3#your@email.com gives a list of
                        possibles passwords for your pop3 account, and you can
                        ask this list again and again. WARNING: The passwords
                        generated using this option are not very random. If
                        you use this option, make sure the attacker can not
                        obtain a copy of the file. Also, note that the name of
                        the file may be easily available from the ~/.history
                        or ~/.bash_history file.
```

## Tests

```sh
python3.7 -m unittest
```

## License

This source code is governed by a MIT license that can be found in the [LICENSE](https://github.com/z0rr0/pwgen/blob/master/LICENSE) file.