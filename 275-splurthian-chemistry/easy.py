def valid_abbreviation(element, abbreviation):
    """Check if this is a valid abbreviation for the element.

    The abbreviation is valid if both characters can be found in the same order
    in the element name.
    """
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
    if element[0] == abbreviation[0]:
        return valid_abbreviation_recursive(element[1:], abbreviation[1:])
    else:
        return valid_abbreviation_recursive(element[1:], abbreviation)


def test_validation():
    assert valid_abbreviation("spenglerium", "ee") is True
    assert valid_abbreviation("zeddemorium", "zr") is True
    assert valid_abbreviation("venkmine", "kn") is True
    assert valid_abbreviation("stantzon", "zt") is False
    assert valid_abbreviation("melintzum", "nn") is False
    assert valid_abbreviation("tullium", "ty") is False

    assert valid_abbreviation_recursive("spenglerium", "ee") is True
    assert valid_abbreviation_recursive("zeddemorium", "zr") is True
    assert valid_abbreviation_recursive("venkmine", "kn") is True
    assert valid_abbreviation_recursive("stantzon", "zt") is False
    assert valid_abbreviation_recursive("melintzum", "nn") is False
    assert valid_abbreviation_recursive("tullium", "ty") is False


if __name__ == "__main__":
    test_validation()
