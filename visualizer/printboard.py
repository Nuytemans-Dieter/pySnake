import game

class BoardPrinter:
    def drawBoard (self, board):
        game_space = board.get_game_view()

        game_view =  "|--------------|" + "\n"
        game_view += "| Score: " + str(board.score) + (6 - str(board.score).__len__()) * " " + "|\n"
        game_view += "|--------------|" + "\n"
        game_view += (game.Board.BOARD_DIM_X + 2) * "+ " + "\n"

        for row in game_space:
            game_view += "+ "
            for value in row:
                game_view += value + " "
            game_view += "+"
            game_view += "\n"

        game_view += (game.Board.BOARD_DIM_X + 2) * "+ " + "\n"
        print(game_view)
