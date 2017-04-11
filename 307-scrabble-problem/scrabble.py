"""
What is the longest word you can build in a game of Scrabble one letter at a
time? That is, starting with a valid two-letter word, how long a word can you
build by playing one letter at a time on either side to form a valid three-
letter word, then a valid four-letter word, and so on? (For example, HE could
become THE, then THEM, then THEME, then THEMES, for a six-letter result.)
"""

"""
Create a set of all words of each length 2+. Starting with the 3-letter words,
delete any words that can't be made by adding a character to the beginning or
end of a word from the previous list.
"""

def get_words_by_length(wordlist):
    words_by_length = []
    for word in wordlist:
        while len(words_by_length) <= len(word):
            words_by_length.append([])
        words_by_length[len(word)].append(word)
    return words_by_length


def list_diff(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)
    while l1 and l2:
        if l1[0] < l2[0]:
            print("list 1 has {}".format(l1.pop(0)))
        elif l2[0] < l1[0]:
            print ("list 2 has {}".format(l2.pop(0)))
        else:
            # These elements match, move on
            l1.pop(0)
            l2.pop(0)

    # Maybe one list has items left, finish them out
    for item in l1:
        print("list 1 has {}".format(item))

    for item in l2:
        print("list 2 has {}".format(item))
            

def test_get_words_by_length():
    with open("enable1.txt") as f:
        wordlist = [line.strip() for line in f]

    words_by_length = get_words_by_length(wordlist)
    for a, b in zip(sorted(wordlist), sorted(sum(words_by_length, []))):
        assert a == b


def longest_scrabble_words(wordlist):
    """
    Return a list of the longest words that can be made by starting with a
    two-letter word and adding one letter at a time to either the beginning or
    end of the word, making a new english word each time.
    
    For all words of a particular length, filter out the ones that can't be
    made from the words with one less letter. Start from three-letter words,
    working up until there are no words of a particular length.
    """
    words_by_length = get_words_by_length(wordlist)

    # Assume all 2-letter words are fine
    good_words = words_by_length[2]
    for length in range(3, len(wordlist)):
        previous_words = good_words
        bases = set(previous_words)
        good_words = []

        for word in words_by_length[length]:
            if word[1:] in bases or word[:-1] in bases:
                good_words.append(word)

        # If we didn't find any words of this length, the words of the previous
        # length are the longest ones
        if len(good_words) == 0:
            return previous_words

        previous_words = good_words

    # If the loop is done, there were valid words with the maximum word length
    return good_words

if __name__ == "__main__":
    with open("enable1.txt") as f:
        wordlist = [line.strip() for line in f]

    print longest_scrabble_words(wordlist)
