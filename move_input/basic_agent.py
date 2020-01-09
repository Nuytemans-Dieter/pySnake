from pySnake_util.vector import add_vectors_2D, distance_squared

class BasicAgent:
    def get_direction(self, board):
        body_locations = board.get_body_locations_asarray()
        head_location = body_locations[-1]
        possible_moves = board.get_successors()

        (distance_to_dot, to_tail, to_wall) = board.get_game_data()
        new_move = None
        
        for move in possible_moves:
            new_head_location = add_vectors_2D(head_location, board.DIRECTION_OFFSET_VECTOR[move])
            new_distance = distance_squared(new_head_location, board.dot_location)
            if new_distance < distance_to_dot:
                distance_to_dot = new_distance
                new_move = move

        return new_move
