"""
The inhabitants of the planet Splurth are building their own periodic table of
the elements. Just like Earth's periodic table has a chemical symbol for each
element (H for Hydrogen, Li for Lithium, etc.), so does Splurth's. However,
their chemical symbols must follow certain rules:

* All chemical symbols must be exactly two letters, so B is not a valid symbol
  for Boron.
* Both letters in the symbol must appear in the element name, but the first
  letter of the element name does not necessarily need to appear in the symbol.
  So Hg is not valid for Mercury, but Cy is.
* The two letters must appear in order in the element name. So Vr is valid for
  Silver, but Rv is not. To be clear, both Ma and Am are valid for Magnesium,
  because there is both an a that appears after an m, and an m that appears
  after an a.
* If the two letters in the symbol are the same, it must appear twice in the
  element name. So Nn is valid for Xenon, but Xx and Oo are not.

As a member of the Splurth Council of Atoms and Atom-Related Paraphernalia, you
must determine whether a proposed chemical symbol fits these rules.

Write a function that, given two strings, one an element name and one a
proposed symbol for that element, determines whether the symbol follows the
rules. If you like, you may parse the program's input and output the result,
but this is not necessary.

The symbol will have exactly two letters. Both element name and symbol will
contain only the letters a-z. Both the element name and the symbol will have
their first letter capitalized, with the rest lowercase. (If you find that too
challenging, it's okay to instead assume that both will be completely
lowercase.)

Examples:
  Spenglerium, Ee -> true
  Zeddemorium, Zr -> true
  Venkmine, Kn -> true
  Stantzon, Zt -> false
  Melintzum, Nn -> false
  Tullium, Ty -> false
"""


def valid_abbreviation(element, abbreviation):
    """Check if this is a valid abbreviation for the element.

    The abbreviation is valid if both characters can be found in the same order
    in the element name.
    """
    element = element.lower()
    abbreviation = abbreviation.lower()
    start = 0
    for char in abbreviation:
        # Find the first occurence of this letter, starting at the last letter
        try:
            pos = element.index(char, start)
        except ValueError:
            return False

        start = pos + 1

    # We've found all the letters, so the abbreviation is valid
    return True


def valid_abbreviation_recursive(element, abbreviation):
    # Base cases:
    # If abbreviation is empty, all letters were found
    if abbreviation == "":
        return True

    # Otherwise, if the element name is empty, they weren't
    if element == "":
        return False

    # Otherwise, search the rest of the element name
    if element[0].lower() == abbreviation[0].lower():
        return valid_abbreviation_recursive(element[1:], abbreviation[1:])
    else:
        return valid_abbreviation_recursive(element[1:], abbreviation)


def test_validation():
    assert valid_abbreviation("Spenglerium", "Ee") is True
    assert valid_abbreviation("Zeddemorium", "Zr") is True
    assert valid_abbreviation("Venkmine", "Kn") is True
    assert valid_abbreviation("Stantzon", "Zt") is False
    assert valid_abbreviation("Melintzum", "Nn") is False
    assert valid_abbreviation("Tullium", "Ty") is False

    assert valid_abbreviation_recursive("Spenglerium", "Ee") is True
    assert valid_abbreviation_recursive("Zeddemorium", "Zr") is True
    assert valid_abbreviation_recursive("Venkmine", "Kn") is True
    assert valid_abbreviation_recursive("Stantzon", "Zt") is False
    assert valid_abbreviation_recursive("Melintzum", "Nn") is False
    assert valid_abbreviation_recursive("Tullium", "Ty") is False


if __name__ == "__main__":
    test_validation()
