// basic file operations
#include <iostream>
#include <fstream>
#include <string>

#include "trie.h"

int main (int argc, const char *argv[])
{
  ifstream dictionary("enable1.txt");
  if (!dictionary.is_open())
    {
      cout << "Couldn't open dictionary \"enable1.txt\"\n";
      return 1;
    }

  string line;
  while (getline(dictionary, line))
    {
      cout << line << "\n";
    }

  dictionary.close();
  return 0;
}
