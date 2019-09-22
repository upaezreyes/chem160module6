from sudoku_class import *

asudoku = sudoku()  # Create an empty 9x9 sudoku puzzle
asudoku.generate()  # Generates a solved sudoku puzzle
asudoku.display()   # Print out current state of sudoku puzzle
asudoku = sudoku()
asudoku.makepuzzle(40) # Creates a sudoku puzzle containing n initial clues
asudoku.display()   # Print out current state of sudoku puzzle
asudoku.solved()    # Test if puzzle is solved, returns Ture or False
asudoku.solve()    # Attempt to solve the sudoku puzzle
asudoku.display()   # Print out current state of sudoku puzzle

# to finish solving the soduku puzzle
asudoku.solve()   # attenpt to solve sudoku
asudoku.display()   # print out current soduku puzzle

# asudoku.set_random(n)  # Remove all but n clues from a generated puzzle
