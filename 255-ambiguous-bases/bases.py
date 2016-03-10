"""
challenge inputs
    101 2
    101 16
    120973 25

Bonus Inputs
    25190239128039083901283 100
    251902391280395901283 2398
"""

def digit_list_to_decimal(digits, base):
    total = 0
    for pos, digit in enumerate(reversed(digits)):
        total += digit * base**pos
    return total

def ambiguous_base_to_decimal(number, base):
    """
    Take both number and base as strings.
    """
    # results begin as an empty list for each digit, plus an extra empty
    # answer to build from
    solutions = [[] for _ in xrange(len(number))]
    solutions.append([[]])
    num_digits = len(number)
    base_int = int(base)
    num_base_digits = len(base)
    # For every digit starting at the end, try each possible number ending
    # there that could be single digit in the original number.
    for last_digit_index in range(num_digits - 1, -1, -1):
        max_digit_length = min(num_base_digits, last_digit_index + 1)
        for digit_length in range(1, max_digit_length + 1):
            first_digit_index = last_digit_index - digit_length + 1
            group = number[first_digit_index:last_digit_index + 1]
            decimal_this_digit = int(group)
            if (len(group) == 1 or group[0] != "0" and decimal_this_digit < base_int):
                # If this is a valid digit, add it to all previous solutions
                # and save answers for this digit
                previous_solutions = solutions[last_digit_index + 1]
                for solution in previous_solutions:
                    solutions[last_digit_index - digit_length + 1].append(
                        [decimal_this_digit] + solution)
    return [digit_list_to_decimal(s, base_int) for s in solutions[0]]


if __name__ == "__main__":
    print ambiguous_base_to_decimal("101", "2")
    print ambiguous_base_to_decimal("101", "16")
    print ambiguous_base_to_decimal("120973", "25")
    print ambiguous_base_to_decimal("25190239128039083901283", "100")[:10]
    print ambiguous_base_to_decimal("251902391280395901283", "2398")[:10]
