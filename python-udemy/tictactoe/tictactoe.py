from IPython.display import clear_output

def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = [' '] * 10
display_board(test_board)


def player_input():
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
