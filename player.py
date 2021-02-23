import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if game.is_empty_squares:
            square = int(input(self.letter + "'s Turn to play, make move (0 - 8 > "))
            return square


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
            square = random.choice(game.available_moves())
            return square




