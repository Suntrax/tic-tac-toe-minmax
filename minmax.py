import random


class MinMax:
    def __init__(self, difficulty, ai_symbol, human_symbol):
        self.difficulty = difficulty
        self.ai_symbol = ai_symbol
        self.human_symbol = human_symbol

    def __str__(self):
        return "MinMax Algorithm"

    @staticmethod
    def random_move(possible_moves: list):
        return random.choice(possible_moves)

    def return_algo_move(self, game):
        if self.difficulty == 1:
            return self.random_move(game.get_available_moves())

        if self.difficulty == 2:
            return self.find_best_move(game)

        return None

    def minimax(self, game, depth=0, maximizing=True):
        if self.game_finished(game):
            return self.evaluate(game, depth)

        best_score = -float("inf") if maximizing else float("inf")

        # minmax here
        # generate all moves
        moves = game.get_available_moves()

        # loop through them
        # simulate each move
        # call minimax again, recursion
        # undo move
        for move in moves:
            game.place_symbol(move, self.ai_symbol if maximizing else self.human_symbol)
            new_score = self.minimax(game, depth+1, maximizing=False if maximizing else True)
            best_score = max(best_score, new_score) if maximizing else min(best_score, new_score)
            game.undo_move(move)

        # pick best result
        return best_score

    def evaluate(self, game, depth):
        winner = game.get_winner()

        # AI wins
        if winner == self.ai_symbol:
            return 10 - depth

        # Human wins
        if winner == self.human_symbol:
            return depth - 10

        # Draw
        return 0

    @staticmethod
    def game_finished(game):
        return game.get_winner() is not None or game.is_draw()

    def find_best_move(self, game):
        best_score = -float("inf")
        best_move = None

        for move in game.get_available_moves():
            # place move
            game.place_symbol(move, self.ai_symbol)
            # call minimax for score
            score = self.minimax(game, depth=0, maximizing=False)
            # undo move
            game.undo_move(move)
            # store both score and move
            if score > best_score:
                best_score = score
                best_move = move

        # pick move with best score
        return best_move
