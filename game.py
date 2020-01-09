# Board representation with utility functions

from moves import Moves
from pySnake_util.vector import addVectors2D
import numpy as np
import queue
import random

class Board:

    # -------------
    # Game settings
    # -------------

    # Board size
    BOARD_DIM_X = 30    # Board size width
    BOARD_DIM_Y = 30    # Board size height

    # Dificulty settings
    SCORE_PER_DOT = 1   # Amount of score awarded per eaten dot
    DOTS_PER_GROWTH = 2 # Amount of dots to be eaten before the snake grows

    RANDOM_BODY_START_UTIL =  {  
                                0: ((0, -1), Moves.DOWN), 
                                1: ((1, 0),  Moves.LEFT),
                                2: ((0, 1),  Moves.UP),
                                3: ((-1, 0), Moves.RIGHT)
                              }

    DIRECTION_OFFSET_VECTOR = { 
                                Moves.DOWN: (0, 1),
                                Moves.LEFT: (-1, 0),
                                Moves.UP:   (0, -1),
                                Moves.RIGHT:(1, 0)
                              }

    DIRECTION_OPPOSITES =     {
                                Moves.DOWN:  Moves.UP,
                                Moves.LEFT:  Moves.RIGHT,
                                Moves.UP:    Moves.DOWN,
                                Moves.RIGHT: Moves.LEFT
                              }

    # --------------
    # Game variables
    # --------------

    game_over = False               # Keep track whether the game is over
    score = 0                       # The current score
    dots_to_grow = DOTS_PER_GROWTH  # Counter to remember when the snake should grow (grows when this reaches 0)
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
        #tail_location = (head_location[0] + offset[0], head_location[1] + offset[1])
        tail_location = addVectors2D(head_location, offset)

        self.body_locations.put(tail_location)
        self.body_locations.put(head_location)
        self.current_direction = direction

        # Generate a random starting point for the food dot
        rand_dot_x = random.randint(0, self.BOARD_DIM_X - 1)
        rand_dot_y = random.randint(0, self.BOARD_DIM_Y - 1)
        self.dot_location = (rand_dot_x, rand_dot_y)

    
    def move(self, direction):
        if direction is not None:
            self.current_direction = direction

        body_locations_list = self.get_body_locations_asarray()

        # Calculate the new head position
        new_head_location = addVectors2D(body_locations_list[-1], self.DIRECTION_OFFSET_VECTOR[ self.current_direction ])

        # Do point hit detection
        # If hit: generate a random new one
        # Do wall collision detection
        (x, y) = new_head_location
        if x < 0 or x >= self.BOARD_DIM_X or y < 0 or y >= self.BOARD_DIM_Y:
            self.game_over = True
            return
        elif x is self.dot_location[0] and y is self.dot_location[1]:
            self.score += self.SCORE_PER_DOT    # Add score
            self.dots_to_grow -= 1              # Subtract dots needed to grow
            # Generate new random dot
            rand_dot_x = random.randint(0, self.BOARD_DIM_X - 1)
            rand_dot_y = random.randint(0, self.BOARD_DIM_Y - 1)
            self.dot_location = (rand_dot_x, rand_dot_y)
        
        self.body_locations.put(new_head_location)  # Add the new head to the body list
        if self.dots_to_grow is not 0:              # If it is NOT time to grow
            self.body_locations.get()               # Remove the last part of the tail
        



    def get_successors(self):
        # Only get the possible moves: not in the direction of square n°2
        moves = [Moves.UP, Moves.RIGHT, Moves.DOWN, Moves.LEFT]          # Get all possible directions
        moves.remove(self.DIRECTION_OPPOSITES[self.current_direction])   # Remove the opposite direction and return
        return moves
        

    def get_score(self):
        return self.score


    def is_game_over(self):
        return self.game_over


    def get_game_view(self):
        view = [["_" for x in range(self.BOARD_DIM_X)] for y in range(self.BOARD_DIM_Y)]
        
        (x, y) = self.dot_location
        view[y][x] = "O"

        for location in self.get_body_locations_asarray():
            view[location[1]][location[0]] = "X"

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

