"""
Clone of 2048 game.
"""

import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    first_line = move_the_zero(line)
    index = 0
    merge_line = [0] * len(first_line)
    while index < len(first_line):
        if index != len(first_line) - 1:
            if first_line[index] == first_line[index + 1]:
                merge_line[index] = first_line[index] * 2
                index += 2
            else:
                merge_line[index] = first_line[index]
                index += 1
        else:
            merge_line[index] = first_line[index]
            index += 1
            
    second_line = move_the_zero(merge_line)
    return second_line
    
def move_the_zero(original):
    """
    Move all the zero to the end.
    """
    goal = [0] * len(original)
    index = 0
    for num in original:
        if num != 0:
            goal[index] = num
            index += 1
    return goal

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        
        self._all_initial_tiles = {
            UP: [(0, col) for col in range(grid_width)],
            DOWN: [(grid_height - 1, col) for col in range(grid_width)],
            LEFT: [(row, 0) for row in range(grid_height)],
            RIGHT: [(row, grid_width - 1) for row in range(grid_height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two initial tiles.
        """
        self._board = [[ 0 for dummy_col in range(self._grid_width)] 
                           for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        board_info = "The Board:\n"
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                board_info += str(self._board[row][col])
                board_info += ' '
            board_info += '\n'
        return board_info

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add a new tile if any tiles moved.
        """
        initial_tiles = self._all_initial_tiles[direction]
        num_steps = 0
        tiles_changed = 0
        if direction == UP or direction == DOWN:
            num_steps = self._grid_height
        else:
            num_steps = self._grid_width
            
        for start_cell in initial_tiles:
            temp_line = []
            for step in range(num_steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                temp_line.append(self._board[row][col])
            merged_line = merge(temp_line)
            for step in range(num_steps):
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                if self._board[row][col] != merged_line[step]:
                    self._board[row][col] = merged_line[step]
                    tiles_changed += 1
                    
        if tiles_changed > 0: 
            self.new_tile()
                
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty square.  
        The tile should be 2 90% of the time and 4 10% of the time.
        """
        empty_list = []
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._board[row][col] == 0: 
                    empty_square = row, col
                    empty_list.append(empty_square)
        if len(empty_list) > 0:
            chosen = random.choice(empty_list)
            random_num = random.randrange(0, 10)
            if random_num == 0:
                self._board[chosen[0]][chosen[1]] = 4
            else:
                self._board[chosen[0]][chosen[1]] = 2
            
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]

test = TwentyFortyEight(4, 4)
