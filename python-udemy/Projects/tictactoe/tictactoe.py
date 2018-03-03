from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


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
        return('0', 'X')


def place_marker(board, marker, position):
    board[position] = marker


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



import random

def choose_first():
    flip = random.randint(0, 1)
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
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position


def replay():
    choice = input('Play again? Enter Yes or No ')
    return choice == 'Yes'

# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe')

while True:
    # PLAY THE GAME

    # SET EVERYTHING UP (BOARD, WHO'S FIRST, CHOOSE MARKERS X, 0)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? Yes or No? ')

    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False

    # GAMEPLAY
    while game_on:

        # PLAYER 1 TURN
        if turn == 'Player 1':

            # SHOW THE BOARD
            display_board(the_board)

            # CHOOSE A position
            position = player_choice(the_board)

            # PLACE MARKER ON THE POSITION
            place_marker(the_board, player1_marker, position)

            # CHECK IF THEY WON
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'

        # PLAYER 2 TURN
        else:
            # SHOW THE BOARD
            display_board(the_board)

            # CHOOSE A position
            position = player_choice(the_board)

            # PLACE MARKER ON THE POSITION
            place_marker(the_board, player2_marker, position)

            # CHECK IF THEY WON
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'

    # BREAKOUT OF THE WHILE LOOP ON replay()
    if not replay():
        break
