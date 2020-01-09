
class BoardPrinter:
    def drawBoard (self, board):
        gameSpace = board.get_game_view()
        gameView = ""

        for row in gameSpace:
            gameView += "+"
            for value in row:
                gameView += value + " "
            gameView += "+"
            gameView += "\n"

        print (gameView)
        print("---")