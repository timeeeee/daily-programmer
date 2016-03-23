#include <iostream>
#include <fstream>
#include <cassert>
#include <string>

#include "trie.h"

int main() {
  // Make trie, let it go out of scope
  {
    Trie trie;
  }

  // empty tree
  {
    Trie trie;
    assert(!trie.validWord());
    for (char letter = 97; letter < 123; letter++)
      {
	assert(trie.getSubtrie(letter) == NULL);
	assert(!trie.validNextChar(letter));
      }
  }

  // add a couple words
  {
    Trie trie;
    std::string word1 = "abacus";
    std::string word2 = "absolutely";
    std::string word3 = "butt";
    trie.addWord(word1);
    trie.addWord(word2);
    trie.addWord(word3);

    assert(trie.validNextChar('a'));
    assert(trie.validNextChar('b'));
    for (char letter = 99; letter < 123; letter++)
      assert(!trie.validNextChar(letter));

    Trie* subtrie;

    // "bacus" trie
    subtrie = trie.getSubtrie('a');
    assert(!subtrie->validWord());
    assert(subtrie->validNextChar('b'));
				  
    // "acus" trie
    subtrie = subtrie->getSubtrie('b');
    assert(!subtrie->validWord());
    assert(subtrie->validNextChar('a'));

    // "cus" trie
    subtrie = subtrie->getSubtrie('a');
    assert(!subtrie->validWord());
    assert(subtrie->validNextChar('c'));

    // "us" trie
    subtrie = subtrie->getSubtrie('c');
    assert(!subtrie->validWord());
    assert(subtrie->validNextChar('u'));

    // "s" trie
    subtrie = subtrie->getSubtrie('u');
    assert(!subtrie->validWord());
    assert(subtrie->validNextChar('s'));

    // empty end-of-word trie
    subtrie = subtrie->getSubtrie('s');
    assert(subtrie->validWord());
  } // add a couple words

  // read in the whole dictionary!
  {
    std::ifstream infile;
    infile.open("enable1.txt");
    if (!infile.is_open()) return 1;

    Trie trie;
    std::string inWord;
    std::cout << "building dictionary... ";
    std::cout.flush();
    while (!infile.eof())
      {
	infile >> inWord;
	trie.addWord(inWord);
      }
    infile.close();
    std::cout << "done.\n";

    assert(trie.validWord("abacus"));
    assert(trie.validWord("adzes"));
    assert(!trie.validWord("adzuk"));
    assert(trie.validWord("adzuki"));
    assert(!trie.validWord("tim"));

    std::cout << "deleting dictionary... ";
    std::cout.flush();
  } // make trie of whole dictionary
  std::cout << "done.\n";

  // test file constructor
  {
    std::cout << "building dictionary... ";
    std::cout.flush();
    Trie trie("enable1.txt");
    std::cout << "done.\n";
    std::cout << "deleting dictionary... ";
    std::cout.flush();
  }
  std::cout << "done.\n";

  std::cout << "all tests passed!\n";
  return 0;
}
