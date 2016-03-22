all: square.o trie.o
	g++ -o square square.o trie.o

square.o: square.cpp
	g++ -g square.cpp

trie.o: trie.h trie.cpp
	g++ -g trie.cpp

clean:
	rm -f *.o
