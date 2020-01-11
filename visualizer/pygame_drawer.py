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
    big_font = None

    def __init__(self):
        pygame.init()
        #pygame.font.init()
        self.font = myfont = pygame.font.SysFont('Comic Sans MS', self.SQUARE_SIZE)
        self.big_font = myfont = pygame.font.SysFont('Comic Sans MS', 3 * self.SQUARE_SIZE)

    def drawBoard (self, board):
        
        # Create basic screen layout with a bottom box
        self.screen.fill(self.black)
        bottom_bar_rect = pygame.Rect(0,  Board.BOARD_DIM_Y * self.SQUARE_SIZE, self.SQUARE_SIZE * Board.BOARD_DIM_Y, 3 * self.SQUARE_SIZE)
        pygame.draw.rect(self.screen, self.grey, bottom_bar_rect)
        
        # Draw score
        score = "Score: " + str(board.score)
        score_x = self.SQUARE_SIZE * 3
        score_y = (1 + Board.BOARD_DIM_Y) * self.SQUARE_SIZE
        self.draw_text((score_x, score_y), self.white, score)

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

    def show_end_screen(self, board):
        # Create a black screen
        self.screen.fill(self.black)

        # Display the game title
        text_render = self.big_font.render("pySnake", True, self.light_green)
        text_rect = text_render.get_rect(center=((self.SQUARE_SIZE * board.BOARD_DIM_X) /2, self.SQUARE_SIZE * 5 ))
        self.screen.blit(text_render, text_rect)

        score = "Your score: " + str(board.score)
        score_render = self.big_font.render(score, True, self.white)
        score_rect = score_render.get_rect(center=((self.SQUARE_SIZE * board.BOARD_DIM_X) /2, self.SQUARE_SIZE * 12 ))
        self.screen.blit(score_render, score_rect)

        # Update the view
        pygame.display.update()

    
    def draw_text(self, location, color, text):
        text_render = self.font.render(text, True, color)
        x = location[0]
        y = location[1]
        self.screen.blit(text_render, (x, y))

    def draw_square(self, location, color):
        x_loc = location[0]
        y_loc = location[1]
        square = pygame.Rect(x_loc*self.SQUARE_SIZE, y_loc*self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)
        pygame.draw.rect(self.screen, color, square)