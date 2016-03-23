all: square.o trie.o
	g++ -o square square.o trie.o

.PHONY: clean trie_test trie_test_binary

square.o: square.cpp
	g++ -g -c square.cpp

trie.o: trie.h trie.cpp
	g++ -g -c trie.cpp

trie_test.o: trie_test.cpp
	g++ -g -c trie_test.cpp

trie_test_binary: trie_test.o trie.o
	g++ -g trie_test.o trie.o -o trie_test

trie_test: trie_test_binary
	valgrind ./trie_test

clean:
	rm -f *.o *~ trie_test
