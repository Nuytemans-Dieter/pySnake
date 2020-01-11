import pygame
from pygame import Color
from game import Board

class BoardDrawer:

    SQUARE_SIZE = 17      # Sets the size of each block

    # Colors
    white = Color(255, 255, 255)
    black = Color(0, 0, 0)
    grey = Color(133,133,133)
    yellow = Color(255, 255, 0)
    light_green = Color(0, 181, 57)
    dark_green = Color(0, 128, 40)

    pygame.display.set_caption('pySnake')
    screen = pygame.display.set_mode((SQUARE_SIZE * Board.BOARD_DIM_X, SQUARE_SIZE * Board.BOARD_DIM_Y + 3 * SQUARE_SIZE))
    font = None

    def __init__(self):
        pygame.init()
        #pygame.font.init()
        self.font = myfont = pygame.font.SysFont('Comic Sans MS', self.SQUARE_SIZE)

    def drawBoard (self, board):
        
        # Create basic screen layout with a bottom box
        self.screen.fill(self.black)
        bottom_bar_rect = pygame.Rect(0,  Board.BOARD_DIM_Y * self.SQUARE_SIZE, self.SQUARE_SIZE * Board.BOARD_DIM_Y, 3 * self.SQUARE_SIZE)
        pygame.draw.rect(self.screen, self.grey, bottom_bar_rect)
        
        # Draw score
        score = "Score: " + str(board.score)
        score_render = self.font.render(score, True, self.white)
        score_x = self.SQUARE_SIZE * 3
        score_y = (1 + Board.BOARD_DIM_Y) * self.SQUARE_SIZE
        self.screen.blit(score_render, (score_x, score_y))

        # Draw the score dot
        self.draw_square(board.dot_location, self.yellow)

        # Draw the snake (alternating light and dark green pattern: head is always dark green)
        body_locations = board.get_body_locations_asarray()
        body_counter = len(body_locations)
        for location in body_locations:
            if body_counter % 2 is 0:
                self.draw_square(location, self.light_green)
            else:
                self.draw_square(location, self.dark_green)
            body_counter -= 1

        # Perform a screen update
        pygame.display.update()

    def draw_square(self, location, color):
        x_loc = location[0]
        y_loc = location[1]
        square = pygame.Rect(x_loc*self.SQUARE_SIZE, y_loc*self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)
        pygame.draw.rect(self.screen, color, square)