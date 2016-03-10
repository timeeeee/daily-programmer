from string import lowercase

KEY = dict(zip(map(str, range(1, 27)), lowercase))


def test_string_queue():
    print "testing string queue"
    string = "some string"
    sq = StringQueue(string)
    for char in string:
        assert(char == sq.pop())


def text_segment(num_string):
    print "decode {}".format(num_string)
    # Base cases:
    #   No chars- we interpreted the whole string!
    if len(num_string) == 0:
        # single empty solution
        return [""]
    
    #   one character left:
    if len(num_string) == 1:
        if num_string == "0":
            # no solutions- last character had two digits
            return []
        else:
            # single 1-character solution
            return [KEY[num_string]]

    # recurse
    # 2 or more characters left. Two possibilities:
    #   decode single character, decode rest (check for "0")
    #   decode two characters, decode rest (check for string[:2] in (1, 26))
    results = []
    # decode first character, then rest
    if num_string[0] in KEY:
        results += [KEY[num_string] + rest
                    for rest in text_segment(num_string[1:])]

    # decode first two characters, then rest
    if num_string[:2] in KEY:
        results += [KEY[num_string:2] + rest
                    for rest in text_segment(num_string[2:])]

    return results


def main():
    from sys import argv
    if len(argv) == 1:
        print "usage:"
        print "python segment.py <integer 1> .. <integer n>"
        return

    for integer in argv[1:]:
        print "{}:".format(integer)
        for result in text_segment(integer):
            print "  {}".format(result)
        print


if __name__ == "__main__":
    main()
