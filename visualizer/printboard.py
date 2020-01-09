import game

class BoardPrinter:
    def drawBoard (self, board):
        gameSpace = board.get_game_view()
        gameView = ""

        gameView += (game.Board.BOARD_DIM_X + 2) * "+ " + "\n"

        for row in gameSpace:
            gameView += "+ "
            for value in row:
                gameView += value + " "
            gameView += "+"
            gameView += "\n"

        gameView += (game.Board.BOARD_DIM_X + 2) * "+ " + "\n"
        print (gameView)