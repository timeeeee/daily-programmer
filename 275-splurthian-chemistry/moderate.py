"""
The Splurth Council of Atoms and Atom-Related Paraphernalia has decided to keep
their current naming conventions, as listed in the Easy challenge, but to add a
preference system. So while there are still 6 valid symbols for the element
Iron, the preferred symbol is Ir. The second-most preferred symbol is Io, then
In, Ro, Rn, and finally On. A symbol is preferred based on how early in the
element name its first letter is, followed by how early its second letter is.

In the case of repeated letters like in Neon, Eo is preferred to En, even
though an n is closer to the beginning of Neon than the o is. This is because
it's the second n that's used in the symbol En, since the second letter in the
symbol must appear after the first.

When the Council receives a new element to add to the table, it chooses the
most preferred valid symbol for that element that's not already taken by
another element. For instance, if Chlorine were the first element added, then
it would get the symbol Ch. If Chromium was added later, it would get the
symbol Cr. If Cesium and Cerium were then added, they would get the symbols Ce
and Ci. If there are no valid symbols for the new element.... well, that's why
the Council needs you.

The Council has decided to wipe the table clean and start afresh. The list of
all 366 elements known to Splurthians are set to be assigned a symbol, one by
one, in the order in that text file, following the preference rules above.

Determine the symbol assigned to each element in the list. For instance, you
should find that Protactinium is assigned Pt, Californium is assigned Cf, and
Lionium is assigned Iu.

Find the first element that will not be able to have a symbol assigned, because
when you get to it all the valid symbols for it are taken. (You can stop
assigning symbols at this point if you like.) Post this element along with your
solution, as a check.

Correct answer: 

Bonus: Find a way to reorder the elements so that it's possible to get through
the entire list, using the preference rules above. Post a link to your
reordered list. There are many possible answers.
"""


def possible_abbreviations(name):
    abbreviations = []
    for first_index in range(len(name) - 1):
        for second_index in range(first_index, len(name)):
            first_char = name[first_index].lower()
            second_char = name[second_index].lower()
            abbreviation = first_char + second_char
            if abbreviation not in abbreviations:
                abbreviations.append(abbreviation)
    return abbreviations


def slow_builder(names):
    """Find the first name with no possible abbreviations"""
    used = set()
    for name in names:
        for abbreviation in possible_abbreviations(name):
            if abbreviation not in used:
                used.add(abbreviation)
                break
        else:
            # If we didn't find an abbreviation, fail here
            return name
    raise ValueError("Found abbreviations for all names ({})".format(used))


def test():
    with open("elements.txt") as f:
        elements = [line.strip() for line in f]
    assert slow_builder(elements) == "Bartium"


if __name__ == "__main__":
    test()
