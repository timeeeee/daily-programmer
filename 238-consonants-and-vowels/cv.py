from sys import stdin
from random import choice

replace = {"c": list("bcdfghjklmnpqrstvwxyz"), "v": list("aeiou")}

def replace_char(char):
    if char in replace:
        return choice(replace[char])
    else:
        raise Exception('Character "{}" is not a c or v'.format(char))

result = []
for char in stdin.read(-1):
    if 
    if char.lower() in replace:
        new_char = choice(replace[char.lower()]
