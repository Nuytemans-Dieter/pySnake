from pySnake_util.vector import add_vectors_2D, distance_squared
from moves import Moves
from game import Board

class BetterAgent:

    max_distance = 0

    def __init__(self):
        if Board.BOARD_DIM_X > Board.BOARD_DIM_Y:
            self.max_distance = Board.BOARD_DIM_X
        else:
            self.max_distance = Board.BOARD_DIM_Y

    def get_direction(self, board):
        # Get snake body and head locations
        body_locations = board.get_body_locations_asarray()
        head_location = body_locations[-1]

        # Get starting parameters
        (distance_to_dot, to_tail, to_wall) = board.get_game_data()
        total_heuristic = distance_to_dot
        new_move = None
        
        # Iterate through all possible moves
        for move in board.get_successors():
            # Calculate the head position and new metric after moving
            new_head_location = add_vectors_2D(head_location, board.DIRECTION_OFFSET_VECTOR[move])
            new_distance = distance_squared(new_head_location, board.dot_location)
            
            # Handle game-losing moves
            distance_to_tail = self.get_distance_to_tail(board, body_locations)
            if distance_to_tail is -1:
                new_heuristic = new_distance
                if new_heuristic < total_heuristic:
                    total_heuristic = new_heuristic
                    new_move = move

        return new_move


    def calculate_heuristic(self, game_data):
        (distance_to_dot, to_tail, to_wall) = game_data
        return distance_to_dot + (self.max_distance - to_tail) + (self.max_distance - to_wall)

    def get_distance_to_tail(self, board, body_locations):
        # Initialize parameters
        dist_to_tail = -1
        looking_for_tail = True

        # Get head location
        head_pos = body_locations[-1]
        next_position = head_pos

        # Iterate until a wall or tail is hit
        while looking_for_tail:
            # Tail distance increment
            dist_to_tail += 1
            
            # Increment position in direction
            next_position = add_vectors_2D(next_position, board.DIRECTION_OFFSET_VECTOR[board.current_direction])
            
            # Collision with tail? looking_for_tail : false
            if body_locations.__contains__(next_position):
                looking_for_tail = False
                return dist_to_tail

            # Collision with the wall? looking_for_tail: false
            if not board.is_location_within_bounds(next_position):
                dist_to_tail = -1
                looking_for_tail = False
                return -1

        return dist_to_tail
