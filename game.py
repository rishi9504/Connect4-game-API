import random
import time
import json

ROWS       = 6
COLUMNS    = 7

PIECE_NONE = ' '
PIECE_ONE  = 'x'
PIECE_TWO  = 'o'

PIECE_COLOR_MAP = {
    PIECE_NONE : 'NONE',
    PIECE_ONE  : 'YELLOW',
    PIECE_TWO  : 'RED',
}

DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
)



# Board Functions

def create_board(rows=ROWS, columns=COLUMNS):
    ''' Creates empty Connect 4 board '''
    board = []

    for row in range(rows):
        board_row = []
        for column in range(columns):
            board_row.append(PIECE_NONE)
        board.append(board_row)

    return board

def print_board(board):
    ''' Prints Connect 4 board '''
    res = []
    for row in board:
        print('|' + '|'.join(row) + '|')

def drop_piece(board, column, piece):
    ''' Attempts to drop specified piece into the board at the
    specified column. If this succeeds, return True, otherwise return False.
    '''

    for row in reversed(board):
        if row[column] == PIECE_NONE:
            row[column] = piece
            return True

    return False

def find_winner(board, length=4):
    ''' Return if the board has a winner '''

    rows    = len(board)
    columns = len(board[0])

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == PIECE_NONE:
                continue

            if check_piece(board, row, column, length):
                return board[row][column]

    return None

def check_piece(board, row, column, length):
    ''' Check if the piece satisfy the condition for winning
    '''
    rows    = len(board)
    columns = len(board[0])

    for dr, dc in DIRECTIONS:
        found_winner = True

        for i in range(1, length):
            r = row + dr*i
            c = column + dc*i

            if r not in range(rows) or c not in range(columns):
                found_winner = False
                break

            if board[r][c] != board[row][column]:
                found_winner = False
                break

        if found_winner:
            return True

    return False

def write_board(board):
	result = []
	rows = len(board)
	columns = len(board[0])
	for row in range(rows):
		tmp = []
		for column in range(columns):
			tmp.append(board[row][column])
		result.append(tmp)

	with open("board.json", 'w') as fp:
		json.dumps(result)
	return res


def reset_board(Board):
	rows = len(Board)
	columns = len(Board[0])
	for row in range(rows):
		for column in range(columns):
			Board[row][column] = PIECE_NONE
