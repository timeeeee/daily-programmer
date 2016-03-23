#ifndef __TRIE_H__
#define __TRIE_H__

#include <iostream>
#include <string>

class Trie {
 private:
  Trie* subtries[26];
  bool wordEndsHere;
  Trie* makeSubtrie(char letter);

 public:
  Trie();
  Trie(const char* filename);
  ~Trie();
  Trie* getSubtrie(char character);
  bool validNextChar(char character);
  bool validWord();
  bool validWord(const std::string&);
  bool validWord(const std::string&, int start);
  void addWord(const std::string& word, int start);
  void addWord(const std::string& word);
};

std::istream& operator>>(std::istream &in, Trie &trie);

#endif
