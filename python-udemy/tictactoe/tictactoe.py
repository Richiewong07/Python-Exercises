from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = [' '] * 10
display_board(test_board)



def player_input():

    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''

    # KEEP ASKING PLAYER 1 TO CHOOSE X OR O
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    # ASSIGN PLAYER 2, THE OPPOSITE MARKER
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player1_marker, player2_marker = player_input()



def place_marker(board, marker, position):
    board[position] = marker

place_marker(test_board, '$', 8)
display_board(test_board)



def win_check(board, mark):

    # WIN TIC TAC TOE?

    # ALL ROWS, AND CHECK TO SEE IF THEY ALL SHARE THE SAME MARKER?
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or

    # ALL COLUMNS, CHECK TO SEE IF MARKER MATCHES
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or

    # 2 DIAGONALS, CHECK TO SEE MATCH
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

display_board(test_board)
win_check(test_board, 'X')



import random

def choose_first():

    flip = random.ranint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'



def space_check(board, position):

    return board[position] == ' '



def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    # BOARD IS FULL IF WE RETURN TRUE
    return True


def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, postion):
        position = int(input('Choose a position: (1-9)'))

    return position


def replay():

    choice = input('Play again? Enter Yes or No')

    return choice == 'Yes'
