#include "trie.h"

#include <iostream>
#include <fstream>
#include <string>

Trie::Trie()
{
  for (int x = 0; x < 26; x++) subtries[x] = NULL;
  wordEndsHere = false;
}

Trie::Trie(const char* filename)
{
  for (int x = 0; x < 26; x++) subtries[x] = NULL;
  wordEndsHere = false;

  std::string inWord;
  std::ifstream infile;
  infile.open(filename);

  while (!infile.eof())
    {
      infile >> inWord;
      addWord(inWord);
    }
  infile.close();
}
  

Trie::~Trie()
{
  for (int x = 0; x < 26; x++) delete subtries[x];
}

Trie* Trie::getSubtrie(char character)
{
  int index = character - 97;
  return subtries[index];
}

bool Trie::validNextChar(char character)
{
  return (getSubtrie(character) != NULL);
}

bool Trie::validWord()
{
  return wordEndsHere;
}

bool Trie::validWord(const std::string& word)
{
  return validWord(word, 0);
}

bool Trie::validWord(const std::string& word, int start)
{
  // if we're at the end of the input, check if this is a valid place to end
  if (word.length() == start) return wordEndsHere;

  // Get the next subtrie. If null, false. If a real subtrie, recurse
  Trie* subtrie = getSubtrie(word[start]);
  if (subtrie == NULL) return false;
  return subtrie->validWord(word, start + 1);
}

void Trie::addWord(const std::string& word, int start)
{
  if (word.length() == start)
    {
      wordEndsHere = true;
    }
  else
    {
      char letter = word[start];
      Trie* subtrie = getSubtrie(letter);
      if (subtrie == NULL) subtrie = makeSubtrie(letter);
      subtrie->addWord(word, start + 1);
    }
}

void Trie::addWord(const std::string& word)
{
  addWord(word, 0);
}

Trie* Trie::makeSubtrie(char letter)
{
  int index = letter - 97;
  subtries[index] = new Trie();
  return subtries[index];
}

std::istream& operator>>(std::istream &in, Trie &trie)
{
  std::string word;
  getline(in, word);
  trie.addWord(word);
  return in;
}
