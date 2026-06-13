from tictactoe import TicTacToe


if __name__ == "__main__":
    # difficulties
    # 1 = random moves
    # 2 = short lookahead
    # 3 = always draw

    difficulty = 2

    # player one symbol can be chosen and player two symbol
    # game = TicTacToe(1, "p", "u")
    # add choice who begins

    game = TicTacToe(difficulty)
    game.start()