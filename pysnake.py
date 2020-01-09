import game
from visualizer.printboard import BoardPrinter
from visualizer.board_drawer import BoardDrawer
import time

class pySnake:

    TIME_PER_FRAME = 0.5        # The time (in seconds) that one step should ideally take

    def __init__(self):
        print("Initializing game...")

        isPlaying = True        # Keep track of the game state (playing/game over)
        
        board = game.Board()        # Initalize the board
        visualizer = BoardPrinter() # Select a visualiser (terminal)
        # visualizer = BoardDrawer()  # Select a visualiser (view screen)

        while (isPlaying):
            start = time.time()

            # Visualize this step
            visualizer.drawBoard(board)

            # Check if the game is over
            isPlaying = not board.is_game_over()

            # Get the next move
            next_move = None

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
            