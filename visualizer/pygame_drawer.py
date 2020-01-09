import pygame
from pygame.locals import *
from game import Board

class BoardDrawer:

    screen = None

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((Board.BOARD_DIM_X,Board.BOARD_DIM_Y))


    def drawBoard (self, board):
        Exception("drawBoard is not yet supported by BoardDrawer!")