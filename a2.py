# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    def __init__(self, symbol, row_r, col_r):
        """(Rat, str, int, int) -> NoneType
        >>> rat = Rat('P', 1, 4)
        >>> rat.symbol
        'P'
        >>> rat.row
        1
        >>> rat.col
        4
        >>> rat.num_sprouts_eaten
        0
        """
        self.symbol = symbol
        self.row = row_r
        self.col = col_r
        self.num_sprouts_eaten = 0

    def set_location(self, row_g, col_g):
        # row_g, col_g is given row and col that we want to set
        """(Rat, int, int) -> NoneType
        >>> rat = Rat('P', 1, 4)
        >>> rat.set_location(2, 3)
        >>> rat.row
        2
        >>> rat.col
        3
        """
        self.row = row_g
        self.col = col_g

    def eat_sprout(self):
        """(Rat) -> NoneType
        >>> rat = Rat('P', 1, 4)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """(Rat) -> str
        >>> rat = Rat('J', 4, 3)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> rat.__str__()
        'J at (4, 3) ate 2 sprouts.'
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """
    def __init__(self, contents, rat1, rat2):
        """(Maze, list of list of str, Rat, Rat) -> NoneType
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ...              ['#', '.', '.', '.', '.', '.', '#'],
        ...              ['#', '.', '#', '#', '#', '.', '#'],
        ...              ['#', '.', '.', '@', '#', '.', '#'],
        ...              ['#', '@', '#', '.', '@', '.', '#'],
        ...              ['#', '#', '#', '#', '#', '#', '#']],
        ...             Rat('J', 0 0),
        ...             Rat('P', 0, 3))

        >>> maze.num_sprouts_left
        3
        """
        self.maze = contents
        self.rat_1 = rat1
        self.rat_2 = rat2
        self.num_sprouts_left = 0
        for content in contents:
            for char in content:
                if char == SPROUT:
                    self.num_sprouts_left += 1

    def is_wall(self, row_m, col_m):
        """(Maze, int, int) -> bool
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ...              ['#', '.', '.', '.', '.', '.', '#'],
        ...              ['#', '.', '#', '#', '#', '.', '#'],
        ...              ['#', '.', '.', '@', '#', '.', '#'],
        ...              ['#', '@', '#', '.', '@', '.', '#'],
        ...              ['#', '#', '#', '#', '#', '#', '#']],
        ...             Rat('J', 0, 0),
        ...             Rat('P', 0, 3))
        >>> maze.is_wall(0, 2)
        True
        >>> maze.is_wall(3, 1)
        False
        """
        self.row = row_m
        self.col = col_m
        return self.maze[row_m][col_m] == WALL
        # indexing based on the method where the maze starts at (0,0) for the (row, col)

    def get_character(self, row_gc, col_gc):
        """(Maze, int, int) -> str
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ...              ['#', '.', '.', '.', '.', '.', '#'],
        ...              ['#', '.', '#', '#', '#', '.', '#'],
        ...              ['#', '.', '.', '@', '#', '.', '#'],
        ...              ['#', '@', '#', '.', '@', '.', '#'],
        ...              ['#', '#', '#', '#', '#', '#', '#']],
        ...             Rat('J', 0, 0),
        ...             Rat('P', 0, 3))
        >>> maze.get_character(0,3)
        'P'
        >>> maze.get_character(2, 4)
        '#'
        >>> maze.get_character(1, 5)
        '.'
        """
        # replace char with rats, then return the char
        if self.rat_1.row == row_gc and self.rat_1.col == col_gc:
            return self.rat_1.symbol
        elif self.rat_2.row == row_gc and self.rat_2.col == col_gc:
            return self.rat_2.symbol
        else:
            return self.maze[row_gc][col_gc]

    def move(self, rat, v_change, h_change):
        """(Maze, Rat, int, int) -> bool
        >>> rat_1 = Rat('J', 0, 0)
        >>> rat_2 = Rat('P', 0, 3)
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ...              ['#', '.', '.', '.', '.', '.', '#'],
        ...              ['#', '.', '#', '#', '#', '.', '#'],
        ...              ['#', '.', '.', '@', '#', '.', '#'],
        ...              ['#', '@', '#', '.', '@', '.', '#'],
        ...              ['#', '#', '#', '#', '#', '#', '#']],
        ...             rat_1,
        ...             rat_2)
        >>> maze.move(RAT_1_CHAR, 1, 0)
        False
        >>> maze.move(RAT_2_CHAR, 1, -1)
        True
        """
        if isinstance(rat, str):
            if rat == RAT_1_CHAR:
                rat = self.rat_1
            elif rat == RAT_2_CHAR:
                rat = self.rat_2

        new_row = rat.row + v_change
        new_col = rat.col + h_change

        location = self.maze[new_row][new_col]

        # checking if there is a wall blocking the way
        if location == WALL:
            return False

        # move the rat
        rat.set_location(new_row, new_col)

        # check for sprout
        if location == SPROUT:
            rat.eat_sprout()
            self.maze[new_row][new_col] = HALL
            self.num_sprouts_left -= 1
        return True

    def __str__(self):
        """(Maze) -> str
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ...              ['#', '.', '.', '.', '.', '.', '#'],
        ...              ['#', '.', '#', '#', '#', '.', '#'],
        ...              ['#', '.', '.', '@', '#', '.', '#'],
        ...              ['#', '@', '#', '.', '@', '.', '#'],
        ...              ['#', '#', '#', '#', '#', '#', '#']],
        ...             Rat('J', 1, 1),
        ...             Rat('P', 1, 4))
        >>> print(str(maze))
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        maze_copy = [row[:] for row in self.maze]

        # put the rats into the maze
        for rat in [self.rat_1, self.rat_2]:
            r, c = rat.row, rat.col
            maze_copy[r][c] = rat.symbol

        # join each row into a string
        maze_str = '\n'.join(''.join(row) for row in maze_copy)

        # add rats’ info at the bottom
        rats_str = '\n'.join(str(rat) for rat in [self.rat_1, self.rat_2])

        return maze_str + '\n' + rats_str

import doctest
doctest.testmod()
