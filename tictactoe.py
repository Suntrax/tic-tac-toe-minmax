from typing import Any
from minmax import MinMax


class TicTacToe:
    def __init__(self, difficulty: int = 1, player_one_symbol: str = "x", player_two_symbol: str = "o"):
        self.difficulty = difficulty
        self.player_one_symbol = str(player_one_symbol)
        self.player_two_symbol = str(player_two_symbol)
        self.current_player = "human"
        self.board = []
        self.minmax = MinMax(self.difficulty, ai_symbol=self.player_two_symbol, human_symbol=self.player_one_symbol)

    def __str__(self):
        return "Tic Tac Toe Game Class"

    def start(self):
        self.clear_board()

        while True:
            self.print_board()
            self.make_move()

            winner = self.get_winner()

            if winner:
                self.print_board()
                print(f"{winner} won!")
                break

            if self.is_draw():
                self.print_board()
                print("It's a draw!")
                break

    def clear_board(self):
        self.board = [[" "] * 3 for _ in range(3)]

    def print_board(self):
        for line in self.board:
            print(line)

    def get_available_moves(self) -> list:
        moves = []

        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == " ":
                    moves.append((i, j))

        return moves

    def make_move(self):
        moves = self.get_available_moves()
        formatted_move = (-1, -1)
        if self.current_player == "human":
            while formatted_move not in moves:
                move = input(f"\n{self.current_player} move (eg. 0 1): ")
                formatted_move = move.split(" ")

                try:
                    formatted_move = (int(formatted_move[0]), int(formatted_move[1]))
                except IndexError:
                    print("Move unavailable, try again.")
                    continue

                if formatted_move not in moves:
                    print("Move unavailable, try again.")
            self.place_symbol(formatted_move, self.player_one_symbol)

        else:
            formatted_move = self.minmax.return_algo_move(self)
            print(f"\n{self.current_player} Move: {formatted_move}")
            self.place_symbol(formatted_move, self.player_two_symbol)

        self.current_player = "ai" if self.current_player == "human" else "human"

    def place_symbol(self, move, symbol):
        self.board[move[0]][move[1]] = symbol

    def undo_move(self, move):
        self.board[move[0]][move[1]] = " "

    def get_winner(self) -> Any | None:
        # left to right
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][0] != " ":
            return self.board[0][0]

        if self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][1] != " ":
            return self.board[1][1]

        if self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][2] != " ":
            return self.board[2][2]

        # up to down
        if self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[0][0] != " ":
            return self.board[0][0]

        if self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[1][1] != " ":
            return self.board[1][1]

        if self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[2][2] != " ":
            return self.board[2][2]

        # top left to bot right
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[1][1] != " ":
            return self.board[1][1]

        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[1][1] != " ":
            return self.board[1][1]

        return None

    def is_draw(self):
        return len(self.get_available_moves()) == 0 and self.get_winner() is None
