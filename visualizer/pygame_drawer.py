import pygame
from pygame import Color
from game import Board
from high_scores import High_Scores
from pySnake_util.vector import add_vectors_2D

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
    screen = pygame.display.set_mode((SQUARE_SIZE * (Board.BOARD_DIM_X + 2), SQUARE_SIZE * Board.BOARD_DIM_Y + 4 * SQUARE_SIZE))
    
    small_font = None
    medium_font = None
    big_font = None

    def __init__(self):
        pygame.init()
        #pygame.font.init()
        self.small_font =  pygame.font.SysFont('Comic Sans MS', self.SQUARE_SIZE)
        self.medium_font = pygame.font.SysFont('Comic Sans MS', 2 * self.SQUARE_SIZE)
        self.big_font =    pygame.font.SysFont('Comic Sans MS', 3 * self.SQUARE_SIZE)

    def drawBoard (self, board):
        
        # Create grey background
        self.screen.fill(self.grey)
        # Create black play area
        play_room = (self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE * Board.BOARD_DIM_X, self.SQUARE_SIZE * Board.BOARD_DIM_Y)
        pygame.draw.rect(self.screen, self.black, play_room)
        # bottom_bar_rect = pygame.Rect(0, Board.BOARD_DIM_Y * self.SQUARE_SIZE, self.SQUARE_SIZE * Board.BOARD_DIM_X, 3 * self.SQUARE_SIZE)
        # pygame.draw.rect(self.screen, self.grey, bottom_bar_rect)
        
        # Draw score
        score = "Score: " + str(board.score)
        score_x = self.SQUARE_SIZE * 4
        score_y = (2 + Board.BOARD_DIM_Y) * self.SQUARE_SIZE
        self.draw_text((score_x, score_y), self.white, score)

        # Draw the score dot
        self.draw_square(add_vectors_2D(board.dot_location, (1, 1)), self.yellow)

        # Draw the snake (alternating light and dark green pattern: head is always dark green)
        body_locations = board.get_body_locations_asarray()
        body_counter = len(body_locations)
        for location in body_locations:
            location = add_vectors_2D(location, (1, 1))
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

        # Display the player's score
        score = "Your score: " + str(board.score)
        score_render = self.big_font.render(score, True, self.white)
        score_rect = score_render.get_rect(center=((self.SQUARE_SIZE * board.BOARD_DIM_X) /2, self.SQUARE_SIZE * 12 ))
        self.screen.blit(score_render, score_rect)

        # Display the high score title
        hscore_title_render = self.medium_font.render("Highscores:", True, self.white)
        hscore_title_rect = hscore_title_render.get_rect(center=((self.SQUARE_SIZE * board.BOARD_DIM_X) /2, self.SQUARE_SIZE * 16 ))
        self.screen.blit(hscore_title_render, hscore_title_rect)

        # Get the high scores
        high_scores = High_Scores()
        high_scores = high_scores.get_highscores()

        # Display the high scores
        num = 1
        for h_score in high_scores:
            text = "#" + str(num) + " - " + str(h_score)
            score_render = self.medium_font.render(text, True, self.white)
            location = ((self.SQUARE_SIZE * board.BOARD_DIM_X) /4, self.SQUARE_SIZE * (16 + num * 2))
            self.screen.blit(score_render, location)
            num += 1

        # Update the view
        pygame.display.update()

    
    def draw_text(self, location, color, text):
        text_render = self.small_font.render(text, True, color)
        x = location[0]
        y = location[1]
        self.screen.blit(text_render, (x, y))

    def draw_square(self, location, color):
        x_loc = location[0]
        y_loc = location[1]
        square = pygame.Rect(x_loc*self.SQUARE_SIZE, y_loc*self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)
        pygame.draw.rect(self.screen, color, square)