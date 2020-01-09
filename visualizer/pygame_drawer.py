import pygame
from pygame import Color
from game import Board

class BoardDrawer:

    SQUARE_SIZE = 20      # Sets the size of each block

    pygame.display.set_caption('pySnake')
    screen = pygame.display.set_mode((SQUARE_SIZE * Board.BOARD_DIM_X, SQUARE_SIZE *Board.BOARD_DIM_Y))


    def __init__(self):
        pygame.init()

    def drawBoard (self, board):
        #pygame.event.get()
        self.screen.fill(Color(0, 0, 0))

        game_space = board.get_game_view()

        for location in board.get_body_locations_asarray():
            white = Color(255, 255, 255)
            self.draw_square(location, white)

        yellow = Color(255, 255, 0)
        self.draw_square(board.dot_location, yellow) 
        pygame.display.update()

    def draw_square(self, location, color):
        x_loc = location[0]
        y_loc = location[1]
        square = pygame.Rect(x_loc*self.SQUARE_SIZE, y_loc*self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)
        pygame.draw.rect(self.screen, color, square)