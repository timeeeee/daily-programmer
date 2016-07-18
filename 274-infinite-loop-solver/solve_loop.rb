=begin
Reddit Daily Programmer Challenge #274 Hard: Infinite Loop Solver

Infinite Loop is a mobile game that consists of n*m tiles, placed in a n*m
grid. There are 16 different tiles.

Every tile may or may not have a "pipe" going up, a "pipe" going right, a
"pipe" going down, and a "pipe" going left. All combinations of those are
valid, legal tiles.

At the beginning of the game, the grid is filled with those tiles. The player
may then choose some tile and rotate it 90 degrees to the right. The player may
do this an unlimited amount of times.

The objective is to create a closed loop: every pipe must have another tile
facing it in the adjacent tile - for example if some tile has a pipe going
right, its adjacent tile to the right must have a pipe going left.

Your task is to write a program that, given an initial grid of tiles, outputs a
solution to that grid.

Strategy:
Recursive with backtracking. For each tile, try all four rotations. At each
step, only check previously visited tiles (left and up) for pipe connections.
Base case is any valid rotation of the final (bottom right) tile.
=end

class Board
  def initialize filename
    @grid = open(filename).map do |line|
      line.split.map { |bitmask| Tile.new bitmask }
    end
  end

  def solve pos=[0, 0]
    row, col = pos
    tile = @grid[row][col]
    tile.possible_rotations.times do
      if check row, col
        if last_tile? row, col
          puts self
        else
          solve next_tile(pos)
        end
      end
      tile.rotate
    end
  end

  def next_tile pos
    row, col = pos
    if col == width - 1
      [row + 1, 0]
    else
      [row, col + 1]
    end
  end

  def check row, col
    # Are all of the pipes connected?
    tile = @grid[row][col]

    # If a pipe leads upwards, we must have a neighbor that is connected down
    if tile.connected? :up
      return false if row == 0 or not grid[row - 1][col].connected? :down
    end

    # If a pipe leads left, we must have a neighbor that is connected right
    if tile.connected? :left
      return false if col == 0 or not grid[row][col - 1].connected? :right
    end

    # For right and downwards neighbors, we will check their connections later.
    # All we need to check now is that if a pipe leads down or right, we have
    # a neighbor there.
    return false if tile.connected? :down and row == height - 1
    return false if tile.connected? :right and col == width - 1

    # If we made it this far, all connections are fine
    true
  end

  def last_tile? row, col
    row == height - 1 and col == width - 1
  end

  def tile row, col
    @grid[row][col]
  end

  def width
    @grid[0].length
  end

  def height
    @grid.length
  end

  def size
    [width, height]
  end
end


class Tile
  @@directions = {:up => 0, :right => 1, :down => 2, :left => 3}
  @@rotation_counts = {0 => 1, 15 => 1, 5 => 2, 10 => 2}

  def initialize bitmask
    # up: 1, right: 2, down: 4, left: 8
    @bitmask = bitmask

    # Number of clockwise rotations
    @rotations = 0

    # Set rotation counts default
    @@rotation_counts.default = 4
  end

  def connected? direction
    mask = 2**(@@directions[direction] + @rotations % 4)
    puts mask
    @bitmask & mask > 0
  end

  def rotate
    @rotations += 1
  end

  def rotations
    @rotations
  end

  def possible_rotations
    @@rotation_counts[@bitmask]
  end
end

def debug
  board = Board.new "board.txt"
  width, height = board.size  
  (0..height).each do |row|
    (0..width).each do |col|
      check = board.check row, col
      puts "row = #{row}, col = #{col}: #{check}"
    end
  end
end
