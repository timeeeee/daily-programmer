"""Modified Game of Threes: at each step, add or subtract 1 or 2, then divide
by three. Game ends when n hits 1. All add/subtract operations must add up to
zero. Solutions in format [(number, op), (number, op)...].
"""

# from math import log

DEBUG = True


def recursive_game_of_threes(n, op_total=0, solution_cache={}):
    """Take number n, sum of solutions so far, dictionary of found solutions,
    return list of all possible solutions for n.
    """

    if DEBUG:
        print "game of threes({}):".format(n)

    # Check cache
    if (n, op_total) in solution_cache:
        if DEBUG:
            print "found solution threes({}) = {} in cache".format(
                n, solution_cache[(n, op_total)])
        return solution_cache[(n, op_total)]

    # Should check here if possible to find solution- op_total magnitude
    # too high? Check with log_3(n) + 1?

    # Base cases - 2, 3, 4, 5
    if n == 2:
        if DEBUG:
            print "base case: 2"
        if op_total == -1:
            return [[(2, 1)]]
        else:
            return []
    elif n == 3:
        if DEBUG:
            print "base case: 3"
        if op_total == 0:
            return [[(3, 0)]]
        else:
            return []
    elif n == 4:
        if DEBUG:
            print "base case: 4"
        if op_total == 1:
            return [[(4, -1)]]
        elif op_total == -2:
            return [[(4, 2), (3, 0)]]
        else:
            return []
    elif n == 5:
        if DEBUG:
            print "base case: 5"
        if op_total == 2:
            return [[(5, -2)]]
        elif op_total == -1:
            return [[(5, 1), (3, 0)]]
        else:
            return []

    # Not base case or known solution - solve recursively
    # Build list of all possible solutions
    mod = n % 3
    if DEBUG:
        print "solve recursively. {} mod 3 = {}".format(n, mod)
    solutions = []
    if mod == 0:
        # Add no-op solutions
        for solution in recursive_game_of_threes(
                n / 3, op_total, solution_cache):
            solutions += [[(n, 0)] + solution]

    elif mod == 1:
        # Add subtract-one solutions
        for solution in recursive_game_of_threes(
                (n - 1) / 3, op_total - 1, solution_cache):
            solutions += [[(n, -1)] + solution]

        # Add add-two solutions
        for solution in recursive_game_of_threes(
                (n + 2) / 3, op_total + 2, solution_cache):
            solutions += [[(n, 2)] + solution]

    elif mod == 2:
        # Add subtract-two solutions
        for solution in recursive_game_of_threes(
                (n - 2) / 3, op_total - 2, solution_cache):
            solutions += [[(n, -2)] + solution]

        # Add add-one solutions
        for solution in recursive_game_of_threes(
                (n + 1) / 3, op_total + 1, solution_cache):
            solutions += [[(n, 1)] + solution]

    # Add solution list to cache
    solution_cache[(n, op_total)] = solutions

    return solutions


def main():
    for solution in recursive_game_of_threes(929):
        for n, op in solution:
            print "{} {}".format(n, op)
        print 1
        print


if __name__ == "__main__":
    main()
