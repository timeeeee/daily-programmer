def can_spell(available, word):
    """Check if a word can be spelled using characters in available"""
    for char in set(word):
        if word.count(char) > available.count(char):
            return False
    return True


def test_can_spell():
    from string import printable
    from random import sample
    for _ in xrange(1000):
        word = "".join(sample(printable, 20))
        assert(can_spell(printable, word))
        assert(not(can_spell(printable, word + word[0])))
        assert(can_spell("".join(sorted(printable * 2)), word * 2))
        assert(not(can_spell("".join(sorted(printable * 2)), word * 3)))


class Trie:
    def __init__(self, dict_file=None, word_length=None, filter_chars=None):
        self.subtries = {}
        self.word_ends_here = False
        self.length = 0

        if dict_file is not None:
            with open(dict_file) as dictionary:
                for line in dictionary:
                    word = line.strip()
                    if word.isalpha() and len(word) == word_length:
                        if filter_chars is None or can_spell(filter_chars, word):
                            self.length += 1
                            self.add_word(word)


    def __len__(self):
        return self.length

    def add_word(self, word):
        """Add word to the trie"""
        if word == "":
            self.word_ends_here = True
        else:
            first, rest = word[0], word[1:]
            if first not in self.subtries:
                self.subtries[first] = Trie()
            self.subtries[first].add_word(rest)

    def __contains__(self, word):
        """Check if the word is in the trie"""
        # If it's the end of the word, check if this is a valid place to stop
        if word == "":
            return self.word_ends_here

        first, rest = word[0], word[1:]
        if first not in self.subtries:
            return False

        # Not the end of the word- check subtries
        return rest in self.subtries[first]
            
    def next_chars(self, partial_word=""):
        """Get all possible characters for the partial word"""
        if partial_word == "":
            return self.subtries.keys()

        first, rest = partial_word[0], partial_word[1:]
        return self.subtries[first].next_chars(rest)
