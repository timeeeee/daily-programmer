"""
Here is a weird balance between object oriented and functional programming!
When I write a bunch of functions to call with a variable parameter where I
already know it's going to be the same variable passed every time, I feel like
I probably ought to write a class so I can just call methods of it. But, when
I don't expect the state of the class to change, and I'm just going to do the
same set of operations on it every time, I feel like it ought to just be
a set of functions.
"""
SNAKE = "s"
SPACE = " "
FOOD = "*"
PIT = "O"


class SnakeBoard(object):
    def __init__(self, string):
        """Convert a string into a 2d array snake board"""
        self.left_to_eat = string.count(FOOD)

        # Cut border off of board
        self.board = [
            list(row_str.strip("|")) for row_str in string.split("\n")[1:-2]]
        print "got board... {} to eat".format(self.left_to_eat)

        self.height = len(self.board)
        self.width = len(self.board[0])

        # Get start position
        row_plus_1, col_plus_1 = divmod(
            string.replace("\n", "").find(SNAKE), self.width + 2)
        self.start = (row_plus_1 - 1, col_plus_1 - 1)

        assert self.board[row_plus_1 - 1][col_plus_1 - 1] == SNAKE

    def adjacent(self, space):
        """Return coordinates of open adjacent spaces"""
        row, col = space
        adjacents = []
        for row_delta, col_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = row + row_delta
            new_col = col + col_delta
            if new_row >= 0 and new_col >= 0:
                if new_row < self.height and new_col < self.width:
                    new_contents = self.board[new_row][new_col]
                    if (new_contents == SPACE or new_contents == FOOD):
                        adjacents.append((new_row, new_col))
        return adjacents

    def __str__(self):
        top_bottom = "+" + "-" * self.width + "+"
        return "\n".join([top_bottom] +
                         ["|" + "".join(row) + "|" for row in self.board] +
                         [top_bottom])

    def solve(self, start=None):
        """Return the shortest safe path that eats all the food"""
        if start is None:
            start = self.start

        # print "trying space {}; {} left to eat".format(start, self.left_to_eat)

        # Save contents of this space so we can recurse
        row, col = start
        previous_contents = self.board[row][col]
        if previous_contents == FOOD:
            # Base case- we just finished all the food!
            if self.left_to_eat == 1:
                return [start]
            self.left_to_eat -= 1

        # Set this spot to full-of-snake
        self.board[row][col] = SNAKE

        best_path = None
        best_length = float("inf")

        for next_space in self.adjacent(start):
            rest_of_path = self.solve(next_space)
            if rest_of_path is not None:
                length_of_rest = len(rest_of_path)
                if length_of_rest < best_length:
                    best_path = rest_of_path
                    best_length = length_of_rest

        # Reset this space to original contents
        self.board[row][col] = previous_contents
        if previous_contents == FOOD:
            self.left_to_eat += 1

        # Return best path found, plus this space.
        if best_path is None:
            return None
        else:
            return [start] + best_path
                

BOARD3 = ("+- map 3 --+\n"
         "|          |\n"
         "| s OO  *  |\n"
         "|    OOO   |\n"
         "|    * OOOO|\n"
         "|          |\n"
         "+----------+\n")

BOARD16 = ("+--- map 16 ---+\n"
         "|       *   *  |\n"
         "|    O     *  O|\n"
         "|  O     OO   *|\n"
         "| s      *     |\n"
         "|O O* O* OO    |\n"
         "+--------------+\n")


if __name__ == "__main__":
    snake = SnakeBoard(BOARD16)
    print snake
    print snake.solve()
