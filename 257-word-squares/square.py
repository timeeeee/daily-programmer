"""
Fill a square one character a time, so that each row and column is a valid
word. Recursively guess space 0 through n**2 - 1, only using valid next
characters for that row and column.
"""

from copy import deepcopy

from trie import Trie

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


def guess_words(words_so_far, trie, word_list, char_counts_left):
    if len(words_so_far) == len(words_so_far[0]):
        # Done!
        return [words_so_far]

    pass


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
