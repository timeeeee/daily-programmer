"""
Fill a square one character a time, so that each row and column is a valid
word. Recursively guess space 0 through n**2 - 1, only using valid next
characters for that row and column.
"""

from copy import deepcopy
from string import lowercase

from trie import Trie, can_spell

DICT_FILE = "enable1.txt"


def guess_chars(grid, trie, space, chars_left):
    # If no characters left, grid is full
    if chars_left == "":
        print "========== FOUND SOLUTION =========="
        print "\n".join(str(line) for line in grid)
        print "===================================="
        print
        return [deepcopy(grid)]

    # Else, try all possible characters for this spot.
    results = []
    row, col = divmod(space, len(grid))

    # get valid next chars
    row_word = "".join(grid[row][n] for n in range(col))
    row_next_chars = trie.next_chars(row_word)
    col_word = "".join(grid[n][col] for n in range(row))
    col_next_chars = trie.next_chars(col_word)
    valid_chars = set(chars_left)
    valid_chars.intersection_update(row_next_chars)
    valid_chars.intersection_update(col_next_chars)

    """
    print "for grid {}, space {}:".format(grid, (row, col))
    print "chars left = {}".format(chars_left)
    print "possible next chars for row word '{}': {}".format(
        row_word, row_next_chars)
    print "possible next chars for col word '{}': {}".format(
        col_word, col_next_chars)
    print "testing chars {}".format(valid_chars)
    print
    """

    for char in valid_chars:
        # plop the guess into the grid
        grid[row][col] = char
        results += guess_chars(grid, trie, space + 1, chars_left.replace(char, "", 1))

    return results


"""
The way to do this which makes much more sense is guessing a word at a time
instead of a single character. The problem then is how to 

Is there a data structure that would make it efficient to find everything with
character counts less than or equal to some set of numbers? Rather than step
through the whole list each time, could generate smaller lists to pass to
recursively called functions?

Make character counts for each word at the beginning. For remaining characters,
remember counts for the whole alphabet, not a string. MAY AS WELL DO THIS IN C.
"""


class CharCount(object):
    def __init__(self, string=""):
        self.counts = [0 for _ in xrange(26)]
        for char in string.lower():
            if char not in lowercase:
                raise ValueError("'{}' contains non-character '{}'".format(
                    string, char))
            self.counts[ord(char) - 97] += 1

    def __getitem__(self, key):
        key = key.lower()
        if key not in lowercase:
            raise KeyError("'{}' not a character".format(key))
        return self.counts[ord(key) - 97]

    def __setitem__(self, key, value):
        key = key.lower()
        if key not in lowercase:
            raise KeyError("'{}' not a character".format(key))
        self.counts[ord(key) - 97] = value

    def __gt__(self, other):
        return all(a >= b for a, b in zip(self.counts, other.counts))

    def can_spell(self, word):
        return (self > CharCount(word))

    def __str__(self):
        key_values = ", ".join(
            "'{}': {}".format(key, value)
            for key, value in zip(lowercase, self.counts))
        return "{{{}}}".format(key_values)

    def subtract_word(self, word):
        for char in word.lower():
            self[char] -= 1

    def __sub__(self, word):
        new_counts = CharCount()
        new_counts.counts = list(self.counts)
        for char in word.lower():
            new_counts[char] -= 1
        return new_counts


def guess_words(words_so_far, trie, word_list, char_counts_left):
    if len(words_so_far) == len(words_so_far[0]):
        # Done!
        return [words_so_far]

    # guess one word at a time from the word list, checking to see if it's
    # a viable word with the characters left
    filtered_word_list = []
    for word in word_list:
        if char_counts_left.can_spell(word):
            filtered_word_list.append(word)
            


def make_square(string):
    size_str, chars = string.split()
    size = int(size_str)
    trie = Trie(DICT_FILE, size, filter_chars=chars)

    grid = [[None for _ in range(size)] for _ in range(size)]
    return guess_chars(grid, trie, 0, chars)


if __name__ == "__main__":
    problems = [
        "4 aaccdeeeemmnnnoo",
        "5 aaaeeeefhhmoonssrrrrttttw",
        "5 aabbeeeeeeeehmosrrrruttvv",
        "7 aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy"]
    for problem in problems:
        print problem
        make_square(problem)
