import pygame
from moves import Moves

class UserAgent:
    def get_direction(self, board):
        choice = None

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    choice = Moves.LEFT
                if event.key == pygame.K_RIGHT:
                    choice = Moves.RIGHT
                if event.key == pygame.K_UP:
                    choice = Moves.UP
                if event.key == pygame.K_DOWN:
                    choice = Moves.DOWN

        possible_moves = board.get_successors()
        if possible_moves.__contains__(choice):
            return choice
        else:
            return None