from game import Board
from visualizer.printboard import BoardPrinter
from visualizer.board_drawer import BoardDrawer

class pySnake:

    def __init__(self):
        isPlaying = True        # Keep track of the game state (playing/game over)
        
        board = Board()             # Initalize the board
        visualizer = BoardPrinter() # Select a visualiser (terminal)
        # visualizer = BoardDrawer()  # Select a visualiser (view screen)

        while (isPlaying):
            visualizer.drawBoard(board)

            