"""
Fill a square one character a time, so that each row and column is a valid
word. Recursively guess space 0 through n**2 - 1, only using valid next
characters for that row and column.
"""

from copy import deepcopy

from trie import Trie

DICT_FILE = "enable1.txt"


def guess(grid, trie, space, chars_left):
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
        results += guess(grid, trie, space + 1, chars_left.replace(char, "", 1))

    return results


def make_square(string):
    size_str, chars = string.split()
    size = int(size_str)
    trie = Trie(DICT_FILE, size)

    grid = [[None for _ in range(size)] for _ in range(size)]
    return guess(grid, trie, 0, chars)


if __name__ == "__main__":
#    make_square("4 aaccdeeeemmnnnoo")
#    make_square("5 aaaeeeefhhmoonssrrrrttttw")
#    make_square("5 aabbeeeeeeeehmosrrrruttvv")
    make_square("7 aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy")
