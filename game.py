# Board representation with utility functions

from moves import Moves

class Board:

    # -------------
    # Game settings
    # -------------

    # Board size
    BOARD_DIM_X = 40    # Board size width
    BOARD_DIM_Y = 40    # Board size height

    # Dificulty settings
    POINTS_PER_DOT = 1  # Amount of score awarded per eaten dot
    DOTS_PER_GROWTH = 3 # Amount of dots to be eaten before the snake grows

    # --------------
    # Game variables
    # --------------

    board = [[0 for x in range(BOARD_DIM_X)] for y in range(BOARD_DIM_Y)]   # Initialize the board matrix
    score = 0


    def ___init__(self):
        j = 5


    def get_successors(self):
        return [Moves.UP, Moves.RIGHT, Moves.DOWN, Moves.LEFT]
        

    def get_score(self):
        return 0


    def is_game_over(self):
        return False

