from player import HumanPlayer, ComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [[j for j in self.board[i*3 : (i+1)*3]] for i in range(3)]:
              print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_num():
        for board_num in [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]:
            print("| " + " | ".join(board_num) + " |")

    def is_empty_squares(self):
        return " " in self.board

    def available_moves(self):
        return [spot for spot, i in enumerate(self.board) if i == " "]

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Checking row
        row_index = square//3
        if all(k == letter for spot, k in enumerate(self.board[row_index*3:(row_index+1)*3])):
            return True

        # Checking column
        col_index = square % 3
        if all([i == letter for spot, i in enumerate(self.board) if spot % 3 == col_index]):
            return True

        # Check diagonals
        if square % 2:
            if all([i == letter for spot, i in enumerate(self.board) if spot in [0, 4, 8]]):
                return True

            if all([i == letter for spot, i in enumerate(self.board) if spot in [6, 4, 2]]):
                return True


def play(game, x_player, o_player, print_game = True):
    letter = 'x'
    game.print_board_num()

    while game.is_empty_squares():
        if letter == "x":
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f"Makes a move to {square}")
                game.print_board()
                if game.current_winner:
                    print(letter + "Wins!!")
                    break

            letter = "x" if letter == "o" else "o"


if __name__ == '__main__':
    player_x = HumanPlayer("x")
    player_o = ComputerPlayer("o")
    ttt = TicTacToe()
    play(ttt, player_x, player_o, print_game=True)







