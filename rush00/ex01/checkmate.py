PIECE_MAP = {
    'K': '♔',  # King
    'Q': '♕',  # Queen
    'R': '♖',  # Rook
    'B': '♗',  # Bishop
    'P': '♟',  # Pawn
    '.': '·'    # ช่องว่าง
}

def print_pretty_board(board_str):
    if not isinstance(board_str, str):
        return

    for line in board_str.splitlines():
        pretty_line = ""
        for char in line:
            symbol = PIECE_MAP.get(char, char)
            pretty_line += symbol + " "
        print(pretty_line)
        
def is_piece(char):
    return char == 'P' or char == 'B' or char == 'R' or char == 'Q'

def check_pawn(board, row, col):

    # Pawn (P):
    # . . . . . . .
    # . . . . . . .
    # . . X . X . .
    # . . . P . . .
    # . . . . . . .
    # . . . . . . .
    # . . . . . . .

    if row == 0:
        return False

    # ทแยงขึ้นซ้าย
    if col - 1 >= 0:
        if board[row - 1][col - 1] == 'K':
            return True

    # ทแยงขึ้นขวา
    if col + 1 < len(board):
        if board[row - 1][col + 1] == 'K':
            return True

    return False

def check_bishop(board, row, col):

    # Bishop (B):
    # X . . . . . X
    # . X . . . X .
    # . . X . X . .
    # . . . B . . .
    # . . X . X . .
    # . X . . . X .
    # X . . . . . X

    size = len(board)

    # ทแยงขึ้นซ้าย
    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 'K':
            return True
        if is_piece(board[r][c]):
            break
        r = r - 1
        c = c - 1

    # ทแยงขึ้นขวา
    r = row - 1
    c = col + 1
    while r >= 0 and c < size:
        if board[r][c] == 'K':
            return True
        if is_piece(board[r][c]):
            break
        r = r - 1
        c = c + 1

    # ทแยงลงซ้าย
    r = row + 1
    c = col - 1
    while r < size and c >= 0:
        if board[r][c] == 'K':
            return True
        if is_piece(board[r][c]):
            break
        r = r + 1
        c = c - 1

    # ทแยงลงขวา
    r = row + 1
    c = col + 1
    while r < size and c < size:
        if board[r][c] == 'K':
            return True
        if is_piece(board[r][c]):
            break
        r = r + 1
        c = c + 1

    return False

def check_rook(board, row, col):

    # Rook (R):
    # . . . X . . .
    # . . . X . . .
    # . . . X . . .
    # X X X R X X X
    # . . . X . . .
    # . . . X . . .
    # . . . X . . .

    size = len(board)

    # ขึ้น
    r = row - 1
    while r >= 0:
        if board[r][col] == 'K':
            return True
        if is_piece(board[r][col]):
            break
        r = r - 1

    # ลง
    r = row + 1
    while r < size:
        if board[r][col] == 'K':
            return True
        if is_piece(board[r][col]):
            break
        r = r + 1

    # ซ้าย
    c = col - 1
    while c >= 0:
        if board[row][c] == 'K':
            return True
        if is_piece(board[row][c]):
            break
        c = c - 1

    # ขวา
    c = col + 1
    while c < size:
        if board[row][c] == 'K':
            return True
        if is_piece(board[row][c]):
            break
        c = c + 1

    return False

def check_queen(board, row, col):

    # Queen (Q)
    # X . . X . . X
    # . X . X . X .
    # . . X X X . .
    # X X X Q X X X
    # . . X X X . .
    # . X . X . X .
    # X . . X . . X

    if check_bishop(board, row, col):
        return True
    if check_rook(board, row, col):
        return True
    return False

def is_valid(rows):

    if len(rows) == 0:
        return False

    for row in rows:
        if len(row) != len(rows):
            return False

    count = 0
    for row in rows:
        for char in row:
            if char == 'K':
                count = count + 1
    if count != 1:
        return False

    return True

def checkmate(board):

    if not isinstance(board, str):
        print("Error")
        return

    rows = board.splitlines()

    if not is_valid(rows):
        print("Error")
        return
    
    for row in range(len(rows)):
        for col in range(len(rows)):
            piece = rows[row][col]

            if piece == 'P':
                if check_pawn(rows, row, col):
                    print("Success")
                    return
            elif piece == 'R':
                if check_rook(rows, row, col):
                    print("Success")
                    return
            elif piece == 'B':
                if check_bishop(rows, row, col):
                    print("Success")
                    return
            elif piece == 'Q':
                if check_queen(rows, row, col):
                    print("Success")
                    return

    print("Fail")