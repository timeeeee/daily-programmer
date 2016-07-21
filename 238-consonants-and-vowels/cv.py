#!/bin/python

"""
Read characters from standard input. Replace 'c' with a random consonant, and v
with a random vowel (matching case). Raise ValueError on any other letter.

Example:
echo "ccvvCCVV" | python cv.py
"""

from sys import stdin
from random import choice
from string import letters

REPLACE = {"c": "bcdfghjklmnpqrstvwxyz", "v": "aeiou",
           "C": "BCDFGHJKLMNPQRSTVWXYZ", "V": "AEIOU"}


def replace_char(char):
    if char in "cvCV":
        return choice(REPLACE[char])
    elif char in letters:
        raise ValueError("Character '{}' not in [cvCV]".format(char))
    else:
        # If character is digit or punctuation or whitespace, return it
        return char


def replace_flo(flo):
    return "".join(map(replace_char, flo.read(-1)))


if __name__ == "__main__":
    print replace_flo(stdin)
