from sys import stdin
from random import choice
from string import letters

replace = {"c": "bcdfghjklmnpqrstvwxyz", "v": "aeiou"}

print "".join(
    choice(replace[char.lower()])
    for char in stdin.read(-1)
    if char in letters)
