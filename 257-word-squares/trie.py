class Trie:
    def __init__(self, dict_file=None, word_length=None):
        self.subtries = {}
        self.word_ends_here = False

        if dict_file is not None:
            with open(dict_file) as dictionary:
                for line in dictionary:
                    word = line.strip()
                    if word.isalpha() and len(word) == word_length:
                        self.add_word(word)

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
