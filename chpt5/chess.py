def isValidChessBoard(k,v):
    #Each player can only have at most 16 pieces
    #at most 8 pawns, one king
    #all pieces must be on a valid space from '1a' to '8h'
    #a piece can’t be on space '9z'
    #The piece names begin with either a 'w' or 'b' followed by
    #'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
    #This function should detect when a bug has resulted in an improper chess board.

    #k = location
    #v = piece name

    #test for 16 pieces
    bcounter = 0
    wcounter = 0
    k[0]

    #test for location
    k[1] = abcdefgh

    #test for 8 pawns, 1 king

    return True
    return False


def validate_board(board_dict):
    # check for one black and one white king


    # check for a maximum of 16 pieces per player


    # check for at most 8 pawns per player

    # check for a valid location


    # check if the name starts with a "w" or "b"


    # check if the piece name is valid


# testing boards
print(validate_board({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))  # True
print(validate_board({"1a": "bpawn", "2a": "wking"}))  # False: no bking
print(validate_board({"1a": "wking", "2a": "wking", "3c": "bbishop"}))  # False: cannot have 2 white kings, no bking
print(validate_board({"1a": "bking", "9z": "wking"}))  # False: 9z is an invalid position
