# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working

def check_row(pos: int, player: str, board: list) -> bool:
    if board[pos] == player and board[pos + 1] == player and board[pos + 2] == player:
        return True
    return False


def check_col(pos: int, player: str, board: list) -> bool:
    if board[pos] == player and board[pos + 3] == player and board[pos + 6] == player:
        return True
    return False

def check_diag(pos: int, player: str, board: list, a: bool) -> bool:
    if(a == True):
        if board[pos] == player and board[pos + 4] == player and board[pos + 8] == player:
            return True
        return False
    else:
        if board[pos] == player and board[pos + 2] == player and board[pos + 4] == player:
            return True
        return False

class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self) -> None:
        self.board = ['*'] * 9


    def __str__(self) -> str:
        return f"{self.board[0]} {self.board[1]} {self.board[2]}\n{self.board[3]} {self.board[4]} {self.board[5]}\n{self.board[6]} {self.board[7]} {self.board[8]}"


    def make_move(self, player: str, pos: int) -> bool:
        if pos > 8 or pos < 0 or self.board[pos] != "*":
            return False
        self.board[pos] = player
        return True


    def has_won(self, player: str):
        b = player
        c = self.board
        if check_col(0, b, c) or check_col(1, b, c) or check_col(2, b, c):
            return True
        if check_row(0, b, c) or check_row(3, b, c) or check_row(6, b, c):
            return True
        if check_diag(0, b, c, True) or check_diag(2, b, c, False):
            return True
        
        return False 

    def game_over(self):
        b = "X"
        c = self.board

        for i in range(3):
            if check_col(i, b, c):
                return True
        for i in [0, 3, 6]:
            if check_row(i, b, c):
                return True
        if check_diag(0, b, c, True) or check_diag(2, b, c, False):
            return True

        b = "O"
        c = self.board
        for i in range(3):
            if check_col(i, b, c):
                return True
        for i in [0, 3, 6]:
            if check_row(i, b, c):
                return True
        if check_diag(0, b, c, True) or check_diag(2, b, c, False):
            return True

        for i in range(8):
            if(self.board[i] == '*'):
                return False
        return True

    def clear(self):
        self.board = ['*'] * 9

    pass


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    print(brd)
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    # uncomment to play!
    #play_tic_tac_toe()
