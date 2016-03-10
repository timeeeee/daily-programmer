""" Draw pieces from a random bag"""

from random import shuffle
from itertools import islice

PIECES = "OISZLJT"

def piece_bag(pieces):
    while True:
        bag = list(pieces)
        shuffle(bag)
        while bag:
            yield bag.pop()


def main():
    piece_generator = piece_bag(PIECES)
    print list(islice(piece_generator, 100))


if __name__ == "__main__":
    main()
