import game
import pygame
from visualizer.printboard import BoardPrinter
from visualizer.pygame_drawer import BoardDrawer
from moves import Moves
from move_input.random_agent import RandomAgent
from move_input.basic_agent import BasicAgent
from move_input.better_agent import BetterAgent
from move_input.user_input import UserAgent
import time

class pySnake:

    TIME_PER_FRAME = 0.05        # The time (in seconds) that one step should ideally take

    def __init__(self):
        print("Initializing game...")

        isPlaying = True        # Keep track of the game state (playing/game over)
        
        board = game.Board()        # Initalize the board

        # Choose gameplay input
        #agent = RandomAgent()       # This agent selects a random possible move
        #agent = BasicAgent()        # This agent selects a move closer to the dot
        #agent = BetterAgent()       # This agent selects a move closer to the dot, but farther from its tail and the edge
        agent = UserAgent()         # This records and processes user input

        # Choose a visualizer
        #visualizer = BoardPrinter() # Select a visualiser (terminal)
        visualizer = BoardDrawer()  # Select a visualiser (view screen)

        while (isPlaying):
            start = time.time()

            # Visualize this step
            visualizer.drawBoard(board)

            # Check if the game is over
            isPlaying = not board.is_game_over()

            # Get the next move
            next_move = agent.get_direction(board)

            # Perform the move
            board.move( next_move )

            if not isPlaying:
                break

            end = time.time()
            frame_time = end - start
            sleep_time = self.TIME_PER_FRAME - frame_time
            if frame_time > 0 and sleep_time > 0:
                time.sleep( sleep_time )
            
pySnake()
            