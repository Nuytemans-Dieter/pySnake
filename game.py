# Board representation with utility functions

from moves import Moves
import numpy as np
import queue
import random

class Board:

    # -------------
    # Game settings
    # -------------

    # Board size
    BOARD_DIM_X = 40    # Board size width
    BOARD_DIM_Y = 40    # Board size height

    # Dificulty settings
    POINTS_PER_DOT = 1  # Amount of score awarded per eaten dot
    DOTS_PER_GROWTH = 2 # Amount of dots to be eaten before the snake grows

    RANDOM_BODY_START_UTIL = {  0: ((0, -1), Moves.DOWN), 
                                1: ((1, 0),  Moves.LEFT),
                                2: ((0, 1),  Moves.UP),
                                3: ((-1, 0), Moves.RIGHT)}

    # --------------
    # Game variables
    # --------------

    score = 0                       # The current score
    snake_length = 2                # The length of the snake
    current_direction = Moves.UP    # The current direction in which the snake is moving
    
    # Location info
    body_locations = queue.Queue()   # A queue containing the locations of the snake's body
    dot_location = (0,0)

    def __init__(self):
        print("Initializing snake's starting position...")

        # Find random start position that is not at the edge of the board
        rand_start_x = random.randint(1, self.BOARD_DIM_X - 2)
        rand_start_y = random.randint(1, self.BOARD_DIM_Y - 2)
        head_location = (rand_start_x, rand_start_y)

        # Add second part of body at random spot around the head and initialize the direction
        rand_body = random.randint(0, 3)
        offset, direction = self.RANDOM_BODY_START_UTIL[rand_body]
        tail_location = (head_location[0] + offset[0], head_location[1] + offset[1])

        self.body_locations.put(tail_location)
        self.body_locations.put(head_location)
        self.current_direction = direction

        print(self.body_locations)
        print(self.get_body_locations_asarray())
        print(self.body_locations)

    
    def move(self, direction):
        if direction is not None:
            self.current_direction = direction

        # Move snake one square in the current direction (Filo queue)

        # Do point hit detection
        # If hit: generate a random new one


    def get_successors(self):
        # Only get the possible moves: not in the direction of square n°2
        return [Moves.UP, Moves.RIGHT, Moves.DOWN, Moves.LEFT]
        

    def get_score(self):
        return self.score


    def is_game_over(self):
        return False


    def get_game_view(self):
        view = [[" " for x in range(self.BOARD_DIM_X)] for y in range(self.BOARD_DIM_Y)]
        
        (x, y) = self.dot_location
        view[x][y] = "O"

        for location in self.get_body_locations_asarray():
            view[location[0]][location[1]] = "X"

        return view


    def get_body_locations_asarray(self):
        locations = []

        while not self.body_locations.empty():
            locations.append( self.body_locations.get() )

        for location in locations:
            self.body_locations.put(location)

        return locations
        


    def get_game_data(self):
        # Machine learning utility
        # Get distance (squared) to score dot
        # Get distance to own tail (straight distance, #steps) or very high number if not applicable
        # Get straight distance to the nearest wall
        # Return all data
        pass

