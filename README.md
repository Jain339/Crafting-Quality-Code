# Rat Race Maze Game

## Overview

This project implements a two-player maze-based game, Rat Race, where two rats—Jen (`J`) and Paul (`P`) compete to navigate a maze and eat Brussels sprouts (`@`). The maze consists of walls (`#`), hallways (`.`), and sprouts. Each player controls a rat and attempts to collect as many sprouts as possible while avoiding walls.

The project was developed to practice object-oriented programming in Python, focusing on class design, method implementation, and handling interactions between objects in a 2D grid environment.

When the rats move through the maze:

* They cannot pass through walls.
* If they land on a sprout, they eat it, increasing their score and replacing the sprout with a hallway tile.
* The game ends when no sprouts remain.

This project is fully console-based and also supports integration with a simple Tkinter GUI (`rat_race.py`) if you wish to extend it.

## Project Structure

The repository contains the following files:

* `a2.py`: Main file containing the implementation of the `Rat` and `Maze` classes.
* `rat_race.py`: (Optional) Tkinter-based GUI to play the game interactively.
* `maze.txt`: Example maze configuration to test the program.
* `README.md`: Documentation for the project.

## Game Rules

* `#`: Wall – rats cannot move into these.
* `.`: Hallway – empty space that rats can move into.
* `@`: Sprout – collectible item; when eaten, it becomes a hallway.
* `J`: Jen’s rat.
* `P`: Paul’s rat.

### Controls (if GUI is used):

* **Jen**: `w` (up), `s` (down), `a` (left), `d` (right).
* **Paul**: `i` (up), `k` (down), `j` (left), `l` (right).

## Classes and Methods

### `Rat` class

Represents a rat in the maze.

* `__init__(self, symbol, row, col)`: Creates a rat with a symbol, initial row, and column.
* `set_location(self, row, col)`: Updates the rat’s position.
* `eat_sprout(self)`: Increases the number of sprouts eaten.
* `__str__(self)`: Returns a string summary of the rat’s status.

### `Maze` class

Represents the 2D maze environment.

* `__init__(self, contents, rat1, rat2)`: Initializes the maze with its layout and rats.
* `is_wall(self, row, col)`: Returns `True` if a given location is a wall.
* `get_character(self, row, col)`: Returns the character at a position (rat, wall, sprout, or hallway).
* `move(self, rat, v_change, h_change)`: Moves a rat if possible, updating sprouts eaten.
* `__str__(self)`: Displays the maze grid along with rats’ stats.

## How to Run

### Option 1: Run directly in Python

1. Clone the repository:

   ```
   git clone https://github.com/your-username/rat-race.git
   cd rat-race
   ```

2. Open `a2.py` in your Python IDE or terminal.

3. Run the file:

   ```
   python a2.py
   ```

The doctests included in the code will automatically run and validate functionality.

### Option 2: Run with the GUI (Tkinter)

1. Place `a2.py`, `rat_race.py`, and `maze.txt` in the same directory.
2. Open `rat_race.py` in your Python IDE.
3. Run the file:

   ```
   python rat_race.py
   ```
4. Play the game using the keyboard controls listed above.

## Sample Maze

```
#######
#J..P.#
#.###.#
#..@#.#
#@#.@.#
#######
```

* Jen (`J`) starts at row 1, column 1.
* Paul (`P`) starts at row 1, column 4.
* Sprouts (`@`) are scattered in the maze.
* The rats must collect all sprouts to end the game.

## Testing

* Doctests are provided within the code for key methods in both `Rat` and `Maze`.
* Run the file directly to trigger doctests.
* Additional unit testing can be added for extended functionality.

## Future Improvements

* Extend to support more than two rats.
* Add difficulty levels with larger and more complex mazes.
* Implement a scoring system with time penalties.
* Enhance the GUI with animations and better graphics.

## License

This project was completed as part of an academic assignment. You are free to use and adapt the code for learning purposes.


