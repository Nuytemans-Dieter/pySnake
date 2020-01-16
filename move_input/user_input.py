import pygame
from moves import Moves

class UserAgent:
    def get_direction(self, board):
        choice = None

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                                # Arrow keys               # Azerty keyboard
                if event.key == pygame.K_LEFT  or event.key == pygame.K_a:
                    choice = Moves.LEFT
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    choice = Moves.RIGHT
                if event.key == pygame.K_UP    or event.key == pygame.K_w:
                    choice = Moves.UP
                if event.key == pygame.K_DOWN  or event.key == pygame.K_s:
                    choice = Moves.DOWN

        possible_moves = board.get_successors()
        if possible_moves.__contains__(choice):
            return choice
        else:
            return None