import random

class RandomAgent:
    def get_direction(self, board):
        possible_moves = board.get_successors()
        choice = random.randint(0, 2)
        return possible_moves[ choice ]