# Crafting-Quality-Code
Developing a Rat Race Game based on interactive classes

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

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """
        (Rat, str, int, int) -> NoneType
        A Rat with a symbol, row, column and count of number of sprouts eaten.

        Precondition:
        len(symbol) == 1
        row >= 0
	col >= 0
        
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
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """
        (Rat, int, int) -> NoneType
        Set a Rat's location to the given row and column.
        
        >>> rat = Rat('P', 1, 4)
        >>> rat.set_location(6,3)
        >>> rat.row
        6
        >>> rat.col
        3
        """
        self.row = row
        self.col = col
    

    def eat_sprout(self):
        """
        (Rat) -> NoneType
        A Rat with an addition to number of sprouts eaten.
        
        >>> rat = Rat('P', 1, 4)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """
        
        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        (Rat) -> str
        A Rat with a symbol, row, column and count of number of sprouts eaten.
        
        >>> rat = Rat('J', 4, 3)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> str(rat)
        'J at (4, 3) ate 2 sprouts.'
        """
        
        return '{} at ({}, {}) ate {} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType
        A maze with two rats and number of sprouts uneaten.
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                         ['#', '.', '.', '.', '.', '.', '#'],\
                         ['#', '.', '#', '#', '#', '.', '#'],\
                         ['#', '.', '.', '@', '#', '.', '#'],\
                         ['#', '@', '#', '.', '@', '.', '#'],\
                         ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> maze.maze 
        [['#', '#', '#', '#', '#', '#', '#'], ['#', 'J', '.', '.', 'P', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> maze.num_sprouts_left
        3
        >>> maze.rat_1.symbol
        'J'
        >>> maze.rat_2.symbol
        'P'
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        self.maze[rat_1.row][rat_1.col] = rat_1.symbol
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol

        num_sprouts_left = 0
        for row in self.maze:
            if SPROUT in row:
                num_sprouts_left += row.count(SPROUT)
        self.num_sprouts_left = num_sprouts_left

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool
        Check and return True if the character at given row and col is a wall.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                         ['#', '.', '.', '.', '.', '.', '#'],\
                         ['#', '.', '#', '#', '#', '.', '#'],\
                         ['#', '.', '.', '@', '#', '.', '#'],\
                         ['#', '@', '#', '.', '@', '.', '#'],\
                         ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> maze.is_wall(1,2)
        False
        >>> maze.is_wall(2,5)
        False
        >>> maze.is_wall(0,0)
        True
        >>> maze.is_wall(5,4)
        True
        """
        return self.get_character(row, col) == WALL
        

    def get_character(self, row, col):
        """(Maze, int, int) -> str
        Return the character in the maze at the given row and column. If there is a rat
        at that location, then its character should be returned rather than HALL.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                         ['#', '.', '.', '.', '.', '.', '#'],\
                         ['#', '.', '#', '#', '#', '.', '#'],\
                         ['#', '.', '.', '@', '#', '.', '#'],\
                         ['#', '@', '#', '.', '@', '.', '#'],\
                         ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> maze.get_character(0,0)
        '#'
        >>> maze.get_character(1,1)
        'J'
        >>> maze.get_character(1,4)
        'P'
        >>> maze.get_character(2,1)
        '.'
        >>> maze.get_character(3,3)
        '@'
        """
        if 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0]):
            # Check if the character is a rat or another maze character
            if (row, col) == (self.rat_1.row, self.rat_1.col):
                return self.rat_1.symbol
            elif (row, col) == (self.rat_2.row, self.rat_2.col):
                return self.rat_2.symbol
            else:
                return self.maze[row][col]
        else:
            print('These coordinates do not exist')


    def move(self, rat, vertical, horizontal):
        """(Maze, Rat, int, int)-> bool
        Move the rat in the given direction, unless there is a wall in the way. Also, check
        for a Brussels sprout at that location and, if present: have the rat eat the Brussels
        sprout, make that location a HALL and decrease the value that num_sprouts_left refers
        to by one. Return True if and only if there wasn't a wall in the way.

        >>> rat_1 = Rat('J', 1, 1)
        >>> rat_2 = Rat('P', 1, 4)
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                         ['#', '.', '.', '.', '.', '.', '#'],\
                         ['#', '.', '#', '#', '#', '.', '#'],\
                         ['#', '.', '.', '@', '#', '.', '#'],\
                         ['#', '@', '#', '.', '@', '.', '#'],\
                         ['#', '#', '#', '#', '#', '#', '#']],\
                        rat_1,\
                        rat_2)
        >>> maze.move(rat_1, NO_CHANGE, RIGHT)
        True
        >>> rat_1.row
        1
        >>> rat_1.col
        2
        >>> maze.move(rat_1, NO_CHANGE, RIGHT)
        True
        >>> rat_1.row
        1
        >>> rat_1.col
        3
        >>> maze.move(rat_2, NO_CHANGE, LEFT)
        True
        >>> rat_2.eat_sprout()
        >>> rat_2.num_sprouts_eaten
        1
        >>> maze.num_sprouts_left
        3
        >>> maze.move(rat_2, DOWN, NO_CHANGE)
        False
        >>> rat_2.row
        1
        >>> rat_2.col
        3
        >>> maze.move(rat_1, DOWN, NO_CHANGE)
        False
        >>> maze.move(rat_1, NO_CHANGE, LEFT)
        True
        >>> maze.move(rat_1, NO_CHANGE, LEFT)
        True
        >>> rat_1.row
        1
        >>> rat_1.col
        1
        >>> maze.move(rat_2, DOWN, RIGHT)
        False
        >>> rat_2.num_sprouts_eaten
        1
        >>> maze.num_sprouts_left
        3
        
        """
        
        new_row = rat.row + vertical
        new_col = rat.col + horizontal

        if self.is_wall(new_row, new_col):
            return False
        
        self.maze[new_row][new_col] = HALL
        rat.set_location(new_row, new_col)
        
        if self.get_character(new_row, new_col) == SPROUT:
            rat.eat_sprout()
            self.num_sprouts_left -= 1

        self.maze[new_row][new_col] = rat.symbol

        return True


    def __str__(self):
        """(Maze) -> str
        Return a string representation of the Maze.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                         ['#', '.', '.', '.', '.', '.', '#'],\
                         ['#', '.', '#', '#', '#', '.', '#'],\
                         ['#', '.', '.', '@', '#', '.', '#'],\
                         ['#', '@', '#', '.', '@', '.', '#'],\
                         ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
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

        maze_str = ''
        for row in self.maze:
            for char in row:
                maze_str += char
            maze_str += '\n'
        return maze_str + str(self.rat_1) + '\n' + str(self.rat_2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
