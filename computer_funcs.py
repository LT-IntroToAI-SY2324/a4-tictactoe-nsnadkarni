import random


def def_comp_row(player: str, board: list) -> int:
        l = ["X", "O"]
        a = l.index(player)
        for i in [0, 3, 6]:
            if board[i] == player and board[i + 1] == player:
                if(board[i + 2] == l[not a]):
                    return -1
                return i + 2
            elif board[i] == player and board[i + 2] == player:
                if(board[i + 1] == l[not a]):
                    return -1
                return i + 1
            elif board[i + 1] == player and board[i + 2] == player:
                if(board[i] == l[not a]):
                    return -1
                return i

        return -1

def def_comp_col(player: str, board: list) -> int:
    l = ["X", "O"]
    a = l.index(player)
    for i in range(3):
        if board[i] == player and board[i + 3] == player:
            if(board[i + 6] == l[not a]):
                return -1
            return i + 6
        elif board[i] == player and board[i + 6] == player:
            if(board[i + 3] == l[not a]):
                return -1
            return i + 3
        elif board[i + 3] == player and board[i + 6] == player:
            if(board[i] == l[not a]):
                return -1
            return i

    return -1


def def_comp_diag(player: str, board: list) -> int:
    l = ["X", "O"]
    a = l.index(player)
    if board[0] == player and board[4] == player:
        if(board[8] == l[not a]):
            return -1
        return 8
    elif board[0] == player and board[8] == player:
        if(board[4] == l[not a]):
            return -1
        return 4
    elif board[4] == player and board[8] == player:
        if(board[0] == l[not a]):
            return -1
        return 0

    if board[2] == player and board[4] == player:
        if(board[6] == l[not a]):
            return -1
        return 6
    elif board[2] == player and board[6] == player:
        if(board[4] == l[not a]):
            return -1
        return 4
    elif board[4] == player and board[6] == player:
        if(board[2] == l[not a]):
            return -1
        return 2

    return -1

########

def bounds(pos: int, board: list) -> bool:
    if pos > 8 or pos < 0 or board[pos] != "*":
        return False
    return True

def prospect(player: str, board: list) -> int:
    l = ["X", "O"]
    a = l.index(player)

    for i in range(9):
        if i == 4 and board[i] == player:
            if bounds(i - 2, board):
                if bounds(i + 2, board):
                    return i - 2
        if i == 2 and board[i] == player:
            if bounds(i + 2, board):
                if bounds(i + 4, board):
                    return i + 2
        if i == 6 and board[i] == player:
            if bounds(i - 2, board):
                if bounds(i - 4, board):
                    return i + 2

        if i == 0 and board[i] == player:
            if bounds(i + 4, board):
                if bounds(i + 8, board):
                    return i + 4
        if i == 4 and board[i] == player:
            if bounds(i - 4, board):
                if bounds(i + 4, board):
                    return i + 4
        if i == 8 and board[i] == player:
            if bounds(i - 4, board):
                if bounds(i - 8, board):
                    return i - 8


        if board[i] == player:
            if i == 0:
                if bounds(i + 1, board):
                    if bounds(i + 2, board):
                        return i + 2
            if i == 3:
                if bounds(i + 1, board):
                    if bounds(i + 2, board):
                        return i + 2
            if i == 6:
                if bounds(i + 1, board):
                    if bounds(i + 2, board):
                        return i + 2

        if board[i] == player:
            if i == 0:
                if bounds(i + 3, board):
                    if bounds(i + 6, board):
                        return i + 6
            if i == 1:
                if bounds(i + 3, board):
                    if bounds(i + 6, board):
                        return i + 6
            if i == 2:
                if bounds(i + 3, board):
                    if bounds(i + 6, board):
                        return i + 6
            

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(arr)

    while arr:
        random_number = arr.pop()
        if bounds(random_number, board):
            return random_number
            
            

def comp_best_move(player: str, board: list) -> int:
    l = ["X", "O"]
    a = l.index(player)
    if def_comp_col(player, board) != -1:
        return def_comp_col(player, board)
    if def_comp_row(player, board) != -1:
        return def_comp_row(player, board)
    if def_comp_diag(player, board) != -1:
        return def_comp_diag(player, board)
    if def_comp_col(l[not a], board) != -1:
        return def_comp_col(l[not a], board)
    if def_comp_row(l[not a], board) != -1:
        return def_comp_row(l[not a], board)
    if def_comp_diag(l[not a], board) != -1:
        return def_comp_diag(l[not a], board)

    return prospect(player, board)